import json
from pymongo import MongoClient

tweets_file = open("geotagged_tweets.jsons", "r")

client = MongoClient()
db = client.uva_FODS
db.tweets.delete_many({})

for line in tweets_file:
    jsonTweet = json.loads(line)
    db.tweets.insert_one(jsonTweet)
