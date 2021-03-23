import random

DANGER_WORDS = ["marxisme", "communiste", "communisme", "hitler", "nazis", "Greta"]
DANGER_WORDS_ANSWERS = [
    "Nooo pls",
    "Ouch",
    "Ca sent les embrouilles",
    "Je le sens pas ce thème",
    "Après bon, il fait beau non?",
    "Je sors ->",
    "On arrête tout de suite svp",
    "Please pas ce thème",
    "Après bon les canards, c'est joli les canards non?",
]


def contains_danger_word(update, context, probability):
    if (
        len([word for word in DANGER_WORDS if word in str.lower(update.message.text)])
        > 0
        and random.random() <= probability
    ):
        update.message.reply_text(random.choice(DANGER_WORDS_ANSWERS))
