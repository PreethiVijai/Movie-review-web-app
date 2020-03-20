#!/bin/sh
#
# This is the script you need to provide to install the rest-server.py and start it running.
# It will be provided to the instance using redis-launch.sh
#
apt-get update
apt install -y python-pip
#apt-get install -y python python-pip 

#cd ~/.
#git clone https://github.com/pallets/flask
#cd ~/flask/examples/tutorial
#sudo python3 setup.py install
pip install kafka-python==2.0.1

#export FLASK_APP=flaskr
#flask init-db
#nohup flask run -h 0.0.0.0 &
#cd ~/.
#gsutil cp gs://bucket1h/rest-server.py rest-server.py
echo done

python -u /kafka-consumer/kafka-consumer.py