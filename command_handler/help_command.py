def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "**Je peux faire les choses suivantes** \n"
        "\n"
        "/help : Pète et Répète sont sur un bateau, Pète tombe à l'eau, tape /help pour savoir qui reste. \n"
        "/start : Je dis juste bonjour parce que je suis gentil. \n"
        "/joke : Je t'envoie un blague. \n"
        "/roast : Je t'envoie un bon gros roasting.\n"
        "/love Bob Alice : Passe-moi deux prénoms et je te donne leur compatibilté amoureuse.\n"
        "/okboomer : Je t'envoie une image du subreddit.\n"
        "/reddit mildlyinteresting : Choisis un subreddit et je t'envoie une image correspondante.\n"
        "/judge Anna : Donne moi le nom de quelqu'un et j'ouvrirai un sondage pour que vous puissiez le juger bien gratuitement alors qu'il n'avait rien demandé.\n"
        "\n"
        "Sinon je parles aussi parfois sans qu'on me le demande, mais vous verrez bien"
    )
