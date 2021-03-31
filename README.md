# Telegram-bot-python
Welcome to the code of **name_of_the_bot**, the best bot in the world!!

## Introduction
This is the code of the beautiful and funny bot **name_of_the_bot**. It's a Telegram bot, which means you can add it to any of your groups or individual chats! 

It has no specific purpose at all, but it has been created to make you smile  :smile:. Even if the ressources for this bot, like this README, are written in English, the bot only replies in **French** for now. Some English version might be made available in the future. This bot is based on the fabulous Python interface for the Telegram Bot API [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot). If you want to contribute to the development of this bot, please have a look at the **contribution** section. 

## Features:
The bot is is currently able to do the following things:

### Commands
- `/help` command: lists all the features described below
- `/start` command: says hi
- `/joke` command: sends a joke from the [Joke API](https://sv443.net/jokeapi/v2/)
- `/roast` comand: sends a punch line from the [Evilinsult API](https://evilinsult.com/api/)
- `/love Bob Alice` command: returns the love compatibility between the two names provided, using this [love calculator API](https://english.api.rakuten.net/ajith/api/love-calculator)
- `/okboomer` command: sends a random hot post from the *okboomer* subreddit.
- `/reddit mildlyinteresting` command: sends a random hot post from the specified subreddit. 
- `/judge Anna` command: creates a poll where all participants can judge the specified person. The poll is composed of 2 positives answers, 2 negatives answers and 1 unrelated answer. Multiple responses are allowed and the poll is not anonymous. 
- `/spongebob J'aime pas le chocolat` command: return the same text but spongebobed formatted: "j'AImE pAs lE cHOcOlaT"

### Messages
- sends a small reaction message when a user send a very long message (900+ characters). (see `message_handler/too_long_message.py`)
- sends a small reaction message when some message contains one of the danger words specified in `message_handler/danger_words_message.py`

## How to contribute
Have you ever wanted to lose your time for a cause that does not help humanity at all? You can spend some frustrating time coding in Python to add useless features to this Bot!

### Getting started
- Clone this repo
- Run `pip install -r requirements.txt` to install dependencies.
- Read this [introduction](https://core.telegram.org/bots) and get your `APIkey` from **BotFather** so you would be able to test your new feature directly from your computer.
- Duplicate `.env.example` and rename the copy into `.env`. Then, add your `APIkey` in the new file.
- Run the bot with the following command: `pipenv run python bot.py`
- Now you can open your Telegram app, look for your bot using its username (the one you gave to BotFather), and talk to it to test your new feature.

### Create a new Command
Commands are triggered in the chat using the `/` character. For example, type `/start` to get the bot say *Hi!* to you. Have a look at all implemented commands [here](tree/main/command_handler).

### Create a new Message Handler
Message Handlers are commands that scan upcoming text messages from your conversation and react to them. Have a look at all implemented Message Handler [here](tree/main/message_handler).

### Create a Pull Request
Once you are happy with the new features you just created, format you code using [black](https://pypi.org/project/black/), push it to a new branch and create a new PR. Don't forget to explain what is the purpose of your new features. You can also improve existing features. I will be happy to review them! :sunglasses:

### Need more help?
If you are quite new to the world of Telegram bots, I recommend you  take a look at the following resources:
- Base Wrapper used in this bot: [python-telegram-bot](https://python-telegram-bot.org/)
- Simple bot examples: [examples](https://github.com/python-telegram-bot/python-telegram-bot/tree/master/examples)

## Privacy
As you have seen in the features list, this bot requires **full access to your messages** to work properly. If you look at the code you will notice that I never store or use any messages to collect data about you or your groups. As I value privacy as a human right, I can assure you that I don't and will never sell your data or use it for any other purpose than having fun with this bot. I run an instance of this code on my server (`@blabla`) that make this bot alive. This instance is and will always be a version of the code hosted in this repository, even though I have not found a way to prove it, yet.

If you don't trust me, that is also fine! You can also run a copy of this repository on your own server and have total control over your data. **Be careful** if you use version of this bot hosted by someone else, since they have access to all of your messages.

If you are sceptical why you shouldn't give access to anyone to your personnal messages and data, I recommend you watch the great Netflix documentary [The Social Dilemma](https://en.wikipedia.org/wiki/The_Social_Dilemma)

## License
This project is licensed under the [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

