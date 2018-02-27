import discord
from discord.ext import commands
import urllib.request, json 

Client = discord.Client()
client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def ping(text1, text2):
    await client.say("pong" + text1 + "||" + text2)

@client.command()
async def joke():
    data = json.loads(urllib.request.urlopen("http://api.icndb.com/jokes/random").read().decode())
    await client.say((data['value']['joke']).replace("&quot;","\""))


client.run("NDE3NjM3MTc3Nzk1ODA1MjA0.DXbUsQ.kD2npXOfW6g6Kksw5rGH_VCjX_U")
