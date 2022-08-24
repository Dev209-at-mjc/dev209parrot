import tweepy as twitter
import keys
import time, datetime

twitter_oauth = twitter.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
twitter_oauth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)

twitter_api = twitter.API(twitter_oauth)
bot_id = twitter_api.verify_credentials().id

try:
    twitter_api.verify_credentials()
    print("Logged in")
except tweepy.TweepError as e:
    print(e)
except Exception as e:
    print(e)

# create stream
class StreamListener(twitter.StreamListener):
  def on_status(self, status):
    if status.in_reply_to_status_id is not None or status.user.id == bot_id:
      return

    if not status.retweeted:
      try:
        tweet_to_quote_url="https://twitter.com/" + status.user.screen_name + "/status/" + str(status.id)
        twitter_api.retweet(status.id)
        #twitter_api.update_status("yes", attachment_url=tweet_to_quote_url)
        print("RTed successfully")
      except Exception as e:
        print(e)

  def on_error(self, status):
    print(f"RTing error: {status}")

tweets_listener = StreamListener(twitter_api)
tweet_stream = twitter.Stream(twitter_api.auth, tweets_listener)
tweet_stream.filter(track=["#Dev209", "209Hackers"])
