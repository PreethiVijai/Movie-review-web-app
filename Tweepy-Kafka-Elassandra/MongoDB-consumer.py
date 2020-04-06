from pymongo import MongoClient
from confluent_kafka import Consumer, KafkaError
import json

from elasticsearch import Elasticsearch, helpers
from bson.json_util import dumps


from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / 'local.env'

load_dotenv(dotenv_path=env_path)

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

client = MongoClient("mongodb+srv://"+username+":"+password+"@cluster0-kpzsd.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client["realTime"]
tweetCol = db["tweets_test"]

# tweetCol.delete_many({})

# cursor = tweetCol.find({})
# for document in cursor:
#       print(document)
# print(tweetCol.count())

data = dumps(tweetCol.find({}))

dict_doc = json.loads(data)

doc_list = [dict_doc]

client_es = Elasticsearch("localhost:9200")

try:

      resp = helpers.bulk(client=client_es)

      # print the response returned by Elasticsearch
      print ("helpers.bulk() RESPONSE:", resp)
      print ("helpers.bulk() RESPONSE:", json.dumps(resp, indent=4))

except Exception as err:

      print("Elasticsearch helpers.bulk() ERROR:", err)


# consumer = Consumer({
#     'bootstrap.servers': 'localhost:9092',
#     'group.id': 'mygroup',
#     'default.topic.config': {
#         'auto.offset.reset': 'earliest'
#     }
# })
#
# consumer.subscribe(['test'])
# print('subscribed')
#
# while True:
#     msg = consumer.poll(1)
#
#
#
#     if msg is None:
#         print("here")
#         continue
#     if msg.error():
#         if msg.error().code() == KafkaError._PARTITION_EOF:
#             print("HEY")
#             continue
#         else:
#             print(msg.error())
#             break
#
#     msg = msg.value().decode('utf-8')
#     print(msg)
#     tweet = json.loads(msg)
#     tweetCol.insert_one(tweet)
#     print('{} added to {}'.format(tweet, tweetCol))
#
#
# consumer.close()


############## To check the content of a collection in MongoDB ################

# cursor = tweetCol.find({})
# for document in cursor:
#       print(document)
# print(tweetCol.count())
