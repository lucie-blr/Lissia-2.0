import discord
import json
from discord.ext import commands
import os

with open ("data.json", "r") as f:
    data = json.load(f)
    token = data["Token"]
    prefix = data["Prefix"]

client = commands.Bot(command_prefix=prefix)

#Launch

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'{prefix}help | Vroum vroum'))
    print(f"Logged in as {client.user}")
    data[f'morpion'] = "False"
        
    with open(f"./data.json","w") as t:
        json.dump(data,t)

#Load

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
@commands.has_permissions(ban_members=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} command loaded.')
    print(f'{ctx.author} used load')

@load.error
async def load_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Load", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(17, 100, 20))
        await ctx.send(embed=embed)
        
@client.command()
@commands.has_permissions(ban_members=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} command unloaded.')
    print(f'{ctx.author} used unload')

@unload.error
async def unload_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Unload", description="Vous n'avez pas la permission d'éxecuter cette commande.", color=discord.Color.from_rgb(17, 100, 20))
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def reload(ctx, extension):
    if extension == "all":
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.unload_extension(f'cogs.{filename[:-3]}')
                await ctx.send(f'{filename[:-3]} unloaded')
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
                await ctx.send(f'{filename[:-3]} reloaded')
        print(f"{ctx.author} used reload all")
        await ctx.send("Toutes les commandes ont été reload.")
        
    else:
        print(f'{ctx.author} used reload')
        client.unload_extension(f'cogs.{    extension}')
        await ctx.send(f'{extension} command unloaded.')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'{extension} command reloaded.')
        print(f'{ctx.author} used reload')

#message automatique TICKET
@client.event
async def on_guild_channel_create(chan): 
    with open (f"./{chan.guild.id}/data.json", "r") as f:
        data = json.load(f)
        ticketlist = data["ticketlist"]
    if not str(chan) in ticketlist:
        if "ticket" in str(chan):
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
            await chan.send(embed=embed)
    else:
        await chan.send('Ce numéro de ticket est déjà en vérification.')
        
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

@client.command()
async def setprefix(ctx, prefix):
    with open (f"./data.json", "r") as f:
        data = json.load(f)
    data["Prefix"] = f"{prefix}"
    with open (f"./data.json", "w") as t:
        json.dump(data, t)
    await ctx.send(f'Prefix définie sur {prefix} au prochain redémarrage')

class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        embed = discord.Embed(title="Help", description="Toutes les commandes du client discord", color=0x992d22)
        embed.add_field(name=f"{prefix}help", value="Affiche ce message.", inline=True)
        await destination.send(embed=embed)
client.help_command = NewHelpName()

client.run(token)