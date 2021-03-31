#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from command_handler import *
from dotenv import load_dotenv
import logging
from message_handler import *
import os


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
load_dotenv()


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(os.getenv("API_KEY"), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # On different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start_command.start))
    dp.add_handler(CommandHandler("help", help_command.help))
    dp.add_handler(CommandHandler("joke", random_joke_command.get_random_joke))
    dp.add_handler(CommandHandler("roast", random_insult_command.get_random_insult))
    dp.add_handler(CommandHandler("love", love_calculator_command.get_love_between))
    dp.add_handler(
        CommandHandler("okboomer", ok_boomer_command.get_random_ok_boomer_meme)
    )
    dp.add_handler(
        CommandHandler("reddit", random_reddit_command.get_random_subreddit_meme)
    )
    dp.add_handler(CommandHandler("judge", judge_poll_command.get_judgement_poll))
    dp.add_handler(CommandHandler("spongebob", spongebob_command.spongebob_text))


    # Text command:
    dp.add_handler(
        MessageHandler(
            Filters.text,
            lambda update, context: danger_words_message.contains_danger_word(
                update, context, 0.5
            ),
        )
    )
    dp.add_handler(
        MessageHandler(
            Filters.text,
            lambda update, context: too_long_message.is_too_long(update, context, 0.8),
        )
    )

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
