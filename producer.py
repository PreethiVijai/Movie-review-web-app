from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='172.40.0.6:9092')
producer.send('sample', b'Hello, World!')
producer.send('sample', key=b'message-two', value=b'This is Kafka-Python')
producer.flush()
