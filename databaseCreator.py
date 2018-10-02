import json
from pymongo import MongoClient

def write_df_to_mongoDB(  my_df,\
                          database_name = 'uva_FODS' ,\
                          collection_name = 'tweetsClean',
                          server = 'localhost',\
                          mongodb_port = 27017,\
                          chunk_size = 100):

    client = MongoClient('localhost',int(mongodb_port))
    db = client[database_name]
    collection = db[collection_name]
    # To write
    collection.delete_many({})  # Destroy the collection
    #aux_df=aux_df.drop_duplicates(subset=None, keep='last') # To avoid repetitions
    my_list = my_df.to_dict('records')
    l =  len(my_list)
    ran = range(l)
    steps=ran[chunk_size::chunk_size]
    steps.extend([l])

    # Inser chunks of the dataframe
    i = 0
    for j in steps:
        collection.insert_many(my_list[i:j]) # fill de collection
        i = j

    print('Done')
    return


def create_full_database():
    tweets_file = open("geotagged_tweets.jsons", "r")
    
    client = MongoClient()
    db = client.uva_FODS
    db.tweets.delete_many({})
    
    for line in tweets_file:
        jsonTweet = json.loads(line)
        db.tweets.insert_one(jsonTweet)
        

