import credentials
import tweepy
import csv
import codecs

auth = tweepy.OAuthHandler(credentials.api_key, credentials.api_secret_key)
auth.set_access_token(credentials.access_token,
                      credentials.access_token_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()

carol = api.get_user('trashbagstern')
carol_timeline = api.user_timeline('trashbagstern', count=1000, page=6)


def deEmojify(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')


with open('caroltweets.csv', 'a') as f:
    writer = csv.writer(f, delimiter='|')
    for tweet in carol_timeline:
        if(tweet.is_quote_status == False and tweet.in_reply_to_status_id == None and tweet.text[0:2] != 'RT'):
            print(tweet.text)
            f.write(deEmojify(tweet.text + '\n'))
