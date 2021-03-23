import os
import requests

URL = "https://love-calculator.p.rapidapi.com/getPercentage"


def get_love_between(update, context):
    try:
        first_name = context.args[0]
        second_name = context.args[1]
        querystring = {"fname": first_name, "sname": second_name}
        headers = {
            "x-rapidapi-key": os.getenv("API_LOVE_COMPATIBILITY_KEY"),
            "x-rapidapi-host": "love-calculator.p.rapidapi.com",
        }
        response = requests.request("GET", URL, headers=headers, params=querystring)
        update.message.reply_text(
            "Pourcentage: "
            + response.json()["percentage"]
            + "% "
            + response.json()["result"]
        )
    except (IndexError, ValueError):
        update.message.reply_text(
            "Tu dois me donner deux prénoms mon bichon. Essaye comme ça: /love Alice Bob"
        )
