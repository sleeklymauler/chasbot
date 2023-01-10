# Chasbot

Chasbot is a discord bot, *lovingly* based on a former choir teacher from my high school.

## Features

Chasbot can:
* respond to messages with certain keywords in them, such as "chas", "jazz", "gay", "shut up", "bitch", and words that end in 'r'

  * ![jazz command demonstration](/Examples/jazz.gif)
  * ![chas command demonstration](/Examples/chas.gif)
* respond to the following commands:
  * ```chasbot scat```: chasbot will do a jazz scat
  
    * ![scat command demonstration](/Examples/scat.gif)
  * ```chasbot copypasta```: chasbot will send a random copypasta from the r/copypasta subreddit (this can take a little while)
  
    * ![copypasta command demonstration](/Examples/copypasta.gif)
  * ```chasbot jazzscale [name]```: chasbot will rank [name]'s jazz ability
  
    * ![jazzscale command demonstration](/Examples/jazzscale.gif)

## Set Up

Start by cloning the repository. In order for Chasbot to work, you'll need to install some dependencies and set up the discord and reddit integrations.

### Dependencies

Chasbot requires the following packages:
* [discord.py](https://github.com/Rapptz/discord.py)
* [python-dotenv](https://github.com/theskumar/python-dotenv)
* [praw](https://github.com/praw-dev/praw)

### Discord

Follow [this guide](https://discordpy.readthedocs.io/en/stable/discord.html#creating-a-bot-account) to create a bot with your discord account. Then, paste your discord token in the tokens.env file.

### Reddit

Follow [this guide](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) to a create a reddit application with your reddit account. Specifically, you'll be creating a script type application. Then paste the client_id and client_secret in the tokens.env file.

## Adding Him to a Server

Go back to [this guide](https://discordpy.readthedocs.io/en/stable/discord.html#creating-a-bot-account) and follow the instructions to add him to your server. For permissions, make sure that the following are checked:
* Send messages
* Manage messages
* Embed links
* Read message history

## Running
Use ```python chasbot.py``` in your terminal

### Optional: Running on a Web Server

Chasbot will only stay online as long as chasbot.py is running on your computer. You can keep Chasbot online all the time by running it on a web server. I followed [this guide](https://www.codementor.io/@garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz#keeping-our-bot-alive) to do so. Note that this requires the additional dependency of [Flask](https://flask.palletsprojects.com/en/2.1.x/installation/#install-flask).
