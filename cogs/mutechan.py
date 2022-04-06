import discord
from discord.ext import commands
import json


class Mutechan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open (f"data.json", "r") as t:
        data2 = json.load(t)
        servlist = data2["servlist"]

    
    @commands.slash_command(guild_ids = servlist, name = "lock", description = "command to ban people")
    @commands.has_permissions(ban_members=True)
    async def lock(self, ctx, check:bool):
        if (check == True):
            perms = ctx.channel.overwrites_for(ctx.guild.default_role)
            perms.send_messages=False
            await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=perms)
            await ctx.respond("Channel vérouillé !")
        if (check == False):
            perms = ctx.channel.overwrites_for(ctx.guild.default_role)
            perms.send_messages=True
            await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=perms)
            await ctx.respond("Channel dévérouillé !")
        
def setup(bot):
    bot.add_cog(Mutechan(bot))
