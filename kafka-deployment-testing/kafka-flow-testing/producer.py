import tweepy
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='kafka:9092')

CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_TOKEN=""
ACCESS_TOKEN_SECRET=""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    
        def on_status(self, status):
            producer.send('sample', str.encode(status.text))
            producer.flush()
                                    
        def on_error(self, status_code):
            if status_code == 420:
            # returning False in on_error disconnects the stream
	    # returning non-False reconnects the stream, with back off.
                return False                                                                         
                                                                                    
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
                                                                            
myStream.filter(track=['movie'])
