#!/bin/sh
#
# This is the script you need to provide to launch a consumer service
#
docker build -t gcr.io/golden-hook-269722/consumer:v1 .
docker push gcr.io/golden-hook-269722/consumer:v1
#docker run --rm --network network1 -p  7070:7070 gcr.io/green-entity-251200/rest:v1
kubectl create deployment consumer --image=gcr.io/golden-hook-269722/consumer:v1
kubectl expose deployment consumer --port 80 --target-port 80