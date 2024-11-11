# Redact - Reddit Data Deleter Tool

A simple tool to help users delete their Reddit posts and comments efficiently, ensuring control over their online presence and data privacy.

## Features
- **Selective Deletion**: Choose to delete only posts, only comments, or both.
- **Rate Limit Handling**: Includes built-in delays to comply with Reddit's API rate limits.
- **User-Friendly**: Designed to provide easy control over your Reddit history without hassle.

## Requirements
- **Python 3.x**
- **PRAW** (Python Reddit API Wrapper)

- Setup
Create a Reddit Application:
Go to Reddit App Preferences.
Create a new app to get the Client ID and Client Secret.
Configure the Script:
In the script file, replace the placeholders with your Reddit credentials:
python
Copy code
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
username = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
Usage
Run the script from the command line:
bash
Copy code
python reddit_data_deleter.py



Install PRAW by running:
```bash
pip install praw



