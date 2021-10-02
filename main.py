import discord
import os
from dotenv import load_dotenv
import requests
import json

insults_URL = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

load_dotenv()

client = discord.Client()

def get_insult():
    response = requests.get(insults_URL)
    json_data = json.loads(response.text)
    insult = json_data['insult']

    return(insult)



# When Bob is fully loaded
@client.event
async def on_ready():
    print("Bob is Building as {0.user}".format(client))


# When Bob receives a message
@client.event
async def on_message(message):
    if message.author == client.user: # if it's bob's message, ignore it
        return

    if message.content.startswith("!build"): # if someone sends a message with the build prefix
        insult = get_insult()
        await message.channel.send(insult)

client.run(os.getenv('TOKEN'))