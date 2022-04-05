import discord
from discord.ext import commands
from datetime import datetime
import json


class Confess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def confess(self, ctx, *, reason):
        await ctx.message.delete()
        date = datetime.now()
        day = date.day
        month = date.month
       
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
                
        if (day < 10):
            day = str(day)
            day = "0" + day
            
        if (month < 10):
            month = str(month)
            month = "0" + month
            
       
        embed = discord.Embed(title="Confession", description=f"{reason}", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.set_footer(text=f"confessé le {day}/{month}/{date.year} à {date.hour}:{date.minute}", icon_url="https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
       
       
        await ctx.send(embed=embed)
       

def setup(bot):
    bot.add_cog(Confess(bot))
