import praw
import os
import random

ALLOWED_EXTENSIONS_FOR_IMAGES = ["jpeg", "jpg", "png"]


def get_random_image_url_for_subreddit(subreddit_name):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )

    subreddit = reddit.subreddit(subreddit_name)
    try:
        posts = subreddit.hot(limit=100)
        posts_url = [
            post.url for post in posts if ext(post.url) in ALLOWED_EXTENSIONS_FOR_IMAGES
        ]
    except:
        raise RuntimeError("Le subbredit ne semble pas correct")
    return random.choice(list(posts_url))


def ext(str_):
    parts = str_.split(".")
    return parts[len(parts) - 1]
