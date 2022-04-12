import discord
import json
from discord.ext import commands
import os

with open ("data.json", "r") as f:
    data = json.load(f)
    token = data["Token"]
    prefix = data["Prefix"]
    servlist = data["servlist"]

client = commands.Bot(command_prefix=prefix)

#Launch

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'{prefix}help | Vroum vroum'))
    print(f"Logged in as {client.user}")
    data[f'morpion'] = "False"
    glist = []
    
    for guild in client.guilds:
        glist.append(guild.id)
        print(guild.name)
    
    data["servlist"] = glist
        
    with open(f"./data.json","w") as t:
        json.dump(data,t)

#Load

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        

@client.slash_command(guild_ids = servlist, name = "load", description = "command to load others command")   
@commands.has_permissions(ban_members=True)
async def load(ctx, command):
    client.load_extension(f'cogs.{command}')
    await ctx.respond(f'{command} command loaded.', ephemeral=True)
    print(f'{ctx.author} used load')

@load.error
async def load_error(ctx, error):
    with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Load", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        await ctx.respond(embed=embed, ephemeral=True)
        
@client.slash_command(guild_ids = servlist, name = "unload", description = "command to unload others command")   
@commands.has_permissions(ban_members=True)
async def unload(ctx, command):
    client.unload_extension(f'cogs.{command}')
    await ctx.respond(f'{command} command unloaded.', ephemeral=True)
    print(f'{ctx.author} used unload')

@unload.error
async def unload_error(ctx, error):
    with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Unload", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        await ctx.respond(embed=embed, ephemeral=True)


@client.slash_command(guild_ids = servlist, name = "reload", description = "command to reload others command")   
@commands.has_permissions(ban_members=True)
async def reload(ctx, extension):
    with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
    if extension == "all":
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.unload_extension(f'cogs.{filename[:-3]}')
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
        print(f"{ctx.author} used reload all")
        await ctx.respond("Toutes les commandes ont été reload.", ephemeral=True)
        
    else:
        print(f'{ctx.author} used reload')
        client.unload_extension(f'cogs.{    extension}')
        await ctx.respond(f'{extension} command unloaded.', ephemeral=True)
        client.load_extension(f'cogs.{extension}')
        await ctx.respond(f'{extension} command reloaded.', ephemeral=True)
        print(f'{ctx.author} used reload')


    

#message automatique TICKET
@client.event
async def on_guild_channel_create(chan): 
    with open (f"./{chan.guild.id}/data.json", "r") as f:
        data = json.load(f)
        ticketlist = data["ticketlist"]
    if not str(chan) in ticketlist:
        with open (f"data.json", "r") as t:
            data2 = json.load(t)
            color = data2["color"]
        with open (f"./{chan.guild.id}/data.json", "r") as t:
            data3 = json.load(t)
            ticketmsg = data3["ticketmsg"]
        if chan.guild.id == "961006436555571250":
            if "ticket" in str(chan):
                data.get("ticketlist", {}).append(str(chan))
                data[f"{chan}"] = {"chanid":f"{chan.id}", "verif":"1"}
                with open (f"./{chan.guild.id}/data.json", "w") as t:
                    json.dump(data, t)  
                embed = discord.Embed(title="Ticket", description="Hello !\n\nJe viens t'aider afin de vérifier que tu as bien respecté quelques points dans ta fiche avant que les staffiens viennent corriger ta fiche. Lis bien jusqu'au bout, et n'oublie pas d'envoyer ta fiche en Gdoc <:Owiiii:920291924626264125>", color=discord.Color.from_rgb(color[0], color[1], color[2]))
                embed.add_field(name="Mise en page", value="✓ Toutes les catégories doivent être présentent et dans le bon ordre\n✓ Les titres doivent être visible (soulignés, en gras, comme vous voulez du moment qu'ils sont apparents !)", inline=False)
                embed.add_field(name="Identité", value="✓ Le prénom ne doit pas déjà être pris par quelqu'un\n✓ L'âge minimum est de 14 ans sur le RP\n✓ Vérifie que le rôle que tu souhaites est disponible dans <#842659580944711692> / <#748139611867578368>", inline=False)
                embed.add_field(name="Personnalité", value="✓ Développe bien le caractère\n✓ Détester n'est pas avoir peur, la phobie doit en être une !", inline=False)
                embed.add_field(name="Physique", value="✓ Développe bien le physique\n✓ Les qualités / défauts doivent être équilibrés (autant de l'un que de l'autre) et en liste de course", inline=False)
                embed.add_field(name="Capacité", value="✓ La capacité ne doit pas déjà être dans <#748216694442557471>\n✓ Décris la bien avec les limites (temps, rayon, personnes influencées...)\n✓ N'oublie pas de mettre la maîtrise sur 10 !", inline=False)
                embed.add_field(name="Relationnel", value="✓ N'oublie pas le nom et prénom des parents", inline=False)
                embed.add_field(name="Ensuite ?", value="*Après avoir vérifié tout ça, tu pourras faire juste en-dessous **&good** ! Nous viendrons corriger un peu après. Merci d\'avance~*", inline=False)
                await chan.send(embed=embed)
            else:
                await chan.send('Ce numéro de ticket est déjà en vérification.')
        else:
            if "ticket" in str(chan):
                data.get("ticketlist", {}).append(str(chan))
                data[f"{chan}"] = {"chanid":f"{chan.id}", "verif":"1"}
                with open (f"./{chan.guild.id}/data.json", "w") as t:
                    json.dump(data, t)
                embed = discord.Embed(title="Ticket", description=f"{ticketmsg}", color=discord.Color.from_rgb(color[0], color[1], color[2]))
                await chan.send(embed=embed)
        
@client.event
async def on_guild_channel_delete(chan):
    with open (f"./{chan.guild.id}/data.json", "r") as f:
        data = json.load(f)
        ticketlist = data["ticketlist"]
    if str(chan) in ticketlist:
        data.get("ticketlist",{}).remove(str(chan))
        data[f"{chan}"] = {"verif":"close"}
        with open (f"./{chan.guild.id}/data.json", "w") as t:
            json.dump(data, t) 


#commands

class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
        destination = self.get_destination()
        embed = discord.Embed(title="Help", description="Toutes les commandes du client discord", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.add_field(name=f"{prefix}help", value="Affiche ce message.", inline=True)
        embed.add_field(name=f"{prefix}ban @membre", value="Banni un utilisateur du serveur.", inline=True)
        embed.add_field(name=f"{prefix}unban membre#0000", value="DÃ©banni un utilisateur du serveur.", inline=True)
        embed.add_field(name=f"{prefix}kick @membre", value="Exclu un membre du serveur.", inline=True)
        embed.add_field(name=f"{prefix}mute @membre", value="EmpÃªche un membre de parler.", inline=True)
        embed.add_field(name=f"{prefix}timeout @membre t", value="timeout un membre (t = temps en heure).", inline=True)
        embed.add_field(name=f"{prefix}clear nb", value="Supprime un certain nombre de message (nb = nombres de message à clear, 10 de base).", inline=True)
        embed.add_field(name=f"{prefix}courgette @membre", value="Courgette quelqu'un.", inline=True)
        embed.add_field(name=f"{prefix}catalogue personnage", value="Obtenir la fiche d'un personnage important.", inline=True)
        embed.add_field(name=f"{prefix}topvote", value="Donne la liste des meilleurs voteurs !", inline=True)
        embed.add_field(name=f"{prefix}vote (@membre)", value="Donne son nombre de vote.", inline=True)
        await destination.send(embed=embed)

client.help_command = NewHelpName()

@client.slash_command(guild_ids = servlist, name = "help", description = "help command")   
async def help(ctx):
    with open (f"data.json", "r") as t:
            data2 = json.load(t)
            color = data2["color"]
    prefix = "/"
    embed = discord.Embed(title="Help", description="Toutes les commandes du client discord", color=discord.Color.from_rgb(color[0], color[1], color[2]))
    embed.add_field(name=f"{prefix}help", value="Affiche ce message.", inline=True)
    embed.add_field(name=f"{prefix}ban @membre", value="Banni un utilisateur du serveur.", inline=True)
    embed.add_field(name=f"{prefix}unban membre#0000", value="Débanni un utilisateur du serveur.", inline=True)
    embed.add_field(name=f"{prefix}kick @membre", value="Exclu un membre du serveur.", inline=True)
    embed.add_field(name=f"{prefix}mute @membre", value="Empèche un membre de parler.", inline=True)
    embed.add_field(name=f"{prefix}timeout @membre t", value="timeout un membre (t = temps en heure).", inline=True)
    embed.add_field(name=f"{prefix}clear nb", value="Supprime un certain nombre de message (nb = nombres de message à clear, 10 de base).", inline=True)
    embed.add_field(name=f"{prefix}courgette @membre", value="Courgette quelqu'un.", inline=True)
    embed.add_field(name=f"{prefix}catalogue personnage", value="Obtenir la fiche d'un personnage important.", inline=True)
    embed.add_field(name=f"{prefix}catalogue_add", value="Ajouter un personnage dans le catalogue.", inline=True)
    embed.add_field(name=f"{prefix}catalogue_delete", value="Supprimer un personnage du catalogue.", inline=True)
    embed.add_field(name=f"{prefix}confess confession", value="Permet de se confesser anonymement.", inline=True)
    embed.add_field(name=f"{prefix}foundconfess messageid", value="Permet de savoir qui a envoyé une confession.", inline=True)
    
    await ctx.respond(embed=embed, ephemeral=True)



    

client.run(token)