from flask_cors import CORS, cross_origin
from flask_caching import Cache
#from bson.json_util import dumps
from elasticsearch import Elasticsearch
import json
from flask import Flask, request, Response
import jsonpickle
import io
import hashlib 
import sys

cache = Cache(config={
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
})

app = Flask(__name__)
CORS(app)
cache.init_app(app)


@app.route('/status', methods=["GET"])
@app.route('/', methods=["GET"])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def status():
    return "App is running!"


@app.route('/suggest', methods=["GET"])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
@cache.cached(timeout=50)
def suggest():
    es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
    if not es.ping():
        raise ValueError("Connection failed")

    es.indices.refresh(index="test-index")
    res = es.search(index="test-index", body={"query": {"match_all": {}}}, size=50)
    k = []
    for hit in res['hits']['hits']:
        k.append(hit["_source"])

    return json.dumps(k)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
