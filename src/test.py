import tweepy
import os

client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
)

query = "Alzheimer -is:retweet"

# Name and path of the file where you want the Tweets written to
file_name = "./tweets.txt"

tweets = client.search_all_tweets(
    query=query, tweet_fields=["context_annotations", "created_at"], max_results=10
)

with open(file_name, "a+") as filehandle:
    for tweet in tweets:
        filehandle.write("%s\n" % tweet.id)
