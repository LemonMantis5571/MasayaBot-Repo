import discord
import os
import wikipediaapi as wikiAPI
import asyncio
from discord import app_commands
from discord.ext import commands

class Wikipedia(commands.Cog):
    """Busca la mayoria de cosas en wikipedia"""
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Wiki cog loaded.')
        
        
    

    @app_commands.command(name="wiki", description="Search in wikipedia")
    # async def Phrase(self, interaction: discord.Interaction, today: bool):   
    async def wikipedia(self, interaction: discord.Interaction, query: str, section:str=None):
        site = wikiAPI.Wikipedia('en')
        url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Wikipedia-logo-v2-es.svg/1200px-Wikipedia-logo-v2-es.svg.png'
        pageQuery = site.page(query)
        pageSummary  = pageQuery.summary[0:300].split('.')[0]
        
        
        embed = discord.Embed(title=pageQuery.title, description=f'Results for: {query}')
        embed.set_thumbnail(url=f'{url}')
        
        # embed = discord.Embed(title=f'ID: {pokeId}', description=f'{pokesearched.name.capitalize()}', colour=colors[f'{pokeTypes[0]}'])
        # embed.set_thumbnail(url=f"{pokeUrl}")
        # embed.add_field(name="Types", value=f'{filteredPoketypes}', inline=False)
        # embed.add_field(name="Height", value=f' {pokeHeight}', inline=False)
        # embed.add_field(name="Weight", value=f' {pokeWeight}', inline=False)

        if pageQuery.exists():
            message = f'Results for {query}: {pageSummary} {pageQuery.fullurl}'
            embed.add_field(name='Summary', value=f'{pageSummary}', inline=False)
               
            if section is not None:
                pageSections = pageQuery.section_by_title(section.capitalize())
                if pageSections is not None:
                    pageText = pageSections.text[0:300].split('.')[0]
                    print(pageText)
                    embed.remove_field(index=1)
                    embed.add_field(name=f'{pageSections.title}', value=f'{pageText}')
                
                else:
                    
                    await interaction.response.send_message(content=f"This section doesn't exist on {query.capitalize()}'s page")
            embed.add_field(name='Read more', value=f'[here]({pageQuery.fullurl})', inline=False)    
            await interaction.response.send_message(embed=embed)
                
        else:
            await interaction.response.send_message(content='⚡ Page not found. Please make sure you have the correct name!', ephemeral=True)
            
            


async def setup(bot):
    await bot.add_cog(Wikipedia(bot))