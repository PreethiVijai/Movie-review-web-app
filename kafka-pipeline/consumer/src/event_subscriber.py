from pymongo import MongoClient
from confluent_kafka import Consumer, KafkaError
import json

from dotenv import load_dotenv
from pathlib import Path
import os

# env_path = Path('.') / 'src/local.env'
#
# load_dotenv(dotenv_path=env_path)
#
# username = os.getenv("USERNAME")
# password = os.getenv("PASSWORD")

username = ""
password = ""

client = MongoClient("mongodb+srv://"+username+":"+password+"@cluster0-kpzsd.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client["realTime"]
tweetCol = db["tweets_test"]

consumer = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'mygroup',
    'default.topic.config': {
        'auto.offset.reset': 'latest'
    }
})



consumer.subscribe(['example_topic'])
print('subscribed')

while True:
    msg = consumer.poll(1)
    print("here")


    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    msg = msg.value().decode('utf-8')
    tweet = json.loads(msg)
    tweetCol.insert_one(tweet)
    print('{} added to {}'.format(tweet, tweetCol))


consumer.close()


############## To check the content of a collection in MongoDB ################

# cursor = tweetCol.find({})
# for document in cursor:
#       print(document)
# print(tweetCol.count())
