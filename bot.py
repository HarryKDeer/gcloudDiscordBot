import discord
import subprocess
from mcstatus import JavaServer
import os

intents = discord.Intents.default() #Setting up Intents
intentes.message_content = True
client = discord.Client(intents=intents)

TOKEN = #Insert the token you have for your discord bot

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  content = message.content

  if message.author == client.user: #Check if the bot itself sent a message
    return

  elif content == "$start":
    print("Server requested to start")
    await message.channel.send("Server will be starting momentarily\nThis takes around half a minute")
  elif content == "$status":
    print("Getting status of Minecraft server")
    await message.channel.send("Fetching status of server\nThis might take a moment")
    server = JavaServer.lookup("0.0.0.0:25565") #Replace with server IP and port
    try: 
      status = server.status()
      print("The server is online and has {0} players.".format(status.players.online))
    except:
      print("Server is offline")
      await message.channel.send("Server is offline\nUse the command, '$start' to turn it back on")

client.run(TOKEN) #starts the bot
