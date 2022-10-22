import os #for server env
import discord
from discord import app_commands
from replit import db

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return #ignore messages from our bot
  if message.content.startswith('$hello'):
    await message.channel.send('Hello', efemeral = true)

client.run(os.environ['serverToken'])


