import random

PREDEFINED_POSITIVE_ANSWERS = [
    "F*cking fantastic human beeing!",
    "Love that guy",
    "'You are as beautiful as my mom'",
    "top 0.1%",
    "BG!",
    "Lui/Elle c'est Obama les autres c'est Trump",
    "Big brain time",
    "C'est pas con ce qu'il/elle dit",
    "J'aime",
    "Bravo",
    "Enorme!",
    "Moi je le comprends quand même",
    "Il a pas tort",
    "Il est pas bien méchant",
    "pls f*ck me",
]
PREDEFINED_NEGATIVE_ANSWERS = [
    "C'est un con",
    "Wow il/elle est encore plus bête que ce que j'imaginais",
    "'jE sUIs tRoP smArT'",
    "On avait pas demandé son avis en fait",
    "Quelqu'un prend la hache ou je m'en occupe?",
    "Ses deux neurones doivent s'être entrechoqué le pauvre",
    "Il/Elle est surement bourré/e",
    "2 brain cells",
    "Je vais pas dépenser un seul clique pour ce/cette dégénéré/e",
    "Can you lick my ass pls?"
]
PREDEFINED_NO_CONTEXT_ANSWERS = [
    "J'aime les canards",
    "Pff",
    "Il fait beau non?",
    "La réponse D",
    "trop de sel ici",
    "je sors ->",
    "Moi j'aime pas le fromage",
    "...",
    "Non",
    "Il y a pas de bonne ou de mauvaise situation",
    "Je crois pas trop à tous ces trucs de chiffres, d'années et de lettres",
    "Je juge pas les gens moi",
    "Moi j'aime bien quand les gens font l'amour"
]


def get_judgement_poll(update, context) -> None:
    try:
        name = context.args[0]
    except (IndexError, ValueError):
        update.message.reply_text(
            "Comment tu veux que je roast quelqu'un si je sais pas qui c'est? Faut faire comme ça: /judge Anna"
        )
        return

    questions = (
        random.sample(PREDEFINED_POSITIVE_ANSWERS, 2)
        + random.sample(PREDEFINED_NEGATIVE_ANSWERS, 2)
        + random.sample(PREDEFINED_NO_CONTEXT_ANSWERS, 1)
    )
    message = context.bot.send_poll(
        update.effective_chat.id,
        "Jugez " + name + " svp:",
        questions,
        is_anonymous=False,
        allows_multiple_answers=True,
    )