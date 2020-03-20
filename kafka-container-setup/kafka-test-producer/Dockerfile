FROM debian:10
COPY . /rest
#RUN make /rest
#CMD ["python3 /rest/load-data.py"]
CMD ["/rest/kafkaproducer-install.sh"]
#CMD python3 /rest/rest-server.py rest