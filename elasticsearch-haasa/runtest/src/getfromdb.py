#from bs4 import BeautifulSoup
from pymongo import MongoClient
#import certifi
#import urllib3
import json
import csv
import re

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
abbList = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
fullList= ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]          
def getAbbreviation(loc):
    for substring in abbList:
        if(substring in loc):
            return substring
    for substring in fullList:
        if(substring in loc):
            return us_state_abbrev[substring]
    return None        



username = "scrumlords"
password = "Bda2020$!"

client = MongoClient("mongodb+srv://scrumlords:"+password+"@cluster0-4ef7e.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client["scraping"]
tweetCol = db["movies_test"]    
db1 = client["realTime"]
tweetCol1 = db1["tweets_test_1"]

for x in tweetCol.find({"movieId":"tt8946378"}):
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
        if(doc[u'user_place'] is not None):
            print(doc[u'user_place'])
            loc= doc[u'user_place'].encode('ascii', 'replace')
            loc=loc.decode("utf-8")
            Loc1=None
            Loc1= getAbbreviation(loc)
            if(Loc1 is not None):
                tweetLocations.append(Loc1)
        if(doc[u'tweet_place'] is not None):
            print(doc[u'tweet_place'])
            loc= doc[u'tweet_place'].encode('ascii', 'replace')
            Loc1=None
            Loc1= getAbbreviation(loc)
            if(Loc1 is not None):
                tweetLocations.append(Loc1)        
            
        avgsentiment+=doc[u'sentimentScore']
    print(tweetLocations)
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