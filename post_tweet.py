import final_tweets
import credentials
import tweepy

tweets = final_tweets.tweets
tweet = tweets.pop(0)

auth = tweepy.OAuthHandler(credentials.api_key, credentials.api_secret_key)
auth.set_access_token(credentials.access_token,
                      credentials.access_token_secret)

api = tweepy.API(auth)

print(tweet)
print(tweets)


# with open('final_tweets.py', 'w') as f:
#    f.write(f"tweets = {tweets}")
