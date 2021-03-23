import random
from . import reddit_handler
import os


def get_random_subreddit_meme(update, context):
    try:
        subreddit = context.args[0]
        meme_url = reddit_handler.get_random_image_url_for_subreddit(subreddit)
        context.bot.sendPhoto(update.message.chat_id, meme_url)

    except (IndexError, ValueError):
        update.message.reply_text(
            "Tu dois me donner le nom du subreddit imbécile. Faut faire comme ça: /reddit mildlyinteresting"
        )
    except RuntimeError as e:
        update.message.reply_text(str(e))
