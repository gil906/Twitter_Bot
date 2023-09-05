import tweepy
import logging
import os

# Load API credentials and reply triggers from environment variables or a configuration file
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

reply_triggers = {
    "hello": "Hello @{mention.user.screen_name}! How can I assist you today?",
    # Add more triggers and responses as needed
}

# Set up logging
logging.basicConfig(filename="twitter_bot.log", level=logging.INFO)

# Create the API object
def create_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

# Handle mentions and perform actions
def handle_mentions(api):
    try:
        mentions = api.mentions_timeline()

        for mention in mentions:
            mention_text = mention.text.lower()
            reply_text = f"Thank you for reaching out, @{mention.user.screen_name}!"

            for trigger, response in reply_triggers.items():
                if trigger in mention_text:
                    reply_text = response
                    break

            # Reply to mention
            api.update_status(
                status=reply_text,
                in_reply_to_status_id=mention.id,
            )

            # Additional actions
            api.create_favorite(mention.id)
            api.retweet(mention.id)
            api.create_friendship(mention.user.screen_name)

            logging.info(f"Replied to @{mention.user.screen_name}: {mention.text}")

    except tweepy.TweepError as e:
        logging.error(f"Error: {e}")
        print("Error: ", e)

def main():
    api = create_api()
    handle_mentions(api)

if __name__ == "__main__":
    main()
