import requests

URL = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky?format=txt"


def get_random_joke(update, context):
    try:
        response = requests.request("GET", url)
        update.message.reply_text(response.text)
    except:
        update.message.reply_text(
            "le serveur semble avoir un problème... c'est pas mon serveur ok? Pas besoin de me flame :("
        )
