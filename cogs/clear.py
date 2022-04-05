import discord
from discord.ext import commands
import asyncio
import json

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    with open (f"data.json", "r") as t:
        data2 = json.load(t)
        servlist = data2["servlist"]

    @commands.slash_command(guild_ids = servlist, name = "clear", description = "clear messages")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
        await ctx.channel.purge(limit=int(amount)+2)
        author = ctx.author
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            log = data["log"]
        serv = self.bot.get_channel(int(log))
        chan = self.bot.get_channel(ctx.channel.id)
        embed = discord.Embed(title="Clear", description=f"**{author.mention}** a utilisé la commande clear et a supprimé **{amount}** messages dans **{chan}**.", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.set_author(name="Log")
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await serv.send(embed=embed)
        print(f'{ctx.author} used clear')
        embed = discord.Embed(title="Clear", description=f"{amount} messages ont été supprimés !", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.respond(embed=embed, ephemeral=False, delete_after=10)

    @clear.error
    async def clear_error(self, ctx, error):
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Clear", description="Vous n'avez pas la permission d'exécuter cette permission", color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.respond(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Clear(bot))



