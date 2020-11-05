import asyncio
import discord
import matplotlib.pyplot as plt
import os
import re

from discord.ext import commands
from os import path
from wordcloud import WordCloud

bot = commands.Bot("!", self_bot=True)
client = discord.Client()
d = path.dirname(__file__)

@bot.event
async def on_ready():
    print ("User Bot ready. Type !search in any channel to search through the messages.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        content = message.content
        if (content == "!search"):
            await handle_search_pm(message.channel)

@bot.event
async def handle_search_pm(channel):
    print(f"Beginning search for {channel.name}")
    messages = await channel.history(limit=None).flatten()
    message_infos = {}

    all_messages = []
    for message in messages:
        if message.author.name not in message_infos:
            message_infos[message.author.name] = 1
        else:
            message_infos[message.author.name] += 1
        all_messages.append(message.content)

    fd = open(path.join(d, f"output/{channel.id}-{channel.name}-output.txt"), "w+")
    total_length = 0
    for line in all_messages:
        clean_line = re.sub(r"""
               [,.;@#?!&$]+  # Accept one or more copies of punctuation
               \ *           # plus zero or more copies of a space,
               """,
               " ",          # and replace it with a single space
               line, flags=re.VERBOSE)

        sanitized = clean_line.encode('ascii', 'ignore').decode('ascii')
        words = sanitized.split(" ")
        total_length += len(words)
        for word in words:
            word = word.strip()
            if word == '' or word == '\n':
                continue
            fd.write(word.lower())
            fd.write("\n")
    fd.close()

    print(f"Total messages: {len(messages)}, average message length (in words): {total_length / len(messages)}")
    print("Specific message breakdown: (how many messages per each person)")
    print(message_infos)
    print("Generating word cloud...")
    generate_word_cloud(channel.name, channel.id)
        

def generate_word_cloud(channel_name, channel_id):
    text = open(path.join(d, f'output/{channel_id}-{channel_name}-output.txt')).read()

    words = open(path.join(d, "stopwords.txt"), "r")
    content = words.read()
    content_list = content.split("\n")
    words.close()

    wordcloud = WordCloud(width = 800, height = 800, max_font_size=80, stopwords=content_list, max_words=300, collocations=False).generate(text)
    plt.figure(figsize = (8, 8))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    wordcloud.to_file(path.join(d, f"output/{channel_id}-{channel_name}-output.png"))
    print(f"Files outputted to output/{channel_id}-{channel_name} png and txt")
    exit()

    
token = "Your Token Here"
bot.run(token, bot=False)