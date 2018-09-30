import numpy as np
import pandas as pd
import json
from pymongo import MongoClient

client = MongoClient()
db = client.uva_FODS

tweetsdb = db.tweets

# tweet_df = pd.DataFrame(tweets_data)
# tweet_short = tweet_df.loc[:,['created_at','place', 'text', 'in_reply_to_screen_name', 'user']]

filter_query = {
    "$and":[ {"place.country_code":"US"}, { "lang": "en" } ]
    }
#we are keeping only our fields of interest
columns_query = {
    'text':1,
    'entities.hashtags':1,
    'entities.user_mentions':1,
    'place.full_name':1,
    'place.bounding_box':1
}
tweets = pd.DataFrame(list(tweetsdb.find(
    filter_query,
    columns_query
    )))#.limit()

pd.set_option('display.max_colwidth', -1)
tweets.entities.iloc[4]

# print(tweet_short.head())
# from nltk.corpus import stopwords
# from nltk.tokenize import WordPunctTokenizer

# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
# 'year': [2000, 2001, 2002, 2001, 2002, 2003],
# 'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
#
# frame = pd.DataFrame(data)
