import discord
from discord.ext import commands
from discord import app_commands
import requests
import json


class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Quote cog loaded.')

    @app_commands.command(name="quote", description="Gives you a random motivational quote")
    async def Phrase(self, interaction: discord.Interaction, today: bool):
        if today == False:
            responseAPI = requests.get("https://zenquotes.io/api/random")
            data = responseAPI.text
            convertData = json.loads(data)
            quote = convertData[0]['q'] + " - " + convertData[0]['a']
            await interaction.response.send_message(quote)
        else:
            responseAPI = requests.get("https://zenquotes.io/api/today")
            data = responseAPI.text
            convertData = json.loads(data)
            quote = convertData[0]['q'] + " - " + convertData[0]['a']
            await interaction.response.send_message(quote)

async def setup(bot):
    await bot.add_cog(Quote(bot))