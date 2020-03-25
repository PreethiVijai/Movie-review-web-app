#!/bin/sh
#
# This is the script you need to provide to launch a consumer service
#
docker build -t gcr.io/golden-hook-269722/test1:v1 .
docker push gcr.io/golden-hook-269722/test1:v1
#docker run --rm --network network1 -p  7070:7070 gcr.io/green-entity-251200/rest:v1
kubectl create deployment test1 --image=gcr.io/golden-hook-269722/test1:v1
kubectl expose deployment test1 --port 80 --target-port 80