from confluent_kafka import Consumer, KafkaError


consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'default.topic.config': {
        'auto.offset.reset': 'latest'
    }
})

consumer.subscribe(['test'])
print('subscribed')

while True:
    msg = consumer.poll(1)
    print("here")

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print("HEY")
            continue
        else:
            print(msg.error())
            break

    print('Received message: {}'.format(msg.value().decode('utf-8')))

consumer.close()