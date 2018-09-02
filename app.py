import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            f"did you mean {get_close_matches(w, data.keys())[0]} instead?, type 'y' for Yes or 'n' to for no to continue: ")

        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return "word doesn't exist, please double check it.."
        else:
            return "we didn't understand your entry.."

    else:
        return "word doesn't exist, please double check it.."


word = input("Enter word: ")
output = translate(word.lower())

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
