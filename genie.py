import openai
import sys
import random
import string
import colorama
import argparse
from extras import greeting, lamp
from colorama import Fore, Back, Style

def parse_args():
    parser = argparse.ArgumentParser(description="Genie: Interact with ChatGPT")
    parser.add_argument("--model", default="gpt-4", choices=["gpt-4", "gpt-3.5-turbo","code-davinci-002","text-davinci-003"], help="Choose the API model")
    parser.add_argument("question", nargs="*", help="Optional question for non-interactive mode")
    return parser.parse_args()

args = parse_args()

openai.api_key = "API_KEY"

messages = []

randomgreeting = random.choice(greeting)

if args.question:
    prompt = " ".join(args.question).rstrip(string.punctuation)
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
        model=args.model,
        messages=messages,
        temperature=0.7)
    reply = response["choices"][0]["message"]["content"]

    messages.append({"role": "assistant", "content": reply})
    print(Fore.YELLOW + "\nGenie: " + reply + "\n")

    if args.question:
        break
    else:
        prompt = input(Fore.BLUE + "Master: ")
