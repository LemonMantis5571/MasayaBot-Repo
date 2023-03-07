import discord
import asyncio
import pokebase as pb
from discord import app_commands
from discord.ext import commands


class Pokemon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.Cog.listener()
    async def on_ready(self):
            print('Pokemon cog loaded.')
    
    @app_commands.command(name="pokedex", description="Search for a pokemon on PokeAPI")
    async def Pokedex(self, interaction: discord.Interaction, pokemon:str):
        pokeTypes =[]
        
        await interaction.response.defer(thinking=True)
        
        if pokemon.isnumeric():
            pokesearched = pb.pokemon(int(pokemon))
            
        
        else:
            pokesearched = pb.pokemon(pokemon.lower())


        pokeHeight = pokesearched.height
        pokeWeight = pokesearched.weight
        pokeName = pokesearched.name
        pokeId = pokesearched.id
        
        for type_slot in pokesearched.types:
            pokeTypes.append(type_slot.type.name.title())
        
        filteredPoketypes = ', '.join(pokeTypes) 
        pokeImage = pb.SpriteResource('pokemon', pokeId)
        pokeUrl = pokeImage.url
        
        await asyncio.sleep(3)

        colors = {
            'Normal': int('A8A77A', 16),
            'Fire': int('EE8130', 16),
            'Water': int('6390F0', 16), 
            'Electric': int('F7D02C', 16), 
            'Grass': int('7AC74C', 16),
            'Ice': int('96D9D6', 16),
            'Fighting': int('C22E28', 16),
            'Poison': int('A33EA1', 16),
            'Ground': int('E2BF65', 16),
            'Flying': int('A98FF3', 16),
            'Psychic': int('F95587', 16),
            'Bug': int('A6B91A', 16),
            'Rock': int('B6A136',16),
            'Ghost': int('735797',16),
            'Dragon': int('6F35FC',16),
            'Dark': int('705746', 16),
            'Steel': int('B7B7CE', 16),
            'Fairy': int('D685AD', 16)
            }
        
        embed = discord.Embed(title=f'ID: {pokeId}', description=f'{pokesearched.name.capitalize()}', colour=colors[f'{pokeTypes[0]}'])
        embed.set_thumbnail(url=f"{pokeUrl}")
        embed.add_field(name="Types", value=f'{filteredPoketypes}', inline=False)
        embed.add_field(name="Height", value=f' {pokeHeight}', inline=False)
        embed.add_field(name="Weight", value=f' {pokeWeight}', inline=False)

        await interaction.followup.send(embed=embed);
            
async def setup(bot):
    await bot.add_cog(Pokemon(bot))
    
    