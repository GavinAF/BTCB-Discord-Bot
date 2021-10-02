import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import requests
import json

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True
intents.guilds = True
intents.members = True


insults_URL = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
description = "Building your character one line at a time"

load_dotenv()

bot = commands.Bot(command_prefix="!", description=description, intents=intents)

def get_insult():
    response = requests.get(insults_URL)
    json_data = json.loads(response.text)
    insult = json_data['insult']

    return(insult)



# When Bob is fully loaded
@bot.event
async def on_ready():
    print("Bob is Building as {0.user}".format(bot))


# When Bob receives a message
@bot.command()
async def build(ctx, arg):

    insult = get_insult()
    await ctx.send(insult)

bot.run(os.getenv('TOKEN'))