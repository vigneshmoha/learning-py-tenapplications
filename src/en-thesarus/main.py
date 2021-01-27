import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        prompt = input(f"Did you mean '{get_close_matches(word, data.keys())[0]}'? Enter Y if yes, N if no.")
        if prompt.upper() == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif prompt.upper() == "N":
            return f"Word '{word}' doesn\'t exists. Please double check it."
        else:
            return "We did not understand the input."
    else:
        return f"Word '{word}' doesn\'t exists. Please double check it."

input_word = input("Enter word: ")
output = translate(input_word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
