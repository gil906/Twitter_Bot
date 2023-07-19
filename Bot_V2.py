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
        # Get the mention text in lowercase
        mention_text = mention.text.lower()
        
        # Default reply message
        reply_text = f"Thank you for reaching out, @{mention.user.screen_name}!"
        
        # Customize the replies based on different triggers
        if "hello" in mention_text or "hi" in mention_text:
            reply_text = f"Hello @{mention.user.screen_name}! How can I assist you today?"
        elif "help" in mention_text or "support" in mention_text:
            reply_text = f"Sure, I'm here to help! Please let me know what you need assistance with."
        elif "thanks" in mention_text or "thank you" in mention_text:
            reply_text = f"You're welcome, @{mention.user.screen_name}! If you have any more questions, feel free to ask."
        
        # Reply to the mention
        try:
            api.update_status(
                status=reply_text,
                in_reply_to_status_id=mention.id
            )
            print(f"Replied to mention from @{mention.user.screen_name}")

            # Retweet and like the mention
            api.retweet(mention.id)
            api.create_favorite(mention.id)

            # Follow the user who mentioned the bot
            api.create_friendship(mention.user.screen_name)
            print(f"Followed user: @{mention.user.screen_name}")
            
        except tweepy.TweepError as e:
            print(f"Error occurred: {e}")
            continue

# Run the bot
reply_to_mentions()
          
