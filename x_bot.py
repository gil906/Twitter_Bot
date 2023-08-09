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

# Define reply triggers and messages
reply_triggers = {
    "hello": "Hello @{mention.user.screen_name}! How can I assist you today?",
    "hi": "Hello @{mention.user.screen_name}! How can I assist you today?",
    "help": "Sure, I'm here to help! Please let me know what you need assistance with.",
    "support": "Sure, I'm here to help! Please let me know what you need assistance with.",
    "thanks": "You're welcome, @{mention.user.screen_name}! If you have any more questions, feel free to ask.",
    "thank you": "You're welcome, @{mention.user.screen_name}! If you have any more questions, feel free to ask."
}

# Define the function to handle mentions
def reply_to_mentions():
    mentions = api.mentions_timeline()
    
    # Prepare reply actions
    reply_actions = []
    
    for mention in mentions:
        mention_text = mention.text.lower()
        reply_text = f"Thank you for reaching out, @{mention.user.screen_name}!"
        
        for trigger, response in reply_triggers.items():
            if trigger in mention_text:
                reply_text = response
                break
        
        reply_actions.append({
            'mention_id': mention.id,
            'reply_text': reply_text,
            'user_screen_name': mention.user.screen_name
        })
    
    # Prepare bulk reply data
    reply_data = {
        action['mention_id']: action['reply_text'] for action in reply_actions
    }
    
    # Perform bulk actions
    try:
        # Bulk reply to mentions
        api.update_statuses(status=reply_data)
        print(f"Replied to mentions")

        # Get mention IDs for other actions
        mention_ids = [action['mention_id'] for action in reply_actions]

        # Bulk retweet and like
        api.retweet(mention_ids)
        api.create_favorite(mention_ids)

        # Bulk follow
        for user_screen_name in set(action['user_screen_name'] for action in reply_actions):
            api.create_friendship(user_screen_name)
            print(f"Followed user: @{user_screen_name}")

    except tweepy.TweepError as e:
        print(f"Error occurred: {e}")

# Run the bot
reply_to_mentions()
