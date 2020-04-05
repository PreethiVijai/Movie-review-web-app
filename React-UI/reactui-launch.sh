#!/bin/sh
#
# This is the script you need to provide to launch a reactui service
#
docker build -t gcr.io/golden-hook-269722/reactui:v1 .
docker push gcr.io/golden-hook-269722/reactui:v1
#docker run --rm --network network1 -p  7070:7070 gcr.io/green-entity-251200/rest:v1
kubectl run reactui --image=gcr.io/golden-hook-269722/reactui:v1 
kubectl expose deployment reactui --port 80 --target-port 80