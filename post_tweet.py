import final_tweets
import credentials
import tweepy
from random import randint
from time import sleep

sleep(randint(10, 82800))

tweets = final_tweets.tweets
tweet = tweets.pop(0)

auth = tweepy.OAuthHandler(credentials.api_key, credentials.api_secret_key)
auth.set_access_token(credentials.access_token,
                      credentials.access_token_secret)

api = tweepy.API(auth)
api.update_status(tweet)


with open('final_tweets.py', 'w') as f:
    f.write(f"tweets = {tweets}")
