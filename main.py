# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
from discord import app_commands
import random
import os
from replit import db

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

guild_id = os.environ['GUILD_ID']
guild=discord.Object(id = guild_id)
token = os.environ['SERVER_TOKEN']

intents = discord.Intents.default()
intents.message_content = True

#setup the bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

times_updated = 0

@tree.command(name="setup", description="Setup the professions channels.", guild=guild) 
async def channel_setup(interaction):
  
  await interaction.response.send_message("This is the response.", ephemeral=True)
  from_channel = interaction.channel_id
  channel = client.get_channel(from_channel)
  message = await channel.send("This is to the channel")

  db["sync_msg_id"] = message.id

@tree.command(name="update", description="Update the widgets to the current information", guild=guild)
async def update_embed(interaction, profession:str = "all"):

  channel = client.get_channel(interaction.channel_id)
  message = await channel.fetch_message( db["sync_msg_id"] )
  await message.edit(content="This is new content.")

  print(dir(message))

  

@tree.command(name="reset", description="Reset the message ID")
async def reset_message_id(interaction):
  times_updated = 0
  print(times_updated)
  del db["sync_msg_id"]


@client.event
async def on_ready():
  await tree.sync(guild=discord.Object(id=guild_id))
  print("Ready!")


client.run(token)
