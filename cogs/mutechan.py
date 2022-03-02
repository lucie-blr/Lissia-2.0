import discord
from discord.ext import commands
import json


class Mutechan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["mutechannel"])
    @commands.has_permissions(manage_roles=True)
    async def mutechan(self, ctx, *, reason=None):
        permission = discord.Permissions()
        permission.update()
        var = discord.utils.get(ctx.guild.roles, name = "Membres")
        await ctx.channel.set_permissions(var, send_messages=False, view_channel=True)
        chan = self.bot.get_channel(ctx.channel.id)
        embed = discord.Embed(title="Mute Channel", description=f"le salon a été mute pour {reason}", color=discord.Color.from_rgb(197,197,197))
        await ctx.send(embed=embed)
        author = ctx.message.author
        embed = discord.Embed(title="Mute Channel", description=f"{chan} a été mute par **{author.mention}** pour **{reason}**.", color=discord.Color.from_rgb(197,197,197))
        embed.set_author(name="Log")
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            log = data["log"]
        serv = self.bot.get_channel(int(log))
        await serv.send(embed=embed)
        print(f'{ctx.author} used mutechan')

    @mutechan.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Mute channel", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(197,197,197))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.send(embed=embed)
    
    @commands.command(aliases=["unmutechannel"])
    @commands.has_permissions(manage_roles=True)
    async def unmutechan(self, ctx, *, reason=None):
        var = discord.utils.get(ctx.guild.roles, name = "Membres")
        await ctx.channel.set_permissions(var, send_messages=True, view_channel=True)
        chan = self.bot.get_channel(ctx.channel.id)
        embed = discord.Embed(title="Unmute Channel", description=f"le salon a été mute pour {reason}", color=discord.Color.from_rgb(197,197,197))
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.send(embed=embed)
        author = ctx.message.author
        embed = discord.Embed(title="Unmute Channel", description=f"{chan} a été unmute par **{author.mention}** pour **{reason}**.", color=discord.Color.from_rgb(197,197,197))
        embed.set_author(name="Log")
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            log = data["log"]
        serv = self.bot.get_channel(int(log))
        await serv.send(embed=embed)
        print(f'{ctx.author} used mutechan')
        
    @unmutechan.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Unmute channel", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(197,197,197))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Mutechan(bot))
