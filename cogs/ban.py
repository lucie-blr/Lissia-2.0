import discord
from discord.ext import commands
import json




class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open (f"data.json", "r") as t:
        data2 = json.load(t)
        servlist = data2["servlist"]


    @commands.slash_command(guild_ids = servlist, name = "ban", description = "command to ban people")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member = None, *, reason = None):
        print(member, 't')
        if member == None:
            await ctx.respond("Vous devez donner un utilisateur a debannir", ephemeral=True)
            return
        await member.ban(reason=reason)
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
        author = ctx.author
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            log = data["log"]
        serv = self.bot.get_channel(int(log))
        embed = discord.Embed(title="Ban", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.add_field(name="Modérateur", value=f"{author}", inline=True)
        embed.add_field(name="Membre", value=f"{member}", inline=True)
        embed.add_field(name="Reason", value=f"{reason}", inline=True)
        embed.set_author(name="Log")
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await serv.send(embed=embed)
        print(f'{ctx.author} used ban')
        embed = discord.Embed(title="Ban", description=f"**{member}** a été ban pour **{reason}**.", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.respond(embed=embed)  
    
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
            embed = discord.Embed(title="Ban", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.respond(embed=embed, ephemeral=True)

    @commands.slash_command(guild_ids = servlist, name = "unban", description = "command to unban people")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        
        if member == None:
            await ctx.respond("Vous devez donner un utilisateur a debannir", ephemeral=True)
        else:
            member_name, member_discriminator = member.split('#')

            
            
            for ban_entry in banned_users:
                user = ban_entry.user
                with open (f"data.json", "r") as t:
                    data2 = json.load(t)
                    color = data2["color"]
            
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    with open (f"./{ctx.guild.id}/data.json", "r") as f:
                        data = json.load(f)
                        log = data["log"]
                    serv = self.bot.get_channel(int(log))
                    author = ctx.author
                    embed = discord.Embed(title="Unban", color=discord.Color.from_rgb(color[0], color[1], color[2]))
                    embed.add_field(name="Modérateur", value=f"{author.mention}", inline=True)
                    embed.add_field(name="Membre", value=f"{member}", inline=True)
                    embed.set_author(name="Log")
                    embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
                    await serv.send(embed=embed)
                    embed = discord.Embed(title="Unban", description=f"**{user.name}#{user.discriminator}** a été débanni !", color=discord.Color.from_rgb(color[0], color[1], color[2]))
                    await ctx.respond(embed=embed)
                    return
        print(f'{ctx.author} used unban')
            
    @unban.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
            embed = discord.Embed(title="Unban", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
            await ctx.respond(embed=embed, ephemeral=True)
    
    @commands.slash_command(guild_ids = servlist, name = "banlist", description = "command to see people banned")
    @commands.has_permissions(ban_members = True)
    async def banlist(self, ctx):
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]

        bans = await ctx.guild.bans()
        embed = discord.Embed(color=discord.Color.from_rgb(color[0], color[1], color[2]), title = "**Liste des bans**", description = "Personnes bannie de ce serveur :")
        for ban in bans:
            embed.add_field(name = ban.user.name, value = ban.reason, inline = False)
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        print(f'{ctx.author} used banlist')
        await ctx.respond(embed = embed)
        
    
def setup(bot):
    bot.add_cog(Ban(bot))
