docker build -t gcr.io/green-entity-251200/consumer:v1 .
docker push gcr.io/green-entity-251200/consumer:v1
#docker run --rm --network network1 -p  7070:7070 gcr.io/green-entity-251200/consumer:v1
kubectl create deployment consumer  --image=gcr.io/green-entity-251200/consumer:v1
kubectl expose deployment consumer --type=LoadBalancer --port 5000 --target-port 5000