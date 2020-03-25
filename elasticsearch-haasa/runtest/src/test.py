from datetime import datetime
from elasticsearch import Elasticsearch
from pymongo import MongoClient
#es = Elasticsearch()
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])

username = "scrumlords"
password = ""

client = MongoClient("mongodb+srv://scrumlords:"+password+"@cluster0-4ef7e.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client["scraping"]
tweetCol = db["movies_test"]    
for x in tweetCol.find({},{ "_id": 0 }):
    print(x)
    print("new line")  
    print(x[u'movieId'])
  
    #doc = 
    #{'author': 'kimchy',
    #'text': 'Elasticsearch: cool. bonsai cool.',
    #'timestamp': datetime.now(),
    #}

    res = es.index(index="test-index", doc_type='tweet', id=x[u'movieId'], body=x)
    print(res)

#res = es.get(index="test-index", doc_type='tweet', id=1)
#print(res)

es.indices.refresh(index="test-index")
res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(name)s %(year)s" % hit["_source"])