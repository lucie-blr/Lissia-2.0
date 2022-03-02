import discord
from discord.ext import commands
import json



class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ################################RAJOUTER ID ROLE MUTE DANS LE DATA DU SERVER ET LE METTRE DANS LE CODE DU BOT############################""

    @commands.command(aliases=["mute"])
    @commands.has_permissions(manage_roles=True)
    async def _mute(self, ctx, *, member : discord.Member):
        mute = discord.utils.get(ctx.guild.roles, name = "Bâillonné [Cachot]")
        await member.add_roles(mute, atomic=True)
        embed = discord.Embed(title="Mute", description=f"{member.mention} a été mute", color=discord.Color.from_rgb(17, 100, 20))
        await ctx.send(embed=embed)
        author = ctx.message.author
        embed = discord.Embed(title="Mute", color=discord.Color.from_rgb(17, 100, 20))
        embed.add_field(name="Modérateur", value=f"{author.mention}", inline=True)
        embed.add_field(name="Membre", value=f"{member}", inline=True)
        embed.set_author(name="Log")
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            log = data["log"]
        serv = self.bot.get_channel(int(log))
        await serv.send(embed=embed)
        print(f'{ctx.author} used mute')

    @_mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Mute", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(17, 100, 20))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.send(embed=embed)
    
    @commands.command(aliases=["unmute"])
    @commands.has_permissions(manage_roles=True)
    async def _unmute(self, ctx, *, member : discord.Member):
        mute = discord.utils.get(ctx.guild.roles, name = "Bâillonné [Cachot]")
        await member.remove_roles(mute, atomic=True)
        embed = discord.Embed(title="Unmute", description=f"{member.mention} a été unmute", color=discord.Color.from_rgb(17, 100, 20))
        await ctx.send(embed=embed)
        author = ctx.message.author
        embed = discord.Embed(title="Unmute", color=discord.Color.from_rgb(17, 100, 20))
        embed.add_field(name="Modérateur", value=f"{author.mention}", inline=True)
        embed.add_field(name="Membre", value=f"{member}", inline=True)
        embed.set_author(name="Log")
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            log = data["log"]
        serv = self.bot.get_channel(int(log))
        await serv.send(embed=embed)
        print(f'{ctx.author} used unmute')
            
    @_unmute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Unmute", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(17, 100, 20))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Mute(bot))
