import discord
from discord.ext import commands
import json



class Autorole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction, user, reaction.message.channel.id, reaction.message.id)
        with open(f"data.json","r") as data:
            data = json.load(data)
            chanrules = data["chanrules"]
            msgrules = data["msgrules"]
        
        if str(reaction.message.channel.id) in chanrules:
            if str(reaction.message.id) in msgrules:
                if reaction.emoji == "✅":
                    role = discord.utils.get(user.guild.roles, name="✅ • Règlement validé")
                    await user.add_roles(role) #add the role
                    print(f'Add the role ✅ • Règlement validé to {user}')
     
    @commands.command()
    async def autorole(self, ctx, *, reason = None):
        
        if reason == None:
            await ctx.send("Vous devez donner le nom d'un serveur.")  
        elif reason == "FRIENDS":
            embed = discord.Embed(title="Reaction Role", description="Si vous souhaitez accéder à certains channels communautaires, il vous faut réagir avec la réaction qui va avec le channel !", color=discord.Color.from_rgb(197,197,197))
            embed.add_field(name="💻 → Informatique", value="Pour les passionnés d'informatique et de jeu vidéo !", inline=False)
            embed.add_field(name="👺 → Fan du Japon", value="Si vous voulez discuter de manga, de culture japonaise, et autre, c'est ici !", inline=False)
            embed.add_field(name="🎵 → Musique", value="Même ici il y a des passionnés de musique, et vous pouvez en discuter pleinement !", inline=False)
            embed.add_field(name="💩 → Shitpost", value="Pour spam, envoyer n'importe quoi ou dire des bêtises, rendez-vous là !", inline=False)
            embed.add_field(name="🔞 → NSFW", value="Ai-je vraiment besoin de décrire ce channel ?", inline=False)
            embed.add_field(name="🤣 → Humour", value="Il y a des humoristes partout, même quand ils ne sont pas drôles !", inline=False)
            embed.add_field(name="📚 → Travail", value="Pour tous les gens souhaitant travailler, c'est par ici !", inline=False)
            embed.set_image(url="https://images-ext-1.discordapp.net/external/lAQa4Kce7-MvlJoZX0KMlq2rekinA1LpMVdHfpdOWRo/https/i.pinimg.com/originals/76/b4/64/76b4645640120014ba9c4fb26dbd40fd.gif")
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        
            msg = await ctx.send(embed=embed)
            
            await msg.add_reaction("💻")
            await msg.add_reaction("👺")
            await msg.add_reaction("🎵")
            await msg.add_reaction("💩")
            await msg.add_reaction("🔞")
            await msg.add_reaction("🤣")
            await msg.add_reaction("📚")
            
            
            



def setup(bot):
    bot.add_cog(Autorole(bot))
