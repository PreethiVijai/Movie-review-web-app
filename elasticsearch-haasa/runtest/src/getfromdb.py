#from bs4 import BeautifulSoup
from pymongo import MongoClient
#import certifi
#import urllib3
import json
import csv
import re

username = "scrumlords"
password = "Bda2020$!"

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
        print(avgsentiment) 
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

    #res = es.index(index="test-index", doc_type='tweet', id=x[u'movieId'], body=x1)
    #print("x1")
    #print(x1)
    #print("new")