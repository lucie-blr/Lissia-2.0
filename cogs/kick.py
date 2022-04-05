import discord
from discord.ext import commands
import json



class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    with open (f"data.json", "r") as t:
        data2 = json.load(t)
        servlist = data2["servlist"]


    @commands.slash_command(guild_ids = servlist, name = "kick", description = "command to kick people")
    @commands.has_permissions(manage_roles=True, ban_members=True)
    @commands.bot_has_permissions(manage_roles=True, ban_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
        if member == None:
            await ctx.respond("Vous devez mentionner un utilisateur à exclure.", ephemeral=True)
            return
        await member.kick(reason=reason)
        author = ctx.author
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            log = data["log"]
        serv = self.bot.get_channel(int(log))
        embed = discord.Embed(title="Kick", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.add_field(name="Modérateur", value=f"{author}", inline=True)
        embed.add_field(name="Membre", value=f"{member}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.set_author(name="Log")
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await serv.send(embed=embed)
        print(f'{ctx.author} used kick')
        embed = discord.Embed(title="Kick", description=f"**{member}** a été kick pour **{reason}**", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.respond(embed=embed)
        


    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
            embed = discord.Embed(title="Kick", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.respond(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Kick(bot))
