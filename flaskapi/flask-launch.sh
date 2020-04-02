#!/bin/sh
#
# This is the script you need to provide to launch a producer service
#
docker build -t gcr.io/golden-hook-269722/flaskapi:v1 .
docker push gcr.io/golden-hook-269722/flaskapi:v1
#docker run --rm --network network1 -p  7070:7070 gcr.io/green-entity-251200/rest:v1
kubectl create deployment flaskapi --image=gcr.io/golden-hook-269722/flaskapi:v1 
kubectl expose deployment flaskapi --type=LoadBalancer --port 8080 --target-port 8080