import tweepy
import time
from datetime import datetime

# Twitter API credentials
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# Function to like and retweet tweets with high activity based on the given keyword
def like_and_retweet(keyword):
    count = 10
    tweets = api.search(q=keyword, count=count, lang="en")

    for tweet in tweets:
        try:
            # Filter tweets based on their engagement metrics
            if tweet.favorite_count > 1000 and tweet.retweet_count > 500:
                # Like the tweet
                api.create_favorite(tweet.id)
                # Retweet the tweet
                api.retweet(tweet.id)
                print("Liked and retweeted:", tweet.text)
        except tweepy.TweepError as e:
            print(e.reason)


# Set the days to run the bot
days_to_run = ['Monday', 'Wednesday', 'Friday']

# Example topics/accounts
topics = ['habit tracking', 'another_topic', 'yet_another_topic']

while True:
    current_day = datetime.now().strftime("%A")
    if current_day in days_to_run:
        for topic in topics:
            like_and_retweet(topic)
    time.sleep(86400)  # Sleep for 24 hours
