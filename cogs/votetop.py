import discord
from discord.ext import commands
import json


class Votetop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def votetop(self, ctx):
        embed = discord.Embed(title="Top vote", description="Liste des meilleurs voteurs !", color=discord.Color.from_rgb(17, 100, 20))
        with open (f"./votetop.json", "r") as f:
            data = json.load(f)
            register = data["register"]
            
        listvote = []
        
        for user in register:
            user = data[f"{user}"]
            nbvote = int(user.get("vote"))
            listvote.append(nbvote)
        
        listvote.sort(reverse=True)
        
        classement = 1
        
        for nbvote in listvote:
            for userl in register:
                user = data[f"{userl}"]
               
                if int(user.get("vote")) == nbvote:
                    register.remove(f"{userl}")
                    username = user.get("user")
                    nbvote = user.get("vote")
                    embed.add_field(name=f"{classement}. {username}", value=f"Nombre de vote : **{nbvote}**", inline=False)
                    classement = classement + 1
        
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")    
        await ctx.send(embed=embed)

    @commands.command()
    async def vote(self, ctx):
        print(f"{ctx.author}")
        embed = discord.Embed(title="Vote Search", description="Votre nombre de vote.", color=discord.Color.from_rgb(17, 100, 20))
        with open (f"./votetop.json", "r") as f:
            data = json.load(f)
            register = data["register"]
                
        print(register)
        
        if str(ctx.author) in register:
            user = data[f"{ctx.author}"]
            username = user.get("user")
            nbvote = user.get("vote") 
            embed.add_field(name=f"{username}", value=f"Nombre de vote : **{nbvote}**", inline=False)

            
        else:
            embed.add_field(name=f"{ctx.author}", value="Vous n'avez pas encore voté !", inline=True)

        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")    
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def votereset(ctx):
        with open (f"./votetop.json", "r") as f:
            data = json.load(f)
            register = data["register"]
            
        for user in register:
            
            data[f"{user}"] = {"user":f"{user}", "vote":"0"}
            with open (f"./votetop.json", "w") as t:
                json.dump(data, t)
                
        await ctx.send("Compteur de vote reset !")

      
                
    @commands.command(aliases=["bt"])
    async def bumptop(self, ctx):
        embed = discord.Embed(title="Top bump", description="Liste des meilleurs bumpeurs !", color=discord.Color.from_rgb(17, 100, 20))
        with open (f"./bumptop.json", "r") as f:
            data = json.load(f)
            register = data["register"]
            
        listbump = []
        
        for user in register:
            user = data[f"{user}"]
            nbbump = int(user.get("bump"))
            listbump.append(nbbump)
        
        listbump.sort(reverse=True)
        
        classement = 1
        
        for nbbump in listbump:
            for user in register:
                user = data[f"{user}"]
                if int(user.get("bump")) == nbbump:
                    username = user.get("user")
                    nbbump = user.get("bump")
                    embed.add_field(name=f"{classement}. {username}", value=f"Nombre de bump : **{nbbump}**", inline=False)
                    classement = classement + 1
        
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")    
        await ctx.send(embed=embed)
        
    @commands.command()
    async def bump(self, ctx):
        print(f"{ctx.author}")
        embed = discord.Embed(title="bump Search", description="Votre nombre de bump.", color=discord.Color.from_rgb(17, 100, 20))
        with open (f"./bumptop.json", "r") as f:
            data = json.load(f)
            register = data["register"]
                
        print(register)
        
        if str(ctx.author) in register:
            user = data[f"{ctx.author}"]
            username = user.get("user")
            nbbump = user.get("bump") 
            embed.add_field(name=f"{username}", value=f"Nombre de bump : **{nbbump}**", inline=False)

            
        else:
            embed.add_field(name=f"{ctx.author}", value="Vous n'avez pas encore voté !", inline=True)

        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")    
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def bumpreset(self, ctx):
        with open (f"./bumptop.json", "r") as f:
            data = json.load(f)
            register = data["register"]
            
        for user in register:
            
            data[f"{user}"] = {"user":f"{user}", "bump":"0"}
            with open (f"./bumptop.json", "w") as t:
                json.dump(data, t)
        
        await ctx.send("Compteur de bump reset !")


def setup(bot):
    bot.add_cog(Votetop(bot))

