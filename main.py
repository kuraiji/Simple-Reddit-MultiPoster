# Simple Reddit Multi-Poster by Kuraiji (Payman)

from reddit_quick_post import RedditHelper
from days_of_the_week import DaysOfTheWeek
import pytz
import datetime
import configparser

# Open config file
config = configparser.ConfigParser()
config.read('config.ini')

# Config Defaults
client_id = config['DEFAULT']['Client_id']
client_secret = config['DEFAULT']['Client_secret']
username = config['DEFAULT']['Username']
password = config['DEFAULT']['Password']
timezone = pytz.timezone(config['DEFAULT']['Timezone'])
weekday = DaysOfTheWeek[str.upper(config['DEFAULT']['Day_to_post'])]

# Check if today is the right day to post
current_day = DaysOfTheWeek(datetime.datetime.now(timezone).date().weekday())
if not(weekday is current_day or weekday is DaysOfTheWeek.ALL):
    quit()

# Initialize Reddit API
reddit = RedditHelper(client_id, client_secret, username, password)

# Post
for post in config.sections():
    subreddit = config[post]['Subreddit']
    title = config[post]['Title']
    with open(config[post]['Selftext'], encoding='utf8') as file:
        selftext = file.read()
    flair = config[post]['Flair']
    reddit.post(subreddit, title, selftext, flair)
