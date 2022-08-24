from twitter import *
import os
CONSUMER_KEY = 
CONSUMER_SECRET = 
MY_TWITTER_CREDS = os.path.expanduser('')
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("dz-test_tweet", CONSUMER_KEY, CONSUMER_SECRET,
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

twitter = Twitter(auth=OAuth(
    oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

# Now work with Twitter
twitter.statuses.update(status='>.> <.<')
oauth_dance("dz-test_tweet", CONSUMER_KEY, CONSUMER_SECRET)
