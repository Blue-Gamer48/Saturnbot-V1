import random
import discord
import pytz
from discord.ext import commands
from discord.ext.commands import CommandNotFound, bot
from datetime import datetime
class Saturnbot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
      print("g")
      if isinstance(error, CommandNotFound):
        channel = self.bot.get_channel(927156852062556210)
        de = pytz.timezone("Europe/Berlin")
        self.embed = discord.Embed(title="Ein Fehler ist Aufgetreten ⛔", description="", color=0x03465c, timestamp=datetime.now().astimezone(tz=de))
        self.embed.add_field(name="Gesendet von:", value=f"```{ctx.author}```", inline=True),
        self.embed.add_field(name='Fehler:', value=error, inline=True)
        self.embed.set_author(name="", icon_url="https://dbdzm869oupei.cloudfront.net/img/sticker/preview/3201.png")
        await channel.send(embed=self.embed)
        await ctx.send(embed=self.embed)
    @commands.Cog.listener()
    async def on_message(self,message):
        if self.bot.user.mentioned_in(message):
            await message.channel.send(f"Mein Prefix ist {self.bot.command_prefix}")
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(random.choice(guild.text_channels))
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        self.embed = discord.Embed(title=f"Danke fürs Einladen des Bots",
                                   description=f"ich hoffe du wirst viel Spaß Haben mit dem bot um dir die befehle anzeigen zu lassen nutze help",
                                   color=0xc800ff)
        channel = random.choice(guild.text_channels)
        await channel.send(embed=self.embed)
        invite = await guild.text_channels[0].create_invite(reason="Save for Support", max_age=0, max_uses=0, temporary=False, unique=True)
        self.embed2 = discord.Embed(title=f"Saturn Bot Jointe auf einen Server {invite}",
                                   description=f"der Bot: {self.bot.user.name} wurde zu: {guild.name} Eingeladen",
                                   color=0xc800ff)
        channel = self.bot.get_channel(926861744712863774)
        await channel.send(embed=self.embed2)
def setup(bot):
    bot.add_cog(Saturnbot(bot))