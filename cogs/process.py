import discord
from discord.ext import commands
import subprocess

class Process(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def processlist(self, ctx):
        subprocess.call('./generate_bot_list.sh')
        
        file = open('/var/www/html/bot/flo/botlist.txt','r')
        line = file.readline()
        while line:
            
            line.split('│')
            await ctx.send(line)
            # utilisez readline() pour lire la ligne suivante
            line = file.readline()
        file.close()
            

def setup(bot):
    bot.add_cog(Process(bot))
