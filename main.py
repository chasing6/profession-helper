import os #for server env
import discord
from discord import app_commands
from replit import db

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

guild_id = os.environ['GUILD_ID']

@tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id = guild_id)) 
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(name = "secondcommand", description = "My second application Command", guild=discord.Object(id = guild_id)) 
async def second_command(interaction):
    await interaction.response.send_message("Hello!", ephemeral = True )



@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guild_id))
    print("Ready!")

client.run(os.environ['SERVER_TOKEN'])


