import requests

URL = "https://evilinsult.com/generate_insult.php?lang=en&type=text"


def get_random_insult(update, context):
    try:
        response = requests.request("GET", URL)
        update.message.reply_text(response.text)
    except (Exception):
        update.message.reply_text(
            "le serveur semble avoir un problème... c'est pas mon serveur ok? Pas besoin de me flame :("
        )
