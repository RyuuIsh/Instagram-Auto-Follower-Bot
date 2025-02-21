# 📷 Instagram-Auto-Follower-Bot
A Python bot that automatically follows Instagram users from a selected account's follower list using Selenium.

## Features
- Automates Following – Follows users from a specific Instagram account.
- Handles Popups – Bypasses cookie prompts, login save, and notifications.
- Secure Credentials – Uses .env for authentication.
- Auto Scrolls Followers List – Loads more users dynamically.
- Error Handling – Skips accounts that are already followed.

## Tech-Stack
- Python – Core programming language
- Selenium – Automating browser actions
- dotenv – Storing credentials securely

## Setup-Instructions
### Clone the Repository
```
git clone https://github.com/yourusername/Insta-Follower-Bot.git
cd Insta-Follower-Bot
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Setup Environment Variables
Create a `.env` file and add:
```
INSTA_USERNAME=your_instagram_email
INSTA_PASSWORD=your_instagram_password
```
### Run the Script
```
python main.py
```

## Future Enhancements
- Unfollow Inactive Users 
- Auto CAPTCHA Handling 
- Follow Limits to Avoid Bans 

💙 Follow users faster and smarter with automation! 🚀
