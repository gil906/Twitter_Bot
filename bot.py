import tweepy

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Create the API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define the function to handle mentions
def reply_to_mentions():
    mentions = api.mentions_timeline()
    for mention in mentions:
        # Customize the replies based on different triggers
        if "hello" in mention.text.lower():
            reply_text = f"Hello @{mention.user.screen_name}! How can I assist you today?"
        elif "help" in mention.text.lower():
            reply_text = f"Sure, I'm here to help! Please let me know what you need assistance with."
        else:
            reply_text = f"Thank you for reaching out, @{mention.user.screen_name}!"
        
        # Reply to the mention
        api.update_status(
            status=reply_text,
            in_reply_to_status_id=mention.id
        )
        print(f"Replied to mention from @{mention.user.screen_name}")

# Run the bot
reply_to_mentions()

