## ChatGPT in your shell

![](https://imgur.com/JphOx3D.png)

OpenAI's ChatGPT integrated into your shell.

![](https://imgur.com/J7YOzSz.png)

### Description

Simple python implementation of OpenAI's ChatGPT intergrated into your shell, leveraging natural language processing and low temperature parameters for focused responses from ChatGPT.

The interaction can be either calling ChatGPT from shell for one off questions, or entering into an interactive chat with ChatGPT.

### Dependencies

* Install module dependencies using pip:
 ```pip install -r requirements.txt```

* OpenAI API key - you can get one [here](https://platform.openai.com/overview) - Dashboard - Settings - View API Keys - Generate


### Installing

* Clone the repo and copy *chatgpt-prompt.py* to a permanent location.

* Open the script and amend `openai.api_key = "API_KEY"` with your aforementioned API key and save.

* Create an alias pointing at the script's location, either in your bash profile *~/.bash_profile* or *~/.bashrc* or *~/.zshrc* - i.e:
 ```alias chatgpt='python3 /path/to/chatgpt-prompt.py'```

### Usage

Using your chosen alias you can call it from shell and pass your question as an argument for one off questions:

```$ chatgpt "What is the meaning of life?"```

![chatgpt](https://imgur.com/3lqDq7M.gif)

Or by calling the alias without argument to enter an interactive chat with ChatGPT:

```$ chatgpt```

![chatgpt-interactive](https://imgur.com/kJTBOPB.gif)
