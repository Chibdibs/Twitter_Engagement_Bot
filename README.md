# Twitter Engagement Bot

## Overview
This Python script serves as a modular Twitter engagement bot that automatically likes and retweets tweets with high activity based on specified keywords/topics. It utilizes the Tweepy library to interact with the Twitter API and can be configured to operate for different accounts/topics.

## Features
- Automatically likes and retweets tweets with high engagement metrics (likes and retweets).
- Modular design allows for easy configuration for different topics/accounts.
- Runs on specified days of the week (Monday, Wednesday, Friday) by default.

## How to Use
1. Clone or download the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Obtain your Twitter API credentials (consumer key, consumer secret, access token, access token secret) from the Twitter Developer Portal.
4. Replace the placeholder values in the script (`consumer_key`, `consumer_secret`, `access_token`, `access_token_secret`) with your actual API credentials.
5. Modify the `topics` list in the script to include the keywords/topics relevant to your accounts.
6. Run the script using Python: `python engagement_bot.py`.

## Configuration
- `consumer_key`: Your Twitter API consumer key.
- `consumer_secret`: Your Twitter API consumer secret.
- `access_token`: Your Twitter API access token.
- `access_token_secret`: Your Twitter API access token secret.
- `days_to_run`: List of days the bot should run (default: ['Monday', 'Wednesday', 'Friday']).
- `topics`: List of topics/keywords to search for and engage with.

## Disclaimer
Use this bot responsibly and in compliance with Twitter's developer terms of service. Be mindful of rate limits and API usage guidelines to avoid suspension of your Twitter account.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Thanks to Tweepy for providing a Python wrapper for the Twitter API.
