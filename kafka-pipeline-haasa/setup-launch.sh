#!/bin/sh
#
# This is the script you need to provide to launch a kafka and zookeeper services
#
kubectl create -f zookeeper-service.yaml
kubectl create -f zookeeper-deployment.yaml
kubectl create -f kafka-service.yaml
kubectl create -f kafka-deployment.yaml