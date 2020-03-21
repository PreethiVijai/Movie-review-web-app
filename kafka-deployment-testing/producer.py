from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='kafka:9092')
while True:
    producer.send('sample', b'Hello, World!')
    producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
    producer.flush()
