import discord
from discord.ext import commands
import json

class DropDownMenu(discord.ui.View):
        @discord.ui.select(placeholder="Placeholder", min_values=1, max_values=1, options=[
            discord.SelectOption(label="test", description="desc", emoji="🚽"),
            discord.SelectOption(label="scenario", description="Porject ATALANTE", emoji="☢️")])
        
        async def callback(self, select, interaction: discord.Interaction):
            
            with open (f"./{interaction.guild.id}/data.json", "r") as t:
                data = json.load(t)
                info = data["info"]
            with open (f"data.json", "r") as t:
                data2 = json.load(t)
                color = data2["color"]
            
            
            choosen = info[f"{select.values[0]}"]
            
            name = choosen["nom"]
            lore = choosen["lore"]
            image = choosen["image"]
            
            embed = discord.Embed(title=f"{name}", description=f"{lore}", color=discord.Color.from_rgb(color[0], color[1], color[2]))
            embed.set_image(url=f"{image}")
            embed.set_footer(text="Bot by LoliChann", icon_url=f"https://i.pinimg.com/564x/d5/d6/ff/d5d6ff7f3a344085dbffc4a9a34f538e.jpg")
        
            await interaction.channel.send(embed=embed)


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    with open (f"data.json", "r") as t:
        data2 = json.load(t)
        servlist = data2["servlist"]

    
    @commands.slash_command(guild_ids = servlist, name = "info", description = "test")
    @commands.has_permissions(ban_members=True)
    async def info(self, ctx):
        
        if (ctx.guild.id != 961006436555571250):
            await ctx.respond("Cette commande n'set pas prise en charge sur ce serveur.", ephemeral=True)
            return
        
        
        view = DropDownMenu()
        
        await ctx.respond("menu", view=view, ephemeral=True)
def setup(bot):
    bot.add_cog(Info(bot))
