# Discord Python Wordcloud Bot

Very simple self bot that searches through a channel and produces a WordCloud with every message ever sent. Also says how many messages per person were sent, the total amount of messages and average message length.  

**Note**: Using a self bot (providing a user token) is against the Discord Community Guidelines and as such, this repo should only be used with an official bot token, or purely as an educational source.

## Usage

Requires Python 3.6+  
Install https://github.com/Rapptz/discord.py  
Recommend installing numpy1.19.3 rather than numpy1.19.4 to avoid `runtimeError: package fails to pass a sanity check` errors  
Get a token (user token can be retrieved by following https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs#how-to-get-a-user-token  
Place the token in the string at the bottom "Your Token Here"  
Run the bot using `python main.py`  
Go into any channel and type `!search`  
Wait
