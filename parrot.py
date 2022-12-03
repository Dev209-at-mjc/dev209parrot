import tweepy
import keys

twitter_oauth = tweepy.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
twitter_oauth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)

twitter_api = tweepy.API(twitter_oauth)
bot_id = twitter_api.verify_credentials().id
# Subclass Stream to print IDs of Tweets received
class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        print(status.id)
        if status.in_reply_to_status_id is not None or status.user.id == bot_id:
            return

        if not status.retweeted:
            try:
                tweet_to_quote_url="https://twitter.com/" + status.user.screen_name + "/status/" + str(status.id)
                twitter_api.retweet(status.id)
                print("RTed successfully")
            except Exception as e:
                print(e)
    def on_error(self, status):
        print(f"RTing error: {status}")
# Initialize instance of the subclass
printer = IDPrinter(
    keys.API_KEY, keys.API_SECRET_KEY, keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)


# Filter realtime Tweets by keyword
printer.filter(track=["#Dev209","#209Hacker"])