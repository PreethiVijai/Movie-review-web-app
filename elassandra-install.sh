docker pull strapdata/elassandra
docker run --name my-elassandra strapdata/elassandra
docker run -it --link my-elassandra --rm strapdata/elassandra cqlsh my-elassandra
docker run -it --link my-elassandra --rm strapdata/elassandra curl my-elassandra:9200
docker exec -it my-elassandra nodetool status