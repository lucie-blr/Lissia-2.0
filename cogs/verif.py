import discord
from discord.ext import commands
import json

class Verif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def good(self, ctx):
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            ticketlist = data["ticketlist"]
        if not str(ctx.channel) in ticketlist:
            await ctx.reply('Vous devez utiliser cette commande dans un ticket.')
        elif str(ctx.channel) in ticketlist:
            ticket = data[f"{ctx.channel}"]
            step = ticket.get("verif")
            if step == '1':
                step = '2'
                data[f'{ctx.channel}'] = {"chanid":f"{ctx.channel.id}","verif":f"{step}"}
                with open (f"./{ctx.guild.id}/data.json", "w") as t:
                    json.dump(data, t)
                embed = discord.Embed(title="Ticket", description="Vérification passée avec succès !", color=discord.Color.from_rgb(17, 100, 20))
                await ctx.reply(embed=embed)
            else:
                return
    
    @commands.command()
    async def addverif(self, ctx):
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            ticketlist = data["ticketlist"]
        if str(ctx.channel) in ticketlist:
            await ctx.reply('Vous devez utiliser cette commande dans un ticket qui n\'est pas déjà en vérification.')
        else:
            chan = ctx.channel
            if "ticket" in str(chan):    
                if not str(chan) in ticketlist:
                    data.get("ticketlist", {}).append(str(chan))
                    data[f"{chan}"] = {"chanid":f"{chan.id}", "verif":"1"}
                    with open (f"./{chan.guild.id}/data.json", "w") as t:
                        json.dump(data, t)  
                    embed = discord.Embed(title="Ticket", description="Hello !\n\nJe viens t'aider afin de vérifier que tu as bien respecté quelques points dans ta fiche avant que les staffiens viennent corriger ta fiche. Lis bien jusqu'au bout, et n'oublie pas d'envoyer ta fiche en Gdoc <:Owiiii:920291924626264125>", color=discord.Color.from_rgb(17, 100, 20))
                    embed.add_field(name="Mise en page", value="✓ Toutes les catégories doivent être présentent et dans le bon ordre\n✓ Les titres doivent être visible (soulignés, en gras, comme vous voulez du moment qu'ils sont apparents !)", inline=False)
                    embed.add_field(name="Identité", value="✓ Le prénom ne doit pas déjà être pris par quelqu'un\n✓ L'âge minimum est de 14 ans sur le RP\n✓ Vérifie que le rôle que tu souhaites est disponible dans <#842659580944711692> / <#748139611867578368>", inline=False)
                    embed.add_field(name="Personnalité", value="✓ Développe bien le caractère\n✓ Détester n'est pas avoir peur, la phobie doit en être une !", inline=False)
                    embed.add_field(name="Physique", value="✓ Développe bien le physique\n✓ Les qualités / défauts doivent être équilibrés (autant de l'un que de l'autre) et en liste de course", inline=False)
                    embed.add_field(name="Capacité", value="✓ La capacité ne doit pas déjà être dans <#748216694442557471>\n✓ Décris la bien avec les limites (temps, rayon, personnes influencées...)\n✓ N'oublie pas de mettre la maîtrise sur 10 !", inline=False)
                    embed.add_field(name="Relationnel", value="✓ N'oublie pas le nom et prénom des parents", inline=False)
                    embed.add_field(name="Ensuite ?", value="*Après avoir vérifié tout ça, tu pourras faire juste en-dessous **&good** ! Nous viendrons corriger un peu après. Merci d\'avance~* <:LoveForYou:774967995205287976>", inline=False)
                    await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_role('∵🚔∴ Staffiens ∵🚔∴')
    async def verif(self, ctx, reason = None):
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            ticketlist = data["ticketlist"]
        if not str(ctx.channel) in ticketlist:
            await ctx.reply('Vous devez utiliser cette commande dans un ticket.')
        elif str(ctx.channel) in ticketlist:
            ticket = data[f"{ctx.channel}"]
            step = ticket.get("verif")
            if reason == 'back':
                if step == '1':
                    await ctx.reply('Vous ne pouvez pas revenir plus en arrière.')
                elif step == '2':
                    step = '1'
                    data[f'{ctx.channel}'] = {"chanid":f"{ctx.channel.id}","verif":f"{step}"}
                    with open (f"./{ctx.guild.id}/data.json", "w") as t:
                        json.dump(data, t)
                    embed = discord.Embed(title="Ticket", description="Retour en arrière passée avec succès !", color=discord.Color.from_rgb(17, 100, 20))
                    await ctx.reply(embed=embed)
                elif step == '3':
                    step = '2'
                    data[f'{ctx.channel}'] = {"chanid":f"{ctx.channel.id}","verif":f"{step}"}
                    with open (f"./{ctx.guild.id}/data.json", "w") as t:
                        json.dump(data, t)
                    embed = discord.Embed(title="Ticket", description="Retour en arrière passée avec succès !", color=discord.Color.from_rgb(17, 100, 20))
                    await ctx.reply(embed=embed)
                elif step == 'close':
                    step = '3'
                    data[f'{ctx.channel}'] = {"chanid":f"{ctx.channel.id}","verif":f"{step}"}
                    with open (f"./{ctx.guild.id}/data.json", "w") as t:
                        json.dump(data, t)
                    embed = discord.Embed(title="Ticket", description="Retour en arrière passée avec succès !", color=discord.Color.from_rgb(17, 100, 20))
                    await ctx.reply(embed=embed)
                return
            if step == '2':
                step = '3'
                data[f'{ctx.channel}'] = {"chanid":f"{ctx.channel.id}","verif":f"{step}"}
                with open (f"./{ctx.guild.id}/data.json", "w") as t:
                    json.dump(data, t)
                embed = discord.Embed(title="Ticket", description="Vérification passée avec succès !", color=discord.Color.from_rgb(17, 100, 20))
                await ctx.reply(embed=embed)
                return
            if step == '3':
                data[f'{ctx.channel}'] = {"chanid":f"{ctx.channel.id}","verif":f"close"}
                with open (f"./{ctx.guild.id}/data.json", "w") as t:
                    json.dump(data, t)
                embed = discord.Embed(title="Ticket", description="Vérification passée avec succès !", color=discord.Color.from_rgb(17, 100, 20))
                await ctx.reply(embed=embed)
                return          
                
    @commands.command()
    @commands.has_role('∵🚔∴ Staffiens ∵🚔∴')
    async def veriflist(self, ctx):
        embed = discord.Embed(title="Ticket list", description="Liste des tickets à vérifier !", color=discord.Color.from_rgb(17, 100, 20))
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            data = json.load(f)
            ticketlist = data["ticketlist"]
            
        for ticket in ticketlist:
            ticketname = ticket
            ticket = data[f"{ticket}"]
            
            if str(ticket.get("verif")) != 'close':
                ticketdir = ticket.get("chanid")
                verif = ticket.get("verif")
                embed.add_field(name=f"{ticketname}", value=f"<#{ticketdir}> Etape de vérification : **{verif}**", inline=False)
                
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")    
        await ctx.send(embed=embed)
                
def setup(bot):
    bot.add_cog(Verif(bot))
