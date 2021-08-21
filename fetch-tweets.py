from datetime import datetime
import tweepy
import json
import time
import codecs
import re

with open('tweet-meta.json') as meta_file:
    meta = json.loads(meta_file.read())

meta_file.close()
num_tweets = meta[0]['tweets-recorded']
newest_id = meta[0]['max-id-checked']
tweet_ids = []
id_file = open('user_ids.txt', 'r')
all_user_ids = id_file.readlines()
id_file.close()

# def limit_handled(cursor):
#     checks = True
#     while checks:
#         try:
#             yield next(cursor)
#         except tweepy.RateLimitError:
#             print("Rate Limit Error")
#             time.sleep(15 * 60)
#         except StopIteration:
#             print("Next ID")
#             checks = False

with open('credentials.json') as cred_file:
    creds = json.loads(cred_file.read())
cred_file.close()

auth = tweepy.OAuthHandler(creds['twitter'][0]['api_key'],creds['twitter'][0]['api_secret'])
auth.set_access_token(creds['twitter'][0]['access_token'],creds['twitter'][0]['access_secret'])
api = tweepy.API(auth)

tweet_file = open('tweet_file.txt', mode = 'a', encoding = 'utf-8')

for current_id in all_user_ids:
    try:
        timeline = api.user_timeline(user_id = str(current_id), include_rts = False,count=3200, since_id = newest_id)
        for tweet in timeline:
            tweet_file.write(re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', re.sub('\n', ' ', tweet.text)) + '\n')
            num_tweets += 1
            print(tweet.id)
            tweet_ids.append(tweet.id)
    except tweepy.RateLimitError:
        print("Rate Limit Error")
        time.sleep(15 * 60)
    except tweepy.TweepError:
        print("pvt account")

tweet_file.close()
meta[0]['tweets-recorded'] = num_tweets
meta[0]['max-id-checked'] = max(tweet_ids)
with open("tweet-meta.json", "w") as meta_write:
    json.dump(meta, meta_write)
meta_write.close()
