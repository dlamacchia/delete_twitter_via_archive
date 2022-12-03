import tweepy
import json
import os

auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
auth.set_access_token(os.getenv('ACCESS_KEY'), os.getenv('ACCESS_SECRET'))
api = tweepy.API(auth)

# Usage:
# 1) Set your API keys in the above environment variables. You will need to apply for access at
#    developer.twitter.com to get these.
# 2) Download your twitter archive. This can take 24-48 hours (or more)
# 3) Unzip the archive, cd to the data directory where tweets.js is.
# 4) Copy tweets.js to tweets.json and fixup the first line so it's proper JSON: change "window.YTD.tweets.part0 = [" to "["
# 4) Run

f = open("tweets.json", 'r')
tweets = json.load(f)

for tweet in tweets:
    tweet_id = int(tweet["tweet"]["id"])
    try:
        api.destroy_status(tweet_id)
        print(f"Deleted tweet {tweet_id}")
    except tweepy.errors.NotFound as e:
        text = e.response.text
        print(text)
        print(f"Skipped tweet {tweet_id}")
    except tweepy.errors.Forbidden as e:
        text = e.response.text
        print(text)
        print(f"Skipped tweet {tweet_id}")


