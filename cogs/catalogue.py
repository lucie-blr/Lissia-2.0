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

    @commands.command(aliases=["catal"])
    async def catalogue(self, ctx, *, reason=None):
        print(reason)
        catalogue = ["Adar","Calypso","Diana","Jack","Kuyo","Midnight","Sacha","Samuel"]
        if reason in catalogue:
            with open (f"./catalogue/{reason}.json", "r") as f:
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
                
            
            embed = discord.Embed(title="Catalogue", description=f"La fiche de {reason} arrive dans un instant !", color=discord.Color.from_rgb(17, 100, 20))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.send(embed=embed)
            embed2 = discord.Embed(title=nom, color=discord.Color.from_rgb(17, 100, 20))
            embed2.set_thumbnail(url=graph)
            embed2.add_field(name="Âge", value=age, inline=True)
            embed2.add_field(name="Surnom", value=surnom, inline=True)
            embed2.add_field(name="Rôle", value=role, inline=True)
            embed2.add_field(name="Capacité", value=capa, inline=True)
            embed2.add_field(name="Bonus", value=bonus, inline=True)
            embed2.add_field(name="Lien", value=fiche, inline=False)
            embed2.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            embed2.set_image(url=image)
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed2)
        else:
            embed = discord.Embed(title="Catalogue", description="Le personnage n'est pas dans le catalogue.", color=discord.Color.from_rgb(17, 100, 20))
            embed.add_field(name="Liste des personnages dans le catalogue :", value=catalogue, inline=True)                
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.send(embed=embed)
            
        print(f'{ctx.author} used catalogue')
        

    
def setup(bot):
    bot.add_cog(Catalogue(bot))
