import discord
from discord.ext import commands
import json
import os

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open (f"data.json", "r") as t:
        data2 = json.load(t)
        servlist = data2["servlist"]

    @commands.slash_command(guild_ids = servlist, name = "setlogchan", description = "channel")
    @commands.has_permissions(manage_channels=True)
    async def setlogchannel(self, ctx, *, chan = None):
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
        
        if chan == None:
            await ctx.respond("Vous devez envoyer un channel de log.", ephemeral=True)
            
        
        characters="<#>"
        for x in range(len(characters)):
            chan = chan.replace(characters[x],"")
        
         
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            text = json.load(f)
            ticketlist = text["ticketlist"]
            
        text["log"] = chan
            
        
            
        with open(f"./{ctx.guild.id}/data.json","w") as data:
            json.dump(text,data)
        
        embed = discord.Embed(title="Log", description=f"Le channel de log a été changé pour <#{chan}>", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.respond(embed=embed)
        serv = self.bot.get_channel(int(chan))
        await serv.send("Ce channel a été défini comme channel de log.")
        
    @commands.slash_command(guild_ids = servlist, name = "setup", description = "command for setup the bot")
    @commands.has_permissions(ban_members=True)
    async def setup(self, ctx):
        
        os.mkdir(f'{ctx.guild.id}')
        text = {
            "log":"",
            "confess":{},
            "ticketlist":[],
            "ticketmsg":"Ticket créé et enregistré !",
            "mod":""
        }
        with open(f"./{ctx.guild.id}/data.json","w") as data:
            json.dump(text,data)
        data.close
        with open(f"./{ctx.guild.id}/{ctx.guild.name}","w") as data:
            json.dump(text,data)
        await ctx.respond("Bot setup\n\nPour que le système de vérification puisse fonctionner, vous devez définir le message que vous souhaitez envoyer à la création d'un ticket avec /ticketmessage.")           

    @commands.slash_command(guild_ids=servlist, name="modrole", description="define the moderator role")
    async def modrole(self, ctx, role):
        with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
        if role == None:
            await ctx.respond("Vous devez donner un role de modérateur.", ephemeral=True)
            
        print(role)
            
        
        characters="<@&>"
        for x in range(len(characters)):
            role = role.replace(characters[x],"")
        
         
        with open (f"./{ctx.guild.id}/data.json", "r") as f:
            text = json.load(f)
            
        text["mod"] = role
            
        
            
        with open(f"./{ctx.guild.id}/data.json","w") as data:
            json.dump(text,data)
        
        
        embed = discord.Embed(title="Log", description=f"Le rôle de modérateur a été changé pour <@&{role}>", color=discord.Color.from_rgb(color[0], color[1], color[2]))
        embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        await ctx.respond(embed=embed)
        

    @commands.slash_command(guild_ids = servlist, name = "ticketmsg", description = "command for setup the bot")
    @commands.has_permissions(ban_members=True)
    async def ticketmsg(self, ctx, *, message="Null"):
        with open(f"./{ctx.guild.id}/data.json","r") as t:
            data = json.load(t)
        
        if (message=="Null"):
            data["ticketmsg"] = "Ticket créé et enregistré !"
            with open(f"./{ctx.guild.id}/data.json","w") as f:
                json.dump(data,f)
            f.close
            await ctx.respond("Le message de ticket est le message par défaut.")
            
        else:
            data["ticketmsg"] = message
            with open(f"./{ctx.guild.id}/data.json","w") as f:
                json.dump(data,f)
            f.close
            await ctx.respond("Le message de ticket a bien été personnalisé !")

    @commands.command()
    async def serverid(self, ctx):
        await ctx.respond(f"{ctx.guild.id}")
        
    @commands.command()
    async def leaveserver(self,ctx):
        to_leave = self.bot.get_guild(ctx.guild.id)
        await to_leave.leave()

def setup(bot):
    bot.add_cog(Admin(bot))
