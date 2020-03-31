from flask import Flask
from flask_cors import CORS, cross_origin
from flask_caching import Cache
import sys
from bson.json_util import dumps
from datetime import datetime
from elasticsearch import Elasticsearch
from flask import request
import json
import datetime

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
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if not es.ping():
        raise ValueError("Connection failed")

    es.indices.refresh(index="test-index")
    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    k=[]
    for hit in res['hits']['hits']:
        k.append(hit["_source"])

    return dumps(k)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
