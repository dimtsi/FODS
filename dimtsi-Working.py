
import numpy as np
import pandas as pd
import json
from pymongo import MongoClient

tweets_data = []
tweets_file = open("tweetsamples.jsons", "r")

client = MongoClient()
db = client.uva_FODS

print(db)
for line in tweets_file:
    jsonTweet = json.loads(line)
    tweets_data.append(jsonTweet)

tweet_df = pd.DataFrame(tweets_data)
tweet_short = tweet_df.loc[:,['created_at','place', 'text', 'in_reply_to_screen_name', 'user']]

# print(tweet_short.head())
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer

db = client.test_database

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002, 2003],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

frame = pd.DataFrame(data)

print(tweet_df.describe())
