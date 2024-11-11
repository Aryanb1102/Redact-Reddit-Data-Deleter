import praw
import time

# Reddit API credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
user_agent = 'Redact Data Deleter (by u/your_username)'

# Initialize Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

# Function to delete all posts
def delete_posts():
    user = reddit.user.me()
    print("Deleting posts for:", user.name)
    
    # Get user's posts and delete them
    for submission in user.submissions.new(limit=None):
        print(f"Deleting post: {submission.title}")
        submission.delete()
        time.sleep(2)  # Add delay to avoid Reddit rate limits

# Function to delete all comments
def delete_comments():
    user = reddit.user.me()
    print("Deleting comments for:", user.name)
    
    # Get user's comments and delete them
    for comment in user.comments.new(limit=None):
        print(f"Deleting comment in {comment.subreddit}: {comment.body[:30]}...")
        comment.delete()
        time.sleep(2)  # Add delay to avoid Reddit rate limits

# Main function
if __name__ == "__main__":
    delete_posts()  # Uncomment to delete posts
    delete_comments()  # Uncomment to delete comments
    print("Deletion process completed.")
