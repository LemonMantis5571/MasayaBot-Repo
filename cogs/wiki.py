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
        
        if pageQuery.exists():
            embed.add_field(name='Summary', value=pageSummary, inline=False)

            if section is None:
                sections = pageQuery.sections
                for s in sections:
                    section_title = s.title
                    section_text = s.text[0:100].split('.')[0]
                    embed.add_field(name=section_title, value=section_text, inline=False)

            else:
                section_title = section.capitalize()
                page_section = pageQuery.section_by_title(section_title)

                if page_section:
                    section_text = page_section.text[0:300].split('.')[0]
                    embed.add_field(name=page_section.title, value=section_text)
                else:
                    message = f"This section doesn't exist on {query.capitalize()}'s page"
                    await interaction.response.send_message(content=message)

            read_more = f"[here]({pageQuery.fullurl})"
            embed.add_field(name='Read more', value=read_more, inline=False)

            await interaction.response.send_message(embed=embed)

        else:
            message = '⚡ Page not found. Please make sure you have the correct name!'
            await interaction.response.send_message(content=message, ephemeral=True)
                    
            


async def setup(bot):
    await bot.add_cog(Wikipedia(bot))