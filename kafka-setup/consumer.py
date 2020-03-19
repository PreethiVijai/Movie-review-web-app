from kafka import KafkaConsumer
#consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
#consumer.subscribe(['sample'])
consumer = KafkaConsumer('sample')
for message in consumer:
    print(message)
