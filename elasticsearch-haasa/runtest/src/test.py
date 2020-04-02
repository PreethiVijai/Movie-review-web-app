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
db1 = client["realTime"]
tweetCol1 = db1["tweets_test_1"]
for x in tweetCol.find({},{ "_id": 0 }):
    #print(x)
    #print("new line")  
    #print(type(x[u'movieId']))
    movieId=x[u'movieId'].encode('ascii', 'replace')    
    movieId= movieId.decode("utf-8")
    #print(type(movieId))
    myquery = {"movieId":movieId}
    count=0
    avgsentiment=0
    tweetLocations= []
    for doc in tweetCol1.find(myquery):
        #print("entered")
        count+=1
        tweetLocations.append(doc[u'user_place'])
        avgsentiment+=doc[u'sentimentScore']
    if count!=0:    
        avgsentiment= avgsentiment/count
        #print(avgsentiment) 
    else:
        avgsentiment= None       
    x1 = {'name': x[u'name'],
    'movieId': x[u'movieId'],
    'year': x[u'year'],
    'runtime': x[u'runtime'],
    'language': x[u'language'],
    'cast': x[u'cast'],
    'imageurl': x[u'imageurl'],
    'trailer': x[u'trailer'],
    'plot': x[u'plot'],
    'rating': x[u'rating'],
    'genreList': x[u'genreList'],
    'reviewsList': x[u'reviewsList'],
    'watchList': x[u'watchList'],
    'avgsentiment':avgsentiment,
    'tweetLocations': tweetLocations
    }
    #print(x1)
    res = es.index(index="test-index", doc_type='tweet', id=movieId, body=x1)
    #print(res)

#res = es.get(index="test-index", doc_type='tweet', id=1)
#print(res)

es.indices.refresh(index="test-index")
res = es.search(index="test-index", body={"query": {"match_all": {}}})
#res=es.get(index='test-index',doc_type='tweet',id="tt1051906")
#print(res)
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(name)s %(year)s" % hit["_source"])