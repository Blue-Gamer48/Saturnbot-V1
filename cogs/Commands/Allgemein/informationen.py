import os
from typing import io

import discord
from discord.ext import commands
from datetime import datetime
import pytz
class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="entwicklerliste")
    async def entwicklerliste(self,ctx):
        self.embed = discord.Embed(title=f"Sourcecode Entwickler Liste", description="", color=0x03465c)
        self.embed.add_field(name="help und alle Untermenüs", value="***von:*** ```Blue_Gamer48#3565```", inline=False),
        self.embed.set_footer(text=f'Gesendet von: {ctx.author.name} • {ctx.author.id}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=self.embed)
    @commands.command(name="userinfo")
    async def userinfo(self, ctx,member:discord.Member=None):
        if member == None:
            member = ctx.author
        de = pytz.timezone("Europe/Berlin")
        self.embed = discord.Embed(title=f"Userinfo für {member.name}", description="", color=0x03465c,
                              timestamp=datetime.now().astimezone(tz=de))
        self.embed.add_field(name="Name", value=f"```{member.name}```", inline=True),
        self.embed.add_field(name='Bot', value=f'```{("Ja" if member.bot else "Nein")}```', inline=True)
        self.embed.add_field(name='Nickname', value=f'```{(member.nick if member.nick else "Nicht gesetzt")}```',
                        inline=True)
        self.embed.add_field(name='Server beigetreten', value=f'```{member.joined_at.date()}```', inline=True)
        self.embed.add_field(name='Discord beigetreten', value=f'```{member.created_at.date()}```', inline=True)
        self.embed.add_field(name='Rollen', value=f'```{len(member.roles)}```', inline=True)
        self.embed.add_field(name='Farbe', value=f'```{member.color}```', inline=True)
        self.embed.add_field(name="Deine Rollen:",value=", ".join([role.mention for role in member.roles if not role.is_default()]))
        self.embed.add_field(name='Booster', value=f'```{("Ja" if member.premium_since else "Nein")}```', inline=True)
        self.embed.set_footer(text=f'Gesendet von: {ctx.author.name} • {ctx.author.id}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=self.embed)
def setup(bot):
    bot.add_cog(Info(bot))