import openai
import sys
import random
import string
import colorama
from extras import greeting, lamp
from colorama import Fore, Back, Style

openai.api_key = "API_KEY"

messages = []

randomgreeting = random.choice(greeting)

if len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:]).rstrip(string.punctuation)
else:
    print(Fore.YELLOW + lamp)
    print(Fore.YELLOW + "\nGenie: " + randomgreeting + "\n")
    prompt = input(Fore.BLUE + "Master: ")
while True:
    if prompt.lower() in ["quit", "q", "bye"]:
        print(Fore.YELLOW + "\nGenie: " + "Farewell, master. Until you drag me out of bed again...\n")
        break

    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Replace with the GPT-4 model name
        messages=messages,
        temperature=0.7)
    reply = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": reply})
    print(Fore.YELLOW + "\nGenie: " + reply + "\n")
    
    if len(sys.argv) > 1:
            break
    else:
            prompt = input(Fore.BLUE + "Master: ")

