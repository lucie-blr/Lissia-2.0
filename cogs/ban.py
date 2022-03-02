import discord
from discord.ext import commands
import json




class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ban','viredela'])
    @commands.has_permissions(ban_members=True)
    async def _ban(self, ctx, member : discord.Member = None, *, reason = None):
        print(member, 't')
        if member == None:
            await ctx.send("Vous devez donner un utilisateur a debannir")
            return
        await member.ban(reason=reason)
        embed = discord.Embed(title="Ban", description=f"**{member}** a été ban pour **{reason}**.", color=discord.Color.from_rgb(197,197,197))
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.send(embed=embed)  
        author = ctx.message.author
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            log = data["log"]
        serv = self.bot.get_channel(int(log))
        embed = discord.Embed(title="Ban", color=discord.Color.from_rgb(197,197,197))
        embed.add_field(name="Modérateur", value=f"{author.mention}", inline=True)
        embed.add_field(name="Membre", value=f"{member}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.set_author(name="Log")
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await serv.send(embed=embed)
        print(f'{ctx.author} used ban')
    
    @_ban.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Ban", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(197,197,197))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.send(embed=embed)

    @commands.command(aliases=["unban"])
    @commands.has_permissions(ban_members=True)
    async def _unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        
        if member == None:
            await ctx.send("Vous devez donner un utilisateur a debannir")
        else:
            member_name, member_discriminator = member.split('#')

            
            
            for ban_entry in banned_users:
                user = ban_entry.user
            
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    embed = discord.Embed(title="Unban", description=f"**{user.name}#{user.discriminator}** a été débanni !", color=0x00ff00)
                    await ctx.send(embed=embed)
                    with open (f"./{ctx.guild.id}/data.json", "r") as f:
                        data = json.load(f)
                        log = data["log"]
                    serv = self.bot.get_channel(int(log))
                    author = ctx.message.author
                    embed = discord.Embed(title="Unban", color=discord.Color.from_rgb(197,197,197))
                    embed.add_field(name="Modérateur", value=f"{author.mention}", inline=True)
                    embed.add_field(name="Membre", value=f"{member}", inline=True)
                    embed.set_author(name="Log")
                    embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
                    await serv.send(embed=embed)
                    return
        print(f'{ctx.author} used unban')
            
    @_unban.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Unban", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(197,197,197))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def banlist(self, ctx):

        bans = await ctx.guild.bans()
        embed = discord.Embed(color=discord.Color.from_rgb(197,197,197), title = "**Liste des bans**", description = "Personnes bannie de ce serveur :")
        for ban in bans:
            embed.add_field(name = ban.user.name, value = ban.reason, inline = False)
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.send(embed = embed)
        print(f'{ctx.author} used banlist')
    
def setup(bot):
    bot.add_cog(Ban(bot))
