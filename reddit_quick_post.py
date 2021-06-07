import praw


class RedditHelper:
    # Constructor
    def __init__(self, client_id, client_secret, username, password):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            password=password,
            user_agent="Scheduler by u/Crygie",
            username=username
        )
        self.reddit.validate_on_submit = True

    # Make a Post on Reddit
    def post(self, subreddit, title, selftext, flair):
        if not flair:
            flair_id = None
        else:
            flair_id = self.get_flair_id(flair, subreddit)
            print(flair_id)
        self.reddit.subreddit(subreddit).submit(title, selftext, flair_id=flair_id)

    # Used to Get the Flair Id from Flair Text
    def get_flair_id(self, flair, subreddit):
        posts = self.reddit.subreddit(subreddit).hot()
        for post in posts:
            if str.lower(flair) == str.lower(post.link_flair_text):
                return post.link_flair_template_id
        raise ValueError(f"Couldn't find the flair \"{flair}\" in the subreddit \"{subreddit}\", "
                         "try a different flair name or just post without a flair")
