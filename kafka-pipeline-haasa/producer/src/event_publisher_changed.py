# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:32:23 2020

@author: Srihaasa
"""
from confluent_kafka import Producer
import tweepy
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path
import os
import json
#import csv

username = ""
password = ""

client = MongoClient("mongodb+srv://scrumlords:"+password+"@cluster0-4ef7e.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client["scraping"]
tweetCol = db["movies_test"]    
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,
          wait_on_rate_limit_notify=True)
producer = Producer({'bootstrap.servers': 'kafka:9092'})
for x in tweetCol.find({},{ "_id": 0 }):
    tname= x[u'name']
    movieId=x[u'movieId']
    tname = tname.replace(":", "")
    tname = tname.replace(" ", "")
    tname = tname.replace(".", "")
    tname = tname.replace("-", "")
    tname = tname.replace(",", "")
    tname = tname.replace("'", "")
    for tweet in tweepy.Cursor(api.search, q=tname+" "+"#moviereview", count=10,\
                               lang="en",\
                               since_id="2020-02-20",\
                               until="2020-03-27").items(10):
        msg = {'id': tweet.id_str,'movieId':movieId, 'movieName':tname,'tweet': tweet.text, 'tweet_coordinates': None,'tweet_place': None, 'user_place': None}

        if tweet.coordinates:

            msg['tweet_coordinates'] = tweet.coordinates
        elif tweet.place:

            # tweet['place']['full_name'].split(',')

            msg['tweet_place'] = tweet.place.full_name


        elif tweet.user.location:

            # tweet['user']['location'].split(',')

            msg['user_place'] = tweet.user.location

        msg = json.dumps(msg)
        print(msg)
        producer.produce("example_topic",msg.encode('utf-8'))
        print("done")