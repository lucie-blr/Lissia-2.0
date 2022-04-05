import discord
from discord.ext import commands
from datetime import datetime
import json


class Confess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    guildid = [887675595419451396]

    @commands.slash_command(guild_ids = guildid, name = "confess", description = "confession")
    async def confess(self, ctx, *, reason):
        date = datetime.now()
        day = date.day
        month = date.month
        hour = date.hour
        minute = date.minute
       
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
                
        with open (f"./{ctx.guild.id}/data.json", "r") as d:
            data = json.load(d)
            confess = data["confess"]
                
        if (day < 10):
            day = str(day)
            day = "0" + day
            
        if (month < 10):
            month = str(month)
            month = "0" + month
            
        if (hour < 10):
            hour = str(hour)
            hour = "0" + hour
            
        if (minute < 10):
            minute = str(minute)
            minute = "0" + minute
            
       
        embed = discord.Embed(title="Confession", description=f"{reason}", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.set_footer(text=f"confessé le {day}/{month}/{date.year} à {hour}:{minute}", icon_url="https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
       
       
        msg = await ctx.send(embed=embed)
        
        
        msgid = {
            "idmsg":f"{msg.id}",
            "chanid":f"{ctx.channel.id}",
            "guildid":f"{ctx.guild.id}",
            "authorid":f"{ctx.author.id}",
            "date":f"{date}",
            "message":f"{reason}"
            
        }
        
        confess[f"{msg.id}"] = msgid
        
        with open (f"./{ctx.guild.id}/data.json", "w") as t:
            json.dump(data, t)
        
        await ctx.respond("Confession envoyé !", ephemeral=True)
        
    
    @commands.command()
    async def foundconfess(self, ctx, id):
        with open (f"data.json", "r") as t:
            data2 = json.load(t)
            color = data2["color"]
                
        with open (f"./{ctx.guild.id}/data.json", "r") as d:
            data = json.load(d)
            confess = data["confess"]
        
        try:
            conf = confess[f"{id}"]
            
            msg = conf["message"]
            
            aid = conf["authorid"]
            cid = conf["chanid"]
            gid = conf["guildid"]
            mid = conf["idmsg"]
            date = conf["date"]
            
            
            
            embed = discord.Embed(title=f"Confession", description=f"\"{msg}\"", color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed.add_field(name=f"Author", value=f"<@{aid}>", inline=False)
            embed.add_field(name="Channel", value=f"<#{cid}>", inline=False)
            embed.add_field(name="date", value=f"{date}", inline=False)
            embed.add_field(name="Lien du message", value=f"[lien du message](https://discord.com/channels/{gid}/{cid}/{mid})", inline=False)
            
            
            await ctx.send(embed=embed)
            
        except TypeError:
            await ctx.send("prout")
       

def setup(bot):
    bot.add_cog(Confess(bot))
