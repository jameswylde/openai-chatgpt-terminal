import openai
import sys
import spacy
import colorama
from colorama import Fore

openai.api_key = "API_KEY"

messages = []

# Using Spacy module, load english language model to assist with natural language processing
nlp = spacy.load('en_core_web_sm')

if len(sys.argv) > 1:
    # If there is a command line argument, join all the arguments into a single string
    prompt = " ".join(sys.argv[1:])
else:
    print(Fore.YELLOW + "\nChatGPT: " + "How can I help?\n")
    prompt = input(Fore.BLUE + "You: ")

    # Extract noun phrases from the input prompt and join into a single string
    prompt_doc = nlp(prompt)
    prompt_noun_phrases = [chunk.text for chunk in prompt_doc.noun_chunks]
    prompt = " ".join(prompt_noun_phrases)

while True:
            if prompt.lower() in ["quit","q", "bye"]:
                print(Fore.YELLOW + "\nChatGPT: " + "Bye")
                break
            messages.append({"role": "user", "content": prompt})
            # Using GPT-3.5-turbo model with a temperature of 0.5 for more focused response
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