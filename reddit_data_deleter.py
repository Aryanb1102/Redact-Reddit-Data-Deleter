import praw
import requests
from requests.auth import HTTPBasicAuth
import urllib.parse
import time
import hashlib
import os
from cryptography.fernet import Fernet

# Constants for Reddit API
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'YOUR_REDIRECT_URI'  # e.g., 'http://localhost:8080'
OAUTH_URL = 'https://www.reddit.com/api/v1/authorize'
TOKEN_URL = 'https://www.reddit.com/api/v1/access_token'
SCOPE = 'identity edit history read'

# Function to generate a secure state parameter
def generate_state():
    return hashlib.sha256(os.urandom(1024)).hexdigest()

# Function to encrypt the access token
def encrypt_token(token, key):
    f = Fernet(key)
    return f.encrypt(token.encode())

# Function to decrypt the access token
def decrypt_token(token_encrypted, key):
    f = Fernet(key)
    return f.decrypt(token_encrypted).decode()

# Main function
def main():
    # Generate encryption key
    key = Fernet.generate_key()

    # Generate a secure state
    state = generate_state()

    # Step 1: Direct user to Reddit for authorization
    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'state': state,
        'redirect_uri': REDIRECT_URI,
        'duration': 'temporary',
        'scope': SCOPE
    }
    auth_url = f"{OAUTH_URL}?{urllib.parse.urlencode(params)}"
    print("Please go to this URL and authorize access:")
    print(auth_url)

    # Step 2: Receive the authorization code from the redirected URL
    redirect_response = input('Paste the full redirect URL here:\n')
    parsed_url = urllib.parse.urlparse(redirect_response)
    code = urllib.parse.parse_qs(parsed_url.query).get('code')
    received_state = urllib.parse.parse_qs(parsed_url.query).get('state')

    # Validate state parameter to prevent CSRF attacks
    if received_state[0] != state:
        print("Error: State mismatch. Potential CSRF attack.")
        return

    # Step 3: Exchange authorization code for access token
    auth = HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    data = {
        'grant_type': 'authorization_code',
        'code': code[0],
        'redirect_uri': REDIRECT_URI
    }
    headers = {'User-Agent': 'RedactRedditDataDeleter/0.1 by YourUsername'}
    response = requests.post(TOKEN_URL, auth=auth, data=data, headers=headers)
    if response.status_code != 200:
        print("Error fetching access token.")
        return
    token_info = response.json()
    access_token = token_info['access_token']

    # Encrypt the access token for secure storage
    encrypted_token = encrypt_token(access_token, key)

    # Decrypt the token when needed
    access_token = decrypt_token(encrypted_token, key)

    # Initialize PRAW with the access token
    reddit = praw.Reddit(client_id=CLIENT_ID,
                         client_secret=CLIENT_SECRET,
                         user_agent='RedactRedditDataDeleter/0.1 by YourUsername',
                         refresh_token=None,
                         token=access_token)

    # Confirm user's identity
    try:
        user = reddit.user.me()
        print(f"Authenticated as {user.name}")
    except Exception as e:
        print("Authentication failed:", e)
        return

    # Ask user what to delete
    choice = input("What would you like to delete? (posts/comments/both): ").lower()
    if choice not in ['posts', 'comments', 'both']:
        print("Invalid choice.")
        return

    # Input validation for time filter (e.g., delete from last 'n' days)
    try:
        days = int(input("Delete items from how many days ago? (Enter 0 for all): "))
    except ValueError:
        print("Invalid number.")
        return
    current_time = time.time()

    # Error handling and deletion process
    try:
        if choice in ['posts', 'both']:
            print("Deleting posts...")
            for submission in reddit.redditor(user.name).submissions.new(limit=None):
                created_time = submission.created_utc
                if days == 0 or (current_time - created_time) <= days * 86400:
                    submission.delete()
                    time.sleep(2)  # Respect Reddit API rate limits
            print("Posts deletion completed.")

        if choice in ['comments', 'both']:
            print("Deleting comments...")
            for comment in reddit.redditor(user.name).comments.new(limit=None):
                created_time = comment.created_utc
                if days == 0 or (current_time - created_time) <= days * 86400:
                    comment.delete()
                    time.sleep(2)  # Respect Reddit API rate limits
            print("Comments deletion completed.")
    except Exception as e:
        print("An error occurred during deletion:", e)
        return

    print("Data deletion process completed successfully.")

if __name__ == "__main__":
    main()
