from http import client
import os
from discord.ext import commands
from dotenv import dotenv_values
import praw
import random
import time

# get discord token and reddit client_id, client_secret from tokens.env
tokens = dotenv_values("tokens.env")
discordToken = tokens["DISCORD_TOKEN"]
redditClientID = tokens["CLIENT_ID"]
redditClientSecret = tokens["CLIENT_SECRET"]

# access reddit using credentials supplied above
reddit = praw.Reddit(client_id=redditClientID,
                     client_secret=redditClientSecret,
                     user_agent="Discord Bot by Luke Sellmayer")
subreddit = reddit.subreddit("copypasta")

bot = commands.Bot(command_prefix='chasbot ')

print("Chasbot is running...")

# for use in copypasta command with really long copypastas
def split_string(string_input, limit, sep=" "):
    words = string_input.split()
    if max(map(len, words)) > limit:
        pass
    res, part, others = [], words[0], words[1:]
    for word in others:
        if len(sep) + len(word) > limit - len(part):
            res.append(part)
            part = word
        else:
            part += sep + word
    if part:
        res.append(part)
    return res

# determine if any word in a sent message ends with an r
def detect_r(input_string):
    words = input_string.split()
    for word in words:
        if word[-1] == 'r':
            return True

# find the word that ends with an r in a sent message
def find_r(input_string):
    words = input_string.split()
    for word in words:
        if word[-1] == 'r':
            return word

# make chasbot do some vocal improvisation
@bot.command(name="scat")
async def scat(ctx):
    scat_num = random.randrange(10, 30)
    scat_list = ["skiddly", "doo", "do", "dop", "doop", "boo", "bo", "bop", "boop", "beep", "bloop", "bah", "dah",
                 "bee", "dee", "ski", "ska", "dit", "dat", "dot"]
    response = ""
    for x in range(scat_num):
        response += random.choice(scat_list)
        dashmodifier = random.random()
        # dashes are randomly added between words
        if dashmodifier > 0.65:
            response += "-"
        else:
            response += " "
    await ctx.send(response)

# make chasbot say a random copypasta from r/copypasta
@bot.command(name="copypasta")
async def copypasta(ctx):
    await ctx.send("One moment...")
    random_post = subreddit.random()
    await ctx.send("Copypasta title: " + random_post.title)
    await ctx.send("-------------------")
    for element in split_string(string_input=random_post.selftext, limit=2000):
        await ctx.send(element)

# make chasbot explain how good a user is at jazz
@bot.command(name="jazzscale")
async def jazzscale(ctx, *target):
    response = "b"
    odds = random.random()

    if 0 <= odds < 0.188:
        response = '{} is bad at jazz and can suck my scat'.format(" ".join(target))
    elif 0.188 <= odds < 0.376:
        response = "{} is a jazz noob".format(" ".join(target))
    elif 0.376 <= odds < 0.564:
        response = "{} is a jazz amateur".format(" ".join(target))
    elif 0.564 <= odds < 0.752:
        response = "{} is a semipro at jazz".format(" ".join(target))
    elif 0.752 <= odds < 0.94:
        response = "{} is a pro at jazz".format(" ".join(target))
    elif 0.94 <= odds < 0.99:
        response = "{} is a jazz master and I wish to [REDACTED] with them".format(" ".join(target))
    elif odds >= 0.99:
        response = "{} is a jazz deity and I will glady [REDACTED] whenever it pleases them".format(
            " ".join(target))

    await ctx.send(response)

# chasbot also responds to keywords in messages
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
    # he doesn't respond to his own messages though
    if message.author == bot.user:
        return

    # chasbot responds to his name even if it isn't a command
    if 'chas' in message.content.lower() and "chasbot" not in message.content.lower():
        chas_replies = ["Skiddly doo bop!", "*scatting noises*", "My mind is going beep bloop",
                        "I love all my students equally", "I am the superior choir teacher",
                        "Hi, my name is Chas Douthit, and welcome to a Douthit Family Christmas",
                        "And now, for a special viewing of 'The Douthit Family Legacy'",
                        "What color should I paint my nails?", "It is time for [REDACTED] inspection", "God I love scatting",
                        "Anyone who is not in jazz choir is an incel", "One more word and I'll scat",
                        "Every morning I wake up and smell the scat",
                        "Everyone knows that scatting is much harder than actual improv",
                        "Anyone who does not audtion for all state will be punished", "You called?",
                        "What do you want now?", "Leave me alone so that I may scat",
                        "Call me by my full name: Chasles", "Someone in this choir is flat and it's probably you, Erin",
                        "Choir is a liberal art", "Wait for the chorus, WAIT FOR THE CHORUS",
                        "Let's sing that song from Big Mouth!", "Everyone can leave except for the doowops and the boyfriends",
                        "The rain has passed", "Erin, these notes are really difficult so I need you to focus, please"]
        response = random.choice(chas_replies)
        await message.channel.send(response)
    # chasbot loves jazz
    elif 'jazz' in message.content.lower() and "chasbot" not in message.content.lower():
        jazz_replies = ["Man I sure do love jazz. Speaking of jazz, why exactly did you drop jazz again, Tasha?",
                        "I smell jazz in the air",
                        "I love jazz so much I just can't fathom why anyone would drop that class",
                        "Love is in the air? More like jazz is in the air",
                        "Every morning I wake up, drink my coffee, and listen to smooth jazz",
                        "Tasha please rejoin jazz choir, I'll do anything", "j a z z"]
        response = random.choice(jazz_replies)
        await message.channel.send(response)
    # chasbot doesn't tolerate homophobia
    elif "gay" in message.content.lower():
        await message.channel.send("I will not tolerate homophobia in this discord")
    # chasbot preaches kindness
    elif "shut up" in message.content.lower():
        await message.channel.send("I will not tolerate usage of the phrase 'shut up' within this discord")
    elif "bitch" in message.content.lower():
        await message.channel.send("I will not tolerate the usage of the word 'bitch' within this discord")
    # chasbot doesn't like cullen
    elif "cullen" in message.content.lower():
        cullen_replies = ["You can run but you can't hide from me, Cullen", "You have no power over me, Cullen", "Silence Cullen", "Why do you hate me Cullen", "Cullen wishes he was me"]
        response = random.choice(cullen_replies)
        await message.channel.send(response)
    elif ":" in message.content[0]:
        pass
    # ...?
    elif detect_r(message.content.lower()):
        await message.channel.send("Don't say {} with a hard r".format(find_r(message.content.lower())))

bot.run(discordToken)
