from asyncio import sleep
import discord
from discord.ext import commands
import json

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open (f"data.json", "r") as t:
            data2 = json.load(t)
            servlist = data2["servlist"]

    @commands.slash_command(guild_ids = servlist, name = "ticket", description = "command to setup ticket system")
    @commands.has_permissions(ban_members=True)
    async def ticket(self, ctx):
        await ctx.respond("création du système de ticket", ephemeral=True)
        btn1 = discord.ui.Button(
            label="Create a ticket",
            style=discord.ButtonStyle.blurple,
            emoji="🎟️"
        )
        
       
        
        view = discord.ui.View()
        view.add_item(btn1)
        
        await ctx.respond("Pour que les tickets aillent dans une catégorie spécifique, il faut que la catégorie s'appelle \"TICKET\".", ephemeral=True)
        
        async def btn1CallBack(interaction: discord.Interaction):
            with open (f"./{ctx.guild.id}/data.json", "r") as t:
                data = json.load(t)
                ticketlist=data["ticketlist"]
            
            if (len(ticketlist) == 0):
                ticketlist=["ticket-000"]
            
            cat = discord.utils.get(interaction.guild.categories, name="TICKET")
            num = ticketlist[len(ticketlist)-1]
            num = num[-3:]
            print(num)
            num = int(num)+1
            if (num < 10):
                num = "00" + str(num)
            elif (num<100):
                num = "0" + str(num)
            print(num)
            
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                interaction.user: discord.PermissionOverwrite(read_messages=True)
            }
            await interaction.guild.create_text_channel(name=f"ticket-{num}",category=cat, overwrites=overwrites)
                    
                
        btn1.callback = btn1CallBack
        
        
        await ctx.send("Réagissez pour créer un ticket !", view=view)

def setup(bot):
    bot.add_cog(Ticket(bot))
