import os #for server env
from discord.ext import commands
import discord
from discord import app_commands 
from discord.ui import view, item, select 
from replit import db

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

guild_id = os.environ['GUILD_ID']

# Define a simple View that persists between bot restarts
# In order a view to persist between restarts it needs to meet the following conditions:
# 1) The timeout of the View has to be set to None
# 2) Every item in the View has to have a custom_id set
# It is recommended that the custom_id be sufficiently unique to
# prevent conflicts with other buttons the bot sends.
# For this example the custom_id is prefixed with the name of the bot.
# Note that custom_ids can only be up to 100 characters long.
class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Green', style=discord.ButtonStyle.green, custom_id='persistent_view:green')
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is green.', ephemeral=True)

    @discord.ui.button(label='Red', style=discord.ButtonStyle.red, custom_id='persistent_view:red')
    async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is red.', ephemeral=True)

    @discord.ui.button(label='Grey', style=discord.ButtonStyle.grey, custom_id='persistent_view:grey')
    async def grey(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is grey.', ephemeral=True)

#
# Slash Commands
#

@tree.command(name = "add", description = "Add a recipe that one of your characters knows. Use wowhead.com spell id.", guild=discord.Object(id = guild_id)) 
async def first_command(interaction, recipe: int ):

  reply_msg = "We've added {} to your list of recipes!"
  await interaction.response.send_message(reply_msg.format(recipe), ephemeral = True )
  print("Added", recipe) 

@tree.command(name = "embed", description = "Embed the test case.", guild=discord.Object(id = guild_id) )
async def embed(ctx):

  #### Create the initial embed object ####
  embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0x109319)
  
  # Add author, thumbnail, fields, and footer to the embed
  embed.set_author(name="Alchemy", icon_url="https://wow.zamimg.com/images/wow/icons/large/trade_alchemy.jpg")
  
  embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
  
  embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False) 
  embed.add_field(name="Field 2 Title", value="It is inline with Field 3", inline=True)
  embed.add_field(name="Field 3 Title", value="It is inline with Field 2", inline=True)
  
  embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")

  view = PersistentView()
  message = await ctx.response.send_message(embed=embed, view=view)

  print(message)

#
# Discord View
#


  

#
# Run Bot
#

@client.event
async def on_ready():
  await tree.sync(guild=discord.Object(id=guild_id))
  print("Ready!")

client.run(os.environ['SERVER_TOKEN'])



