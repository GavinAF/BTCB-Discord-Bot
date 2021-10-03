import discord
import os
from discord.channel import TextChannel
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument
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

def search_members(username):
    for guild in bot.guilds:
        for member in guild.members:
            if member.name.startswith(username):
                print("Member Found: " + member.name)
                return(member)
    print("Did not find user")

# When Bob is fully loaded
@bot.event
async def on_ready():
    print("Bob is Building as {0.user}".format(bot))


# If no name is entered when running the build command
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        print("No user given")
        insult = get_insult()
        await ctx.send(insult)

# When Bob receives a message
@bot.command()
async def build(ctx, arg):

    user = search_members(arg)
    insult = get_insult()

    if not user:
        await ctx.send(insult)
        return

    await ctx.send(f"{user.mention} {insult}")

bot.run(os.getenv('TOKEN'))