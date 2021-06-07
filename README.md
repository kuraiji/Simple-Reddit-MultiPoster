# Simple-Reddit-MultiPoster
## Basic Instructions:
1. Download the latest release
2. Fill out your information in the config.ini file
3. Write your selftext message in a .txt file
4. Run main.py

## Additional Notes:

-To get your client id and client secret, follow the "First Steps" section [here](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps)

-You can make as many selftext posts as you want, but just make sure the additional posts follows the same pattern as the sample posts

-For the selftext field, put the name of the text file that contains what you want to post

-Currently only selftext posts are supported

## How to also add the ability to schedule your posts:
-You can use PythonAnywhere to run the script at a certain time. Effectively making it both a multi-poster and post scheduler that is completely free. When scheduling this in PythonAnywhere, make sure to set the python version to [3.6 or higher](https://help.pythonanywhere.com/pages/ScheduledTasks/).

-If you want to use this with PythonAnywhere, make sure to change Day_to_post to the specific day you want to make your post

-Timezone is required to accurately get the current day. Full list of timezones [here](https://gist.github.com/mjrulesamrat/0c1f7de951d3c508fb3a20b4b0b33a98)
