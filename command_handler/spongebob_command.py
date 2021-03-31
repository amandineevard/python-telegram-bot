"""
spongebob_command.py
-----------------------------
Spongebob command for the telegram bot. Takes some string returns it with alternated case for each character, similar to the spongebob meme.
Example : "why are you poor ? just buy a house" -> "wHy aRe yOu pOoR ? JuSt bUy a hOuSe"


Author : Ludovic Herbelin
27.03.2021
"""

import random
import re

# probability that the letter will be changed, to add osme variety
CASE_PROBABILITY = 0.9

def __alternate_case_text__(text):
    """
    Returns an alternated case version of a text

        Parameters:
            text (string): Some text 
        Returns:
            updated_text(string): The alternated case version of the string
    """
    updated_text = []
    for i in range(0, len(text)):
        c = text[i]
        rand_n = random.random()
        # every letter at an odd position can be changed to upper at random
        if i % 2 != 0 and rand_n > (1.0 - CASE_PROBABILITY):
            c = c.upper()
        # if not an odd positon we can still set it to upper sometimes
        elif rand_n > CASE_PROBABILITY:
            c = c.upper()
        
        # add in a list so we don't concatenate every iteration
        updated_text.append(c)

    # returns the list a string with '' (nothing) as a joining char
    return ''.join(updated_text)

def spongebob_text(update, context):
    try:
        # get the user's full message
        message_text = update.message.text

        # check that there was some text given apart from the command
        if ' ' not in message_text:
            raise ValueError('No text given after command')

        # remove the command from the user text (up to the first space)
        user_input = re.sub(r'^.*? ', ' ', message_text).lstrip()

        if len(user_input) == 0:
            raise ValueError('No text given after command')

        update.message.reply_text(__alternate_case_text__(user_input))

    except (IndexError, ValueError):
        update.message.reply_text(
            "Essaie de me donner un texte avec la commande. Même toi tu dois pouvoir le faire. Ré-essaie comme ceci: /spongebob salut"
        )
    except RuntimeError as e:
        update.message.reply_text(str(e))



if __name__ == '__main__':
    text = "/spongebob why are you poor ? just buy a house"
    user_input = re.sub(r'^.*? ', ' ', text).lstrip()
    print(__alternate_case_text__(user_input))
    