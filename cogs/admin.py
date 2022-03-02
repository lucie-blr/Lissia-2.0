import discord
from discord.ext import commands
import json
import os

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["setlogchan"])
    @commands.has_permissions(manage_channels=True)
    async def setlogchannel(self, ctx, *, chan = None):
        if chan == None:
            await ctx.send("Vous devez envoyer un channel de log.")
            return
        
        characters="<#>"
        for x in range(len(characters)):
            chan = chan.replace(characters[x],"")
        
        text = {
            "log":f"{chan}"
        }
        
        guild = ctx.guild
        with open(f"./{ctx.guild.id}/data.json","w") as data:
            json.dump(text,data)
        
        embed = discord.Embed(title="Log", description=f"Le channel de log a été changé pour <#{chan}>", color=discord.Color.from_rgb(197,197,197))
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.send(embed=embed)
        serv = self.bot.get_channel(int(chan))
        await serv.send("Ce channel a été défini comme channel de log.")
    
    @commands.command()
    async def setup(self, ctx):
        with open (f"./data.json", "r") as f:
            data = json.load(f)
            servlist = data["servlist"]
        if ctx.guild.id in servlist:
            ctx.send("Le bot n'a pas besoin d'être setup.")
        elif ctx.guild.id not in servlist:
            os.mkdir(f'{ctx.guild.id}')
            text = {
                "log":""
            }
            with open(f"./{ctx.guild.id}/data.json","w") as data:
                json.dump(text,data)
            data.close
            with open(f"./{ctx.guild.id}/{ctx.guild.name}","w") as data:
                json.dump(text,data)
            await ctx.send("Bot setup")           
    
    @commands.command()
    async def iconlink(self,ctx):
        await ctx.send(f"{discord.Guild.icon_url}")
    
    @commands.command()
    async def serverid(self, ctx):
        await ctx.send(f"{ctx.guild.id}")



        
    

def setup(bot):
    bot.add_cog(Admin(bot))
