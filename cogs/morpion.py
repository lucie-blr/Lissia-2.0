import discord
from discord.ext import commands
import asyncio
import json

def win(p):  
    
    w = [['1️⃣','2️⃣','3️⃣'],['4️⃣','5️⃣','6️⃣'],['7️⃣','8️⃣','9️⃣'],['7️⃣','4️⃣','1️⃣'],['8️⃣','5️⃣','2️⃣'],['9️⃣','6️⃣','3️⃣'],['1️⃣','5️⃣','9️⃣'],['7️⃣','5️⃣','3️⃣']]

    for l in w:
        
        check = set(l).issubset(set(p))
        if check:
            break     

    if check:
        
        return(True)

class Morpion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def morpion(self, ctx):  
        
        with open (f"./data.json", "r") as f:
            data = json.load(f)
            game = data["morpion"]
        
        if game == "True":
            await ctx.reply('Une partie est déjà en cours !')
            return
        
        case = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','❌']
        coord = [(-100,-50),(0,-50),(100,-50),(-100,50),(0,50),(100,50),(-100,150),(0,150),(100,150)]
        p1 = []
        p2 = []
        p1win = False
        p2win = False
        
        pwin = False
        
        emoji = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','❌']
        embed = discord.Embed(title="Morpion", description="Lancement de la partie...", color=discord.Color.from_rgb(17, 100, 20))
        msg = await ctx.reply(embed=embed)
        embed = discord.Embed(title="Morpion", description="Lancement de la partie...", color=discord.Color.from_rgb(17, 100, 20))
        embed.add_field(name="Jeu", value=f"``` {emoji[0]} | {emoji[1]} | {emoji[2]} \n ———-+-——-+-————\n {emoji[3]} | {emoji[4]} | {emoji[5]} \n ———-+-——-+-————\n {emoji[6]} | {emoji[7]} | {emoji[8]} ```", inline=False)
        await msg.edit(embed=embed)
        for moji in emoji:
            await msg.add_reaction(moji)
        
        def check(reaction, user):
            return str(reaction.emoji) in emoji

        embed = discord.Embed(title="Morpion", description="Partie en cours !", color=discord.Color.from_rgb(17, 100, 20))
        embed.add_field(name="Jeu", value=f"``` {emoji[0]} | {emoji[1]} | {emoji[2]} \n ———-+-——-+-————\n {emoji[3]} | {emoji[4]} | {emoji[5]} \n ———-+-——-+-————\n {emoji[6]} | {emoji[7]} | {emoji[8]} ```", inline=False)
        await msg.edit(embed=embed)
        
        while pwin != True:
            #p1 play
            
            data[f'morpion'] = "True"
        
            with open(f"./data.json","w") as t:
                json.dump(data,t)
            
                
            reaction = 't'
            embed = discord.Embed(title="Morpion", description="Partie en cours ! ⚪", color=discord.Color.from_rgb(17, 100, 20))
            embed.add_field(name="Jeu", value=f"``` {emoji[0]} | {emoji[1]} | {emoji[2]} \n ———-+-——-+-————\n {emoji[3]} | {emoji[4]} | {emoji[5]} \n ———-+-——-+-————\n {emoji[6]} | {emoji[7]} | {emoji[8]} ```", inline=False)
            await msg.edit(embed=embed)
        
            try:
                while not str(reaction) in case:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                break
            else:
                if str(reaction) == '❌':
                    pwin = False
                    break
                print(reaction,"morpion")
                del case[case.index(str(reaction))]
                emoji[emoji.index(str(reaction))] = '⚪'
                print(case)
                print(emoji)
                p1.append(str(reaction))
                embed = discord.Embed(title="Morpion", description="Partie en cours !", color=discord.Color.from_rgb(17, 100, 20))
                embed.add_field(name="Jeu", value=f"``` {emoji[0]} | {emoji[1]} | {emoji[2]} \n ———-+-——-+-————\n {emoji[3]} | {emoji[4]} | {emoji[5]} \n ———-+-——-+-————\n {emoji[6]} | {emoji[7]} | {emoji[8]} ```", inline=False)
                await msg.edit(embed=embed)
                if win(p1):
                    pwin = True
                    break
            
            embed = discord.Embed(title="Morpion", description="Partie en cours ! 🔴", color=discord.Color.from_rgb(17, 100, 20))
            embed.add_field(name="Jeu", value=f"``` {emoji[0]} | {emoji[1]} | {emoji[2]} \n ———-+-——-+-————\n {emoji[3]} | {emoji[4]} | {emoji[5]} \n ———-+-——-+-————\n {emoji[6]} | {emoji[7]} | {emoji[8]} ```", inline=False)
            await msg.edit(embed=embed)
        
            
            try:
                while not str(reaction) in case:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                break
            else:
                if str(reaction) == '❌':
                    pwin = False
                    break
                print(reaction,"morpion")
                del case[case.index(str(reaction))]
                emoji[emoji.index(str(reaction))] = '🔴'
                print(case)
                print(emoji)
                p2.append(str(reaction))
                embed = discord.Embed(title="Morpion", description="Partie en cours !", color=discord.Color.from_rgb(17, 100, 20))
                embed.add_field(name="Jeu", value=f"``` {emoji[0]} | {emoji[1]} | {emoji[2]} \n ———-+-——-+-————\n {emoji[3]} | {emoji[4]} | {emoji[5]} \n ———-+-——-+-————\n {emoji[6]} | {emoji[7]} | {emoji[8]} ```", inline=False)
                await msg.edit(embed=embed)
                if win(p2):
                    pwin = True
                    break
            
            if len(case) == 1:
                pwin = False
                break 
    
        if pwin == True:
            embed = discord.Embed(title="Morpion", description=f"{user} a gagné !", color=discord.Color.from_rgb(17, 100, 20))
            embed.add_field(name="Jeu", value=f"``` {emoji[0]} | {emoji[1]} | {emoji[2]} \n ———-+-——-+-————\n {emoji[3]} | {emoji[4]} | {emoji[5]} \n ———-+-——-+-————\n {emoji[6]} | {emoji[7]} | {emoji[8]} ```", inline=False)
            embed.set_thumbnail(url=f"{user.avatar_url}")
            await msg.edit(embed=embed)
            data[f'morpion'] = "False"
        
            with open(f"./data.json","w") as t:
                json.dump(data,t)
            
        else:
            embed = discord.Embed(title="Morpion", description="Personne n'a gagné !", color=discord.Color.from_rgb(17, 100, 20))
            embed.add_field(name="Jeu", value=f"``` {emoji[0]} | {emoji[1]} | {emoji[2]} \n ———-+-——-+-————\n {emoji[3]} | {emoji[4]} | {emoji[5]} \n ———-+-——-+-————\n {emoji[6]} | {emoji[7]} | {emoji[8]} ```", inline=False)
            await msg.edit(embed=embed)
            data[f'morpion'] = "False"
        
            with open(f"./data.json","w") as t:
                json.dump(data,t)
            
                
def setup(bot):
    bot.add_cog(Morpion(bot))
