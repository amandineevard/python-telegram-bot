import random
from . import reddit_handler
import os

SUBREDDIT = "okboomer"



def get_random_ok_boomer_meme(update, context):
    try:
        meme_url = reddit_handler.get_random_image_url_for_subreddit(SUBREDDIT)
        context.bot.sendPhoto(update.message.chat_id, meme_url)

    except (Exception):
        update.message.reply_text(str(e))
