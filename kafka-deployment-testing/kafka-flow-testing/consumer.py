import pymongo
from kafka import KafkaConsumer
consumer = KafkaConsumer(bootstrap_servers='kafka:9092')
consumer.subscribe(['sample'])

# create database ("mydatabase")
myclient = pymongo.MongoClient("<MONGODB-ATLAS-CONNECTION-STRING>")
mydb = myclient["mydatabase"]
# create collection
mycol = mydb["tweets"]

for message in consumer:

    # Insert documents - one at a time.

    mydict = {"tweet": message}
    mycol.insert_one(mydict)
