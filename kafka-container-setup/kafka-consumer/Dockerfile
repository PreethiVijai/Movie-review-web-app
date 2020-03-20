FROM debian:10
COPY . /kafka-consumer
#RUN make /rest
#CMD ["python3 /rest/load-data.py"]
CMD ["/kafka-consumer/kafka-consumer-install.sh"]
#CMD python3 /rest/rest-server.py rest