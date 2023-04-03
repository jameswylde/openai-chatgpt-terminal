## ChatGPT in your terminal

OpenAI's ChatGPT integrated into your shell.

![](https://imgur.com/2WDy29Y.png)

### Note ChatGPT4 - Limited Access Beta

Despite the release of ChatGPT4, the default model used here is `gpt-3.5-turbo` for a more fluent experience as its replies are much faster and API pricing is significantly cheaper.

You can switch API model using the `--model` argument (run without `--model` to use the default model) if you'd like to to use gpt-4:

```$ genie --model gpt-4```

`--model` will also accept *code-davinci-002* & *text-davinci-003* - other API models can be seen here [OpenAI ChatGPT API Models](https://platform.openai.com/docs/models) and added as required to the script.

### Description

Python implementation of OpenAI's ChatGPT intergrated into your shell - interaction can be either calling genie from shell for one off questions, or entering into an interactive chat with genie. There are some chat prompts to use for more honed responses - these can be added or amended in `prompts.py`

### Dependencies

* Install module dependencies using pip:
 ```pip install -r requirements.txt```

* OpenAI API key - you can get one [here](https://platform.openai.com/overview) - Dashboard - Settings - View API Keys - Generate


### Installing

* Clone the repo and copy *genie.py* to a permanent location.

* Open the script and amend `openai.api_key = "API_KEY"` with your aforementioned API key and save.

* Create an alias pointing at the script's location, either in your bash profile *~/.bash_profile* or *~/.bashrc* or *~/.zshrc* - i.e:
 ```alias genie='python3 /path/to/genie.py'```

### Usage

Using your chosen alias you can call it from shell and pass your question as an argument for one off questions:

```$ genie "Recommend a python module for LP and link documentation?"```

![genie](https://imgur.com/JYfwkd7.png)

Or by calling the alias without argument to enter an interactive chat with ChatGPT:

```$ genie ```

![genie-interactive](https://imgur.com/40kRhBe.png)

To end the interactive chat, use either `bye`,`quit`,`q` or `ctrl+c`.

### Example of using gpt-4 model for depth

![](https://imgur.com/8Ctreh3.png)
