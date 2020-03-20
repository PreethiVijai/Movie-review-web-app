#!/bin/sh
#
# This is the script you need to provide to launch a rabbitmq instance
# service
#
docker run -d --name ims-zookeeper --network network1 wurstmeister/zookeeper
docker run -d  --expose 9092  --name ims-kafka --network network1 -e KAFKA_ZOOKEEPER_CONNECT=ims-zookeeper:2181 -e KAFKA_ADVERTISED_HOST_NAME=ims-kafka -e KAFKA_ADVERTISED_PORT=9092 -e KAFKA_CREATE_TOPICS=imslog:1:1 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 wurstmeister/kafka

kubectl create deployment ims-zookeeper  --image=wurstmeister/zookeeper
kubectl expose deployment ims-zookeeper  --port 2181 --target-port 2181
kubectl create deployment ims-kafka k --image=wurstmeister/kafka
kubectl expose deployment ims-kafka  --port 9092 --target-port 9092