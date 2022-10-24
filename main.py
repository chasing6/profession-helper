import os #for server env
import discord
from discord import app_commands
from replit import db

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

guild_id = os.environ['GUILD_ID']

@tree.command(name = "add", description = "Add a recipe that one of your characters knows. Use wowhead.com spell id.", guild=discord.Object(id = guild_id)) 
async def first_command(interaction, recipe: int ):

  reply_msg = "We've added {} to your list of recipes!"
  await interaction.response.send_message(reply_msg.format(recipe), ephemeral = True )
  print("Added", recipe) 

@client.event
async def on_ready():
  await tree.sync(guild=discord.Object(id=guild_id))
  print("Ready!")

client.run(os.environ['SERVER_TOKEN'])


