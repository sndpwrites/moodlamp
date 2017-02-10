import tweepy
from datetime import datetime, timedelta
import pandas as pd

consumerKey = "YM4cbxv89HAclK3fUeSPgxQ0b"
consumerSecret = "a2kwcocBz8N8frZoxaXpTcpyRejVMOeFPW2NjZBDRs6Z1gKTez"
accessKey = "3257650580-WJmnmepmOIDozL6GNCFqpxOFniJOoFYXpdHupls"
accessSecret = "rOWRXrSEWuZfoPmJfTCNrQNNqtDDhu5tD4xhr5YI3cCwL"


def getTweets(username, max = 200):

	auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
	auth.set_access_token(accessKey, accessSecret)
	api = tweepy.API(auth)
	

	allExtractedTweets = []
	

	extractedTweets = api.user_timeline(screen_name = username,count=max)
	

	allExtractedTweets.extend(extractedTweets)

	timeFrame = datetime.today()-timedelta(7)
	timeFramedTweets = []
	media = []

	for tweet in allExtractedTweets:
		if (tweet.created_at >= timeFrame):
			if not(tweet.in_reply_to_user_id):
			        date=pd.to_datetime(tweet.created_at)
				if 'media' in tweet.entities:
					for image in tweet.entities['media']:
					      
					        
						timeFramedTweets.append([tweet.text, date.value/1000000000,image['media_url']])
				else:
						timeFramedTweets.append([tweet.text, date.value/1000000000,''])
                
	return timeFramedTweets;


