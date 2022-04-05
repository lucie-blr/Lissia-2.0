import discord
from discord.ext import commands
import json

class Report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def report(self, ctx, *, reason):
        
        with open (f"./report.json", "r") as f:
            data = json.load(f)
            register = data["register"]
            
        if not str(ctx.author) in register:
            data.get("register", {}).append(str(ctx.author))
            data[f"{ctx.author}"] = [reason]
            with open (f"./report.json", "w") as t:
                json.dump(data, t)
        else:
            data.get(f"{ctx.author}", {}).append(reason)
            with open (f"./report.json", "w") as t:
                json.dump(data, t)
            
        await ctx.reply("Report réalisé avec succès !")
        
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def reportlist(self, ctx):
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
        with open (f"./report.json", "r") as f:
            
            data = json.load(f)
            register = data["register"]
        
        embed = discord.Embed(title="Report list", description="Liste de tous les reports", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        classement = 1

        for userl in register:
            with open (f"./report.json", "r") as f:
                data = json.load(f)
                user = data[f"{userl}"]  

            for report in user:
                print(report)
                embed.add_field(name=f"{classement}. {userl}", value=f"report : **{report}**", inline=False)
                classement = classement + 1



        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Report(bot))
