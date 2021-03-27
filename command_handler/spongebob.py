"""
Spongebob.py
-----------------------------
Spongebob command for the telegram bot. Takes some string returns it with alternated case for each character, similar to the spongebob meme.
Example : "why are you poor ? just buy a house" -> "wHy aRe yOu pOoR ? JuSt bUy a hOuSe"


Author : Ludovic Herbelin
27.03.2021
"""


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
        if i % 2 == 0:
            c = c.upper()
        
        # add in a list so we don't concatenate every iteration
        updated_text.append(c)

    # returns the list a string with '' (nothing) as a joining char
    return ''.join(updated_text)

def spongebob_text(update, context):
    try:
        text = update.message.text
        update.message.reply_text(__alternate_case_text__(text))

    except (IndexError, ValueError):
        update.message.reply_text(
            "Essaie de me donner un texte avec la commande. Même toi tu dois pouvoir le faire. Ré-essaie comme ceci: /spongebob salut"
        )
    except RuntimeError as e:
        update.message.reply_text(str(e))



if __name__ == '__main__':
    text = "why are you poor ? just buy a house"
    print(__alternate_case_text__(text))
    