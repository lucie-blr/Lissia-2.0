import discord
from discord.ext import commands
import json



class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open (f"data.json", "r") as t:
        data2 = json.load(t)
        servlist = data2["servlist"]

    @commands.slash_command(guild_ids = servlist, name = "say", description = "command to make the bot talk")
    @commands.has_permissions(ban_members=True)
    async def say(self, ctx, *, message):
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
        if message == None:
            await ctx.respond("Vous devez entrer quelque chose.", ephemeral=True)
        else:
            await ctx.send(message)
            user = ctx.author
            print("t")
            with open (f"./{ctx.guild.id}/data.json", "r") as f:
                data = json.load(f)
                log = data["log"]
            serv = self.bot.get_channel(int(log))
            embed = discord.Embed(title="Say", color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed.add_field(name="Modérateur", value=f"{user.mention}", inline=True)
            embed.add_field(name="Message", value=f"{message}", inline=True)
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            embed.set_author(name="Log")
            
            await serv.send(embed=embed)
        print(f'{ctx.author} used say')
    @commands.command()
    async def test(self, ctx):
        await ctx.respond("test", ephemeral=True)

def setup(bot):
    bot.add_cog(Say(bot))
