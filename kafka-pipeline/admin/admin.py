from confluent_kafka.admin import AdminClient, NewTopic

admin_client = AdminClient({"bootstrap.servers": "localhost:9092"})

topic_list = list()
topic_list.append(NewTopic("example_topic", 1, 1))
admin_client.create_topics(topic_list)
print(admin_client.list_topics())