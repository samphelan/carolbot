with open('generatedtweets6.txt', 'r') as tweets:

    for text in tweets:
        tweet_list = text.split('<|endoftext|>')

        for tweet in tweet_list:
            print(tweet)
