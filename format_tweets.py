import csv
csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)

with open('caroltweets2.csv') as tweets:
    reader = csv.reader(tweets, dialect='piper')
    with open('caroltweets2.txt', 'w') as text_tweets:
        for row in reader:
            text_tweets.write("<|startoftext|>" + row[0] + "<|endoftext|>")
