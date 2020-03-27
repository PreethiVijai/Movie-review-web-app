# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:32:23 2020

@author: Srihaasa
"""
from confluent_kafka import Producer
import tweepy
from dotenv import load_dotenv
from pathlib import Path
import os
import json
#import csv

consumer_key = 'cbOz7WdSq3pscOHcrCPeY4YyV'
consumer_secret = 'PhGK56KBym80X0gCBP8OuHU3BZWFrmWiAKsjJ5PncMEIBBnP0m'
access_token = '1046554892582641664-UIUnXcIgtqMgA9hZdhcURDMelfsmTN'
access_token_secret = 'nxZM3dYEVtp62IUslanUzeRCnBwNFU2NFv3Q0Nf8DoUr4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
producer = Producer({'bootstrap.servers': 'kafka:9092'})
msg = json.dumps(msg)
print(msg)
producer.produce("example_topic",msg.encode('utf-8'))
print("done")

for tweet in tweepy.Cursor(api.search,q="#JumanjiTheNextLevel #moviereview",count=10,\
                           lang="en",\
                           since_id= "2020-02-20",\
                           until="2020-03-26").items(100):
    print(tweet.created_at, tweet.text)
    tweet = json.loads(data)

        msg = {'id': tweet['id_str'], 'tweet': tweet['text'], 'tweet_coordinates': None, 'tweet_place': None, 'user_place': None}

        if tweet['coordinates']:

            msg['tweet_coordinates'] = tweet['coordinates']

        elif tweet['place']:

            # tweet['place']['full_name'].split(',')

            msg['tweet_place'] = tweet['place']['full_name']


        elif tweet['user']['location']:

            # tweet['user']['location'].split(',')

            msg['user_place'] = tweet['user']['location']

        msg = json.dumps(msg)
        print(msg)
        producer.produce("example_topic",msg.encode('utf-8'))

        print("done")
        return True
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])