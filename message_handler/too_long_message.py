import random

TOO_LONG_ANSWER = [
    "Wow le pavé",
    "Oulalaa",
    "Ca sent les embrouilles",
    "Too long did not read",
    "ça donne envie...",
    "Popcorn?",
]


def is_too_long(update, context, probability):
    if len(update.message.text) >= 900 and random.random() <= probability:
        update.message.reply_text(random.choice(TOO_LONG_ANSWER))

