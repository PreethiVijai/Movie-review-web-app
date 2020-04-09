from datetime import datetime
from elasticsearch import Elasticsearch
from pymongo import MongoClient
import re
#es = Elasticsearch()
# host - elasticsearch
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
if not es.ping():
    raise ValueError("Connection failed")
username = "scrumlords"
password = "Bda2020$!"

client = MongoClient("mongodb+srv://scrumlords:"+password+"@cluster0-4ef7e.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client["scraping"]
tweetCol = db["movies_test"]
db1 = client["realTime"]
tweetCol1 = db1["tweets_test_1"]
states = {
    "AL": ["alabama"],
    "AK": ["Alaska"],
    "AZ": ["Arizona"],
    "AR": ["Arkansas"],
    "CA": ["California"],
    "CO": ["Colorado"],
    "CT": ["Connecticut"],
    "DE": ["Delaware"],
    "FL": ["Florida"],
    "GA": ["Georgia"],
    "HI": ["Hawaii"],
    "ID": ["Idaho"],
    "IL": ["Illinois"],
    "IN": ["Indiana"],
    "IA": ["Iowa"],
    "KS": ["Kansas"],
    "KY": ["Kentucky"],
    "LA": ["Louisiana"],
    "ME": ["Maine"],
    "MD": ["Maryland"],
    "MA": ["Massachusetts"],
    "MI": ["Michigan"],
    "MN": ["Minnesota"],
    "MS": ["Mississippi"],
    "MO": ["Missouri"],
    "MT": ["Montana"],
    "NE": ["Nebraska"],
    "NV": ["Nevada"],
    "NH": ["NewHampshire", "New Hampshire"],
    "NJ": ["NewJersey", "New Jersey"],
    "NM": ["NewMexico", "New Mexico"],
    "NY": ["NewYork", "New York"],
    "NC": ["NorthCarolina", "North Carolina"],
    "ND": ["NorthDakota", "North Dakota"],
    "OH": ["Ohio"],
    "OK": ["Oklahoma"],
    "OR": ["Oregon"],
    "PA": ["Pennsylvania"],
    "RI": ["RhodeIsland", "Rhode Island"],
    "SC": ["South Carolina", "SountCarolina"],
    "SD": ["South Dakota", "SouthDakota"],
    "TN": ["Tennessee"],
    "TX": ["Texas"],
    "UT": ["Utah"],
    "VT": ["Vermont"],
    "VA": ["virginia"],
    "WA": ["Washington"],
    "WV": ["West Virginia", "WestVirginia"],
    "WI": ["Wisconsin"],
    "WY": ["Wyoming"],
  }
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
    # filtering tweetLocations - so it contains only state abbreviations. - testing / crude filtering.
    TL = set()
    for elem in x1['tweetLocations']:
        if elem is not None:
            for state in states.keys():
                state1 = state.lower()
                elem1 = elem.lower()
                if re.search(state1, elem1):
                    TL.add(state)
                else:
                    for syn in states[state]:
                        if re.search(state1, elem1):
                            TL.add(state)
    x1['tweetLocations'] = list(TL)

    res = es.index(index="test-index", doc_type='tweet', id=movieId, body=x1)
    print(x1)
    print(res)

#res = es.get(index="test-index", doc_type='tweet', id=1)
#print(res)
