#!/bin/bash
docker build -t gcr.io/<PROJECT_ID>/consumer:v1 -f Dockerfile_consumer .
docker build -t gcr.io/<PROJECT_ID>/producer:v1 -f Dockerfile_producer .
docker push gcr.io/<PROJECT_ID>/consumer:v1
docker push gcr.io/<PROJECT_ID>/producer:v1
curl -L https://github.com/kubernetes/kompose/releases/download/v1.21.0/kompose-linux-amd64 -o kompose
chmod +x kompose
sudo mv ./kompose /usr/local/bin/kompose
gcloud container clusters create cluster-1 --zone=us-central1-a --num-nodes=2
kompose convert
kubectl create -f zookeeper-deployment.yaml,zookeeper-service.yaml,kafka-deployment.yaml,kafka-service.yaml,consumer-deployment.yaml,consumer-service.yaml,producer-deployment.yaml,producer-service.yaml
