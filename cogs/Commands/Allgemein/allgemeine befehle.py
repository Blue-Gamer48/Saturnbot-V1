import random
import discord
from discord.ext import commands
from discord.ext.commands import bot
from main import client
class Allgemein(commands.Cog):
    def __init__(self, bot):
        self.text = None
        self.bot = bot
    @commands.command(name="gutenmorgen")
    async def gutenmorgen(self, ctx):
        self.embed = discord.Embed(title="Einen wunderschönen guten Morgen.",
                              description=f"der User {ctx.author.mention} wünscht euch einen Tollen Start in den Tag",
                              color=0x00ff00)
        self.embed.set_footer(text=f'Gesendet von: {ctx.author.name} • {ctx.author.id}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=self.embed)
    @commands.command(name="gutenacht")
    async def gutenacht(self,ctx):
        self.embed = discord.Embed(title="Gute Nacht.",
                              description=f"der User {ctx.author.mention} wünscht euch eine gute Nacht",
                              color=0x00ff00)
        self.embed.set_footer(text=f'Gesendet von: {ctx.author.name} • {ctx.author.id}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=self.embed)
    @commands.command(aliases=['latency'])
    async def ping(self, ctx):
        await ctx.send(f'**Pong! ``{round(client.latency * 1000)}ms``**')
    @commands.command(name="invite")
    async def invite(self,ctx):
        embed=self.embed = discord.Embed(title="Invite",description="Link zum hinzufügen vom Saturn Bot: https://discord.com/oauth2/authorize?client_id=923162114187747328&permissions=8&scope=bot")
        await ctx.send(embed=self.embed)
    @commands.command(name="serverinvite",aliases=["si"])
    async def serverinvite(self,guild,ctx):
        invite = await guild.text_channels[0].create_invite(reason=None, max_age=0, max_uses=0, temporary=False, unique=True)
        self.embed = discord.Embed(title="Einladungslink Erstellt",
                                   description="",
                                   color=0x00ff00)
        self.embed.add_field(name="Link:",value=f"{invite}")
        await ctx.send(embed=self.embed)

    @commands.command(aliases=['make_role'])
    @commands.has_permissions(manage_roles=True)  # Check if the user executing the command can manage roles
    async def create_role(self,ctx, *, name):
        guild = ctx.guild
        await guild.create_role(name=name)
        await ctx.send(f'Role `{name}` has been created')
        bot.command(aliases=['server-leave'])
    @commands.command(aliases=['wave', 'hi', 'ohaiyo'])
    async def hello(self, ctx):
        gifs = ['https://cdn.discordapp.com/attachments/102817255661772800/219512763607678976/large_1.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219512898563735552/large.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219518948251664384/WgQWD.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219518717426532352/tumblr_lnttzfSUM41qgcvsy.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519191290478592/tumblr_mf76erIF6s1qj96p1o1_500.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519729604231168/giphy_3.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519737971867649/63953d32c650703cded875ac601e765778ce90d0_hq.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219519738781368321/17201a4342e901e5f1bc2a03ad487219c0434c22_hq.gif']
        msg = f':wave: {random.choice(gifs)}'
        await ctx.send(msg)
    @commands.command(name="bugreport",aliases=["br"])
    async def bugreport(self,ctx,):
        await ctx.send("demnächst Verfügbar")

def setup(bot):
    bot.add_cog(Allgemein(bot))