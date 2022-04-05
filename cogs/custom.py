import discord
from discord.ext import commands
import random
import json

class Custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open (f"data.json", "r") as t:
        data2 = json.load(t)
        servlist = data2["servlist"]


    @commands.command()
    async def rounard(self, ctx):
        if ctx.guild.name == 'UnOrdinary | La Guerre des Pouvoirs [RP/FR]':
            await ctx.send("<:UhFox:748272167455817888>")

    @commands.command()
    async def courgette(self, ctx, member : discord.Member):
        user = ctx.message.author
        embed = discord.Embed(title="Courgette", description=f'{user.mention} met sa grosse courgette à {member.mention}.', color=discord.Color.from_rgb(197,197,197))
        embed.set_image(url='https://img.cuisineaz.com/660x660/2017/02/06/i120484-courgettes-au-basilic.webp')
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.send(embed=embed)
        print(f'{ctx.author} used courgette')

    @commands.slash_command(guild_ids = servlist, name = "lovecalc", description = "command to calcul the love behind two people")
    async def lovecalc(self, ctx, personnage1, personnage2):
        love = random.randint(0, 100)
        if love < 20:
            embed = discord.Embed(title="Love calculator", description=f"Amour calculé : **{personnage1}** {love}%💖 **{personnage2}**", color=discord.Color.from_rgb(197,197,197))
            embed.add_field(name="Evaluation", value="Ne tentez rien, ils ne sortiront jamais ensemble !", inline=True)
        elif love < 40:
            embed = discord.Embed(title="Love calculator", description=f"Amour calculé : **{personnage1}** {love}%💖 **{personnage2}**", color=discord.Color.from_rgb(197,197,197))
            embed.add_field(name="Evaluation", value="Ce n'est pas fameux, mais quelque chose peut toujours apparaitre.", inline=True)
            
        elif love < 60:
            embed = discord.Embed(title="Love calculator", description=f"Amour calculé : **{personnage1}** {love}%💖 **{personnage2}**", color=discord.Color.from_rgb(197,197,197))
            embed.add_field(name="Evaluation", value="Il y a bien quelque chose ! Mais ce n'est pas l'amour fou.", inline=True) 
        elif love < 80:
            embed = discord.Embed(title="Love calculator", description=f"Amour calculé : **{personnage1}** {love}%💖 **{personnage2}**", color=discord.Color.from_rgb(197,197,197))
            embed.add_field(name="Evaluation", value="Ils s'aiment ou vont s'aimer ! C'est obligatoire !", inline=True) 
        elif love <= 100:
            embed = discord.Embed(title="Love calculator", description=f"Amour calculé : **{personnage1}** {love}%💖 **{personnage2}**", color=discord.Color.from_rgb(197,197,197))
            embed.add_field(name="Evaluation", value="Si ce n'est pas l'amour fou entre ces deux là, je ne vois pas ce que c'est !", inline=True) 
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        embed.set_thumbnail(url="https://assets.wprock.fr/emoji/joypixels/512/1f497.png")
        await ctx.respond(embed=embed)
        print(f'{ctx.author} used lovecalc')

def setup(bot):
    bot.add_cog(Custom(bot))
