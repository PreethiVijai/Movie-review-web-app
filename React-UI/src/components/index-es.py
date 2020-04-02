from datetime import datetime
from elasticsearch import Elasticsearch
from pymongo import MongoClient
#es = Elasticsearch()
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
if not es.ping():
    raise ValueError("Connection failed")
username = "scrumlords"
password = "Bda2020$!"

client = MongoClient("mongodb+srv://scrumlords:"+password+"@cluster0-4ef7e.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client["scraping"]
tweetCol = db["movies_test"]    
for x in tweetCol.find({},{ "_id": 0 }):
    #doc = 
    #{'author': 'kimchy',
    #'text': 'Elasticsearch: cool. bonsai cool.',
    #'timestamp': datetime.now(),
    #}

    res = es.index(index="test-index", doc_type='tweet', id=x[u'movieId'], body=x)
