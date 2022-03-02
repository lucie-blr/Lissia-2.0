import discord
from discord.ext import commands
import datetime
import json

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def timeout(self, ctx, member : discord.Member, hours : int, *, reason = None):
        
        if member == None:
            await ctx.reply("Vous devez mentionner un utilisateur à bannir.")
            return
        
        time = datetime.timedelta(hours=hours)
        
        await member.timeout_for(time)
        
        
        
        author = ctx.message.author
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            log = data["log"]
        serv = self.bot.get_channel(int(log))
        embed = discord.Embed(title="Timeout", color=discord.Color.from_rgb(197,197,197))
        embed.add_field(name="Modérateur", value=f"{author.mention}", inline=True)
        embed.add_field(name="Membre", value=f"{member}", inline=True)
        embed.add_field(name="Time", value=f"{time}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.set_author(name="Log")
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await serv.send(embed=embed)
        embed = discord.Embed(title="Timeout", description=f"{member} a bien été Timeout durant {time} pour {reason}")
        
        await ctx.reply(embed=embed)
        print(f'{ctx.author} used timeout')
        

def setup(bot):
    bot.add_cog(Mute(bot))
