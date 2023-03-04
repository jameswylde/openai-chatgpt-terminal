import openai
import sys
import spacy
import colorama
from colorama import Fore, Back, Style

openai.api_key = "API_KEY"

messages = []

nlp = spacy.load('en_core_web_sm')

if len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    print(Fore.YELLOW + "\nChatGPT: ")
else:
    print(Fore.YELLOW + "\nChatGPT: " + "How can I help?\n")
    prompt = input(Fore.BLUE + "You: ")

    prompt_doc = nlp(prompt)
    prompt_noun_phrases = [chunk.text for chunk in prompt_doc.noun_chunks]
    prompt = " ".join(prompt_noun_phrases)

while True:
            if prompt.lower() in ["quit","q", "bye"]:
                print(Fore.YELLOW + "\nChatGPT: " + "Bye")
                break
            messages.append({"role": "user", "content": prompt})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=0.5,
                messages=messages)
            reply = response["choices"][0]["message"]["content"]

            reply_doc = nlp(reply)
            reply_noun_phrases = [chunk.text for chunk in reply_doc.noun_chunks]
            prompt = " ".join(reply_noun_phrases)

            messages.append({"role": "assistant", "content": reply})
            print(Fore.YELLOW + "\nChatGPT: " + reply + "\n")

            if len(sys.argv) > 1:
                break
            else:
                prompt = input(Fore.BLUE + "You: ")