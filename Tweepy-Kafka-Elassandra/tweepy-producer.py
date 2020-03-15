from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from confluent_kafka import Producer
from tweepy import API

from dotenv import load_dotenv
from pathlib import Path
import os


class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.produce("test", data.encode('utf-8'))
        print(data)
        return True
    def on_error(self, status):
        print(status)

env_path = Path('.') / 'local.env'

load_dotenv(dotenv_path=env_path)

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


producer = Producer({'bootstrap.servers': 'localhost:9092'})
listener = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth, wait_on_rate_limit=True,
          wait_on_rate_limit_notify=True)
stream = Stream(auth, listener)
stream.filter(track=['#coronapocalypse'])
