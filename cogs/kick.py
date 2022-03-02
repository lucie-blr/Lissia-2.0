import discord
from discord.ext import commands
import json



class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['kick', 'degagefdp'])
    @commands.has_permissions(manage_roles=True, ban_members=True)
    @commands.bot_has_permissions(manage_roles=True, ban_members=True)
    async def _kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embed = discord.Embed(title="Kick", description=f"**{member}** a été kick pour **{reason}**", color=discord.Color.from_rgb(17, 100, 20))
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.send(embed=embed)
        author = ctx.message.author
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            log = data["log"]
        serv = self.bot.get_channel(int(log))
        embed = discord.Embed(title="Kick", color=discord.Color.from_rgb(17, 100, 20))
        embed.add_field(name="Modérateur", value=f"{author.mention}", inline=True)
        embed.add_field(name="Membre", value=f"{member}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.set_author(name="Log")
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await serv.send(embed=embed)
        print(f'{ctx.author} used kick')


    @_kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Kick", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(17, 100, 20))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Kick(bot))