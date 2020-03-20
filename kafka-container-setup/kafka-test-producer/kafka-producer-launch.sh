docker build -t gcr.io/green-entity-251200/producer:v1 .
docker push gcr.io/green-entity-251200/producer:v1
#docker run --rm --network network1 -p  7070:7070 gcr.io/green-entity-251200/consume:v1
kubectl create deployment producer --image=gcr.io/green-entity-251200/producer:v1
kubectl expose deployment producer --type=LoadBalancer --port 5000 --target-port 5000