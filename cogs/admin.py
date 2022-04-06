import discord
from discord.ext import commands
import json
import os

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open (f"data.json", "r") as t:
        data2 = json.load(t)
        servlist = data2["servlist"]

    @commands.slash_command(guild_ids = servlist, name = "setlogchan", description = "channel")
    @commands.has_permissions(manage_channels=True)
    async def setlogchannel(self, ctx, *, chan = None):
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
        if chan == None:
            await ctx.respond("Vous devez envoyer un channel de log.", ephemeral=True)
            
        
        characters="<#>"
        for x in range(len(characters)):
            chan = chan.replace(characters[x],"")
        
        text = {
            "log":f"{chan}"
        }
        
    
        
        with open(f"./{ctx.guild.id}/data.json","w") as data:
            json.dump(text,data)
        
        embed = discord.Embed(title="Log", description=f"Le channel de log a été changé pour <#{chan}>", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.respond(embed=embed)
        serv = self.bot.get_channel(int(chan))
        await serv.send("Ce channel a été défini comme channel de log.")
    
    @commands.slash_command(guild_ids = servlist, name = "setup", description = "command for setup the bot")
    async def setup(self, ctx):
        
        os.mkdir(f'{ctx.guild.id}')
        text = {
            "log":"",
            "confess":{}
        }
        with open(f"./{ctx.guild.id}/data.json","w") as data:
            json.dump(text,data)
        data.close
        with open(f"./{ctx.guild.id}/{ctx.guild.name}","w") as data:
            json.dump(text,data)
        await ctx.respond("Bot setup")           

    @commands.command()
    async def serverid(self, ctx):
        await ctx.respond(f"{ctx.guild.id}")
        
    @commands.command()
    async def leaveserver(self,ctx):
        to_leave = self.bot.get_guild(ctx.guild.id)
        await to_leave.leave()

def setup(bot):
    bot.add_cog(Admin(bot))
