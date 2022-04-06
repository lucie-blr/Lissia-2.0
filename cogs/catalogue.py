from operator import iadd
import discord
from discord.ext import commands
import json
import os
import validators

def replace(phrase):
    list1 = ["&agrave","&acirc","&eacute","&egrave","&ecirc","icirc","&iuml","&oelig","&ugrave","&ucirc","&ccedil"]
    list2 = ["à","â","é","è","ê","î","ï","œ","ù","û","ç"]
    for i in range(-1,11):
        phrase = phrase.replace(list1[i],list2[i])
    return(phrase)
    
class Catalogue(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open (f"data.json", "r") as t:
        data2 = json.load(t)
        servlist = data2["servlist"]


    @commands.slash_command(guild_ids = servlist, name = "catalogue", description = "command search in the catalogue")
    async def catalogue(self, ctx, *, personnage=None):
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
        print(personnage)
        
        catalogue = []
        
        for filename in os.listdir('./catalogue'):
            if filename.endswith('.json'):
                catalogue.append(f'{filename[:-5]}')
        
        if personnage in catalogue:
            with open (f"./catalogue/{personnage}.json", "r") as f:
                data = json.load(f)
                nom = replace(data["nom"])
                age = replace(data["age"])
                surnom = replace(data["surnom"])
                role = replace(data["role"])
                capa = replace(data["capa"])
                bonus = replace(data["bonus"])
                image = replace(data["image"])
                fiche = replace(data["fiche"])
                
            
            
            
            embed = discord.Embed(title="Catalogue", description=f"La fiche de {personnage} arrive dans un instant !", color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.respond(embed=embed, ephemeral=True)
            embed2 = discord.Embed(title=nom, color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed2.add_field(name="Âge", value=age, inline=True)
            embed2.add_field(name="Surnom", value=surnom, inline=True)
            embed2.add_field(name="Rôle", value=role, inline=True)
            embed2.add_field(name="Capacité", value=capa, inline=True)
            embed2.add_field(name="Bonus", value=bonus, inline=True)
            embed2.add_field(name="Lien", value=fiche, inline=False)
            embed2.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            
            if validators.url(image):
                embed2.set_image(url=f"{image}")
            else:
                embed2.set_image(url="https://upload.wikimedia.org/wikipedia/commons/9/9a/Gull_portrait_ca_usa.jpg")
            
            await ctx.respond(embed=embed2, ephemeral=True)
        else:
            
            txt = ""
            
            for i in catalogue:
                txt = txt + i + ", "
                
            embed = discord.Embed(title="Catalogue", description="Le personnage n'est pas dans le catalogue.", color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed.add_field(name="Liste des personnages dans le catalogue :", value=txt, inline=True)                
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.respond(embed=embed, ephemeral=True)
            
        print(f'{ctx.author} used catalogue')
        
    @commands.slash_command(guild_ids = servlist, name = "catalogue_add", description = "command to add a character in the catalogue")
    async def catadd(self, ctx,*, nom=None, age=None, surnom=None, role=None, capacity=None, bonus=None, lien_de_la_fiche=None, lien_image=None):
        fiche = {
    "nom":f"{nom}",
    "age":f"{age}",
    "surnom":f"{surnom}",
    "role":f"{role}",
    "capa":f"{capacity}",
    "bonus":f"{bonus}",
    "fiche":f"{lien_de_la_fiche}",
    "image":f"{lien_image}"
        }
        catalogue = []
        
        for filename in os.listdir('./catalogue'):
            if filename.endswith('.json'):
                catalogue.append(f'{filename[:-5]}')
        
        if nom in catalogue:
            with open (f"./catalogue/{nom}.json", "w") as f:
                json.dump(fiche,f)
            await ctx.respond("Personnage ajouté au catalogue !", ephemeral=True)
        else:
            await ctx.respond("Personne déjà présent dans le catalogue.", ephemeral=True)
        
    @commands.slash_command(guild_ids = servlist, name = "catalogue_delete", description = "command to remove a character in the catalogue")   
    async def catrm(self, ctx, personnage):
        
        catalogue = []
        
        for filename in os.listdir('./catalogue'):
            if filename.endswith('.json'):
                catalogue.append(f'{filename[:-5]}')
        
        if personnage in catalogue:
            
            os.remove(f"./catalogue/{personnage}.json")
            await ctx.respond("Personnage supprimée du catalogue !", ephemeral=True)
        
        else:
            await ctx.respond("Le pesronnage n'est pas dans le catalogue.", ephemeral=True)
    
def setup(bot):
    bot.add_cog(Catalogue(bot))
