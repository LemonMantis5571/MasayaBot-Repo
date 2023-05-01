# Masaya-Bot
Discord Bot
This Discord bot is designed to help users schedule tasks, search the Pokedex, query Wikipedia, and provide daily motivational quotes. It was developed using Discord.py, wikiAPI, POKEAPI, and QUOTEAPI to integrate various functionalities.

# Table of Contents
Installation
Usage
Features
Contributing
License
Installation
To use the Discord bot, you will need to have Python 3.6 or later installed on your computer. Once you have installed Python, you can install the required packages by running the following command:

```
pip install -r requirements.txt
After the required packages have been installed, you will need to create a new Discord bot by following the instructions in the Discord Developer Portal.
```

Once you have created your bot, you will need to create a .env file in the project directory and add the following information:

```
DISCORD_TOKEN=<your_bot_token>
Replace <your_bot_token> with your actual bot token.
```

Usage
To use the Discord bot, run the following command:

```
python bot.py
//This will start the bot and allow it to listen for commands in your Discord server.
```
Features
The Discord bot has the following features:

Schedule tasks: Users can schedule tasks using the !schedule command. The bot will send a reminder to the user at the specified time.

Pokedex search: Users can search for Pokemon using the !pokemon command. The bot will provide information about the Pokemon, including its type, abilities, and stats.

Wikipedia query: Users can search for information on Wikipedia using the !wiki command. The bot will provide a summary of the Wikipedia page.

Motivational quotes: Users can get a daily motivational quote using the !quote command. The bot will provide a quote to help motivate and inspire the user.

Contributing
If you would like to contribute to the Discord bot, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more information.
