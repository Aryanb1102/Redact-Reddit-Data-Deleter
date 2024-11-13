
# Redact - Reddit Data Deleter Tool

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![GitHub stars](https://img.shields.io/github/stars/yourusername/Redact-Reddit-Data-Deleter?style=social)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

**Redact** is a powerful and user-friendly tool designed to help Reddit users manage their online presence by allowing them to selectively delete their posts and comments. In an age where data privacy is paramount, Redact empowers users to take control of their digital footprint with ease and efficiency.

## Features

- **Bulk Deletion**: Remove all your Reddit posts and comments in bulk with just a few clicks.
- **Selective Deletion**: Choose specific posts or comments to delete based on your preferences.
- **User-Friendly Interface**: Intuitive design ensures a seamless user experience.
- **Secure Authentication**: Utilizes Reddit's API securely to authenticate and perform deletions.
- **Rate Limit Handling**: Automatically manages Reddit API rate limits to prevent interruptions.
- **Logging**: Keeps a log of deleted items for your reference.


## Installation

Redact is built with Python and utilizes the PRAW (Python Reddit API Wrapper) library to interact with Reddit's API. Follow the steps below to set up Redact on your local machine.

### Prerequisites

- Python 3.8 or higher
- GitHub account (for cloning the repository)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Redact-Reddit-Data-Deleter.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd Redact-Reddit-Data-Deleter
   ```

3. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Required Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Reddit API Credentials**

   - Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps) and create a new application.
   - Choose the **script** type.
   - Note down the **Client ID**, **Client Secret**, **Username**, and **Password**.

6. **Configure the Application**

   - Rename `config.example.py` to `config.py`.

     ```bash
     mv config.example.py config.py
     ```

   - Open `config.py` and enter your Reddit API credentials:

     ```python
     client_id = 'YOUR_CLIENT_ID'
     client_secret = 'YOUR_CLIENT_SECRET'
     username = 'YOUR_USERNAME'
     password = 'YOUR_PASSWORD'
     user_agent = 'Redact Data Deleter (by u/YOUR_USERNAME)'
     ```

## Usage

1. **Run the Script**

   ```bash
   python reddit_data_deleter.py
   ```

2. **Select Actions**

   - **Delete All Posts**: Remove all your Reddit posts.
   - **Delete All Comments**: Remove all your Reddit comments.
   - **Selective Deletion**: Choose specific posts or comments to delete.

3. **Monitor Progress**

   The script will display the status of deletions in the terminal. Logs are maintained in `deletion_log.txt` for your reference.

## Technologies Used

- **Python 3.8+**
- **PRAW (Python Reddit API Wrapper)**
- **GitHub** for version control and collaboration

## Contributing

Contributions are welcome! If you have suggestions or improvements, please follow the steps below:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add Your Feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

Please ensure your code follows the project's coding standards and includes relevant tests.


