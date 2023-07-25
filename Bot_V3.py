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

# Define the function to handle mentions and interactions
def reply_to_mentions_and_interact():
    mentions = api.mentions_timeline()
    
    # Batch processing for interactions
    interactions = []
    
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
        
        # Add mention to interactions list
        interactions.append({
            'mention_id': mention.id,
            'reply_text': reply_text,
            'user_screen_name': mention.user.screen_name
        })

        # Favorite the mention
        api.create_favorite(mention.id)

    # Perform batch interactions
    for interaction in interactions:
        try:
            # Reply to the mention
            api.update_status(
                status=interaction['reply_text'],
                in_reply_to_status_id=interaction['mention_id']
            )
            print(f"Replied to mention from @{interaction['user_screen_name']}")

            # Retweet the mention
            api.retweet(interaction['mention_id'])
            print(f"Retweeted mention from @{interaction['user_screen_name']}")
            
            # Follow the user who mentioned the bot
            api.create_friendship(interaction['user_screen_name'])
            print(f"Followed user: @{interaction['user_screen_name']}")
            
        except tweepy.TweepError as e:
            print(f"Error occurred: {e}")
            continue


# Run the bot
reply_to_mentions_and_interact()
