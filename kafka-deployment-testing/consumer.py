from kafka import KafkaConsumer
consumer = KafkaConsumer(bootstrap_servers='kafka:9092')
consumer.subscribe(['sample'])
#consumer = KafkaConsumer('sample')
for message in consumer:
    with open('test_output.txt', 'a+') as f:
        f.write(str(message) + '\n')
    print(message)
