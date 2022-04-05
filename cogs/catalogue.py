import discord
from discord.ext import commands
import json

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
        catalogue = ["Adar","Calypso","Diana","Jack","Kuyo","Midnight","Sacha","Samuel"]
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
                graph = replace(data["graph"])
                
            
            embed = discord.Embed(title="Catalogue", description=f"La fiche de {personnage} arrive dans un instant !", color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.respond(embed=embed, ephemeral=True)
            embed2 = discord.Embed(title=nom, color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed2.set_thumbnail(url=graph)
            embed2.add_field(name="Âge", value=age, inline=True)
            embed2.add_field(name="Surnom", value=surnom, inline=True)
            embed2.add_field(name="Rôle", value=role, inline=True)
            embed2.add_field(name="Capacité", value=capa, inline=True)
            embed2.add_field(name="Bonus", value=bonus, inline=True)
            embed2.add_field(name="Lien", value=fiche, inline=False)
            embed2.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            embed2.set_image(url=image)
            await ctx.respond(embed=embed2, ephemeral=True)
        else:
            embed = discord.Embed(title="Catalogue", description="Le personnage n'est pas dans le catalogue.", color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed.add_field(name="Liste des personnages dans le catalogue :", value=catalogue, inline=True)                
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.respond(embed=embed, ephemeral=True)
            
        print(f'{ctx.author} used catalogue')
        

    
def setup(bot):
    bot.add_cog(Catalogue(bot))
