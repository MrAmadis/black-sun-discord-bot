import discord
import asyncio
from discord.ext import commands
import urllib.request, json
import requests

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
    
@client.command()
async def weather(town="Karlovac"):
    api_key = "e0fda9b888596f753e2ff0987dfa2706";
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    query = base_url + "?q=%s&units=metric&APPID=%s" % (town, api_key)
    
    response = requests.get(query)
    weather_data = response.json()
    
    embed = discord.Embed(
        title="Weather: " + town, 
        description=str(weather_data['weather'][0]['description']).upper() +
        "\nTemperature: " + str(weather_data['main']['temp']) + " °C" +
        "\nPressure: " + str(weather_data['main']['pressure']) + " hpa"
        "\nHumidity: " + str(weather_data['main']['humidity']) + " %" 
        "\nWind: " + str(weather_data['wind']['speed']) + " m/s",
        color=0x33339B
        )
    await client.say(embed = embed)

client.run("NDE3NjM3MTc3Nzk1ODA1MjA0.DXbUsQ.kD2npXOfW6g6Kksw5rGH_VCjX_U")
