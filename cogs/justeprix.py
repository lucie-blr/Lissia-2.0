import discord
from discord.ext import commands
import json
import random

class Justeprix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def launchjp(self, ctx):
        prix = random.randint(1000, 2000)
        text = {
            "prix": f"{prix}",
            "launched": "yes"}
        with open("jp.json","w") as data:
            json.dump(text,data)
        await ctx.send(f'Le juste prix a été lancé !')
        print(f'{ctx.author} launch juste prix')

    @commands.command()
    async def stopjp(self, ctx):
        text = {
            "prix": f"",
            "launched": "no"}
        with open("jp.json","w") as data:
            json.dump(text,data)
        await ctx.send("Le juste prix a été arrêté !")
        print(f'{ctx.author} stop juste prix')

    @commands.command(aliases=["jp"])
    @commands.cooldown(1,5)
    async def justeprix(self, ctx, prix=None):
        with open ("jp.json", "r") as f:
            data = json.load(f)
            nb = int(data["prix"])
            launched = data["launched"]
        
        if launched == "no":
            embed = discord.Embed(title="Juste prix", description="Le juste prix n'a pas commencé !", color=discord.Color.from_rgb(197,197,197))
            await ctx.send(embed=embed)
        
        elif launched == "yes":        
            if prix == None:
                await ctx.send("Vous devez entrer quelque chose.")
            else:
                if not prix.isdigit():
                    return
                prix = int(prix)
                user = ctx.message.author
                
                if prix < 1000:
                    prix = f"**{user.mention}** {prix} est Trop grand. Quel est le juste prix ? "
                
                elif prix > 2000:
                    prix = f"**{user.mention}** {prix} est Trop petit. Quel est le juste prix ? "
                
                elif prix > nb: #je vérifie si la réponse est plus grande que le nombre aléatoire
                
                    prix = f"**{user.mention}** {prix} est Trop grand. Quel est le juste prix ? "

                
                elif prix < nb: #je vérifie si la réponse est plus petite que le nombre aléatoire
                
                    prix = f"**{user.mention}** {prix} est Trop petit. Quel est le juste prix ? "

                
                elif prix == nb: #je vérifie si la réponse est égale au nombre aléatoire
                
                    prix = f"**{user.mention}** Bravo ! Le juste prix est bien {nb} bonbons !"
                    text = {
                        "prix": f"",
                        "launched": "no"}
                    with open("jp.json","w") as data:
                        json.dump(text,data)
                    await ctx.send(f'Le juste prix a été stoppé !')
                await ctx.send(prix)
                print(f'{ctx.author} played juste prix')
    
    @justeprix.error
    async def justeprix_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title="Juste prix", description="Vous devez attendre la fin du cooldown.", color=discord.Color.from_rgb(197,197,197))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(manage_roles=True, ban_members=True)
    async def defjp(self, ctx, prix):
        text = {
            "prix": f"{prix}"}
        with open("jp.json","w") as data:
            json.dump(text,data)
        await ctx.send(f'Le juste prix a été défini à {prix}')
        print(f'{ctx.author} setup justeprix')
        
    @defjp.error
    async def defjp_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Juste prix", description="Vous n'avez pas la permission.", color=discord.Color.from_rgb(197,197,197))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Justeprix(bot))
