import datetime
import discord
from discord.ext import commands
class TimeConverter:
    pass
class Admin(commands.Cog):
    def __init__(self, bot):
        self.text = None
        self.bot = bot
    @commands.bot_has_permissions(manage_messages=True)
    @commands.command(name="clear",aliases=["clr"])
    async def clear(self, ctx, amount=100):
        if amount >100:
            await ctx.send("du darfst nicht mehr als 100 bereinigen")
            return
        await ctx.channel.purge(limit=amount)
        await ctx.send("Channel Bereinigung erfolgreich")
    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *reason):
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await member.kick(reason=reason)
        else:
            await ctx.send('**:no_entry:** Kein Benutzer angegeben!')

    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *reason):
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await member.ban(reason=reason)
            await ctx.send(f"der User {member} mit der id: {member.id} wurde gebannt")
        else:
            await ctx.send('**:no_entry:** Kein Benutzer angegeben!')
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, *, reason):
        user = discord.User()
        if user is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await ctx.guild.unban(user, reason=reason)
        else:
            await ctx.send('**:no_entry:** Kein Benutzer angegeben!')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def bans(self, ctx):
        users = await ctx.guild.bans()
        if len(users) > 0:
            msg = f'`{"ID":21}{"Name":25} Begründung\n'
            for entry in users:
                userID = entry.user.id
                userName = str(entry.user)
                if entry.user.bot:
                    username = '🤖' + userName  #:robot: emoji
                reason = str(entry.reason)  # Could be None
                msg += f'{userID:<21}{userName:25} {reason}\n'
            embed = discord.Embed(color=0xe74c3c)  # Red
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.set_footer(text=f'Server: {ctx.guild.name}')
            embed.add_field(name='Ranks', value=msg + '`', inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send('**:negative_squared_cross_mark:** Es gibt keine gebannten Nutzer!')

    @commands.command(alias=['clearreactions'])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def removereactions(self, ctx, messageid: str):
        message = await ctx.channel.get_message(messageid)
        if message:
            await message.clear_reactions()
        else:
            await ctx.send('**:x:** Konnte keine Nachricht mit dieser ID finden!')

    @commands.command()
    async def permissions(self, ctx):
        permissions = ctx.channel.permissions_for(ctx.me)

        embed = discord.Embed(title=':customs:  Permissions', color=0x3498db)  # Blue
        embed.add_field(name='Server', value=ctx.guild)
        embed.add_field(name='Channel', value=ctx.channel, inline=False)

        for item, valueBool in permissions:
            if valueBool == True:
                value = ':white_check_mark:'
            else:
                value = ':x:'
            embed.add_field(name=item, value=value)

        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def hierarchy(self, ctx):
        msg = f'Rollen-Hierarchie für Server **{ctx.guild}**:\n\n'
        roleDict = {}
        for role in ctx.guild.roles:
            if role.is_default():
                roleDict[role.position] = 'everyone'
            else:
                roleDict[role.position] = role.name
        for role in sorted(roleDict.items(), reverse=True):
            msg += role[1] + '\n'
        await ctx.send(msg)
    @commands.command(alies=['setrole', 'sr'])
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def setrank(self, ctx, member: discord.Member = None, *rankName: str):
        rank = discord.utils.get(ctx.guild.roles, name=' '.join(rankName))
        if member is not None:
            await member.add_roles(rank)
            await ctx.send(f':white_check_mark: Rolle **{rank.name}** wurde an **{member.name}** verteilt')
        else:
            await ctx.send(':no_entry: Du musst einen Benutzer angeben!')

    @commands.command(pass_context=True, alies=['rmrole', 'removerole', 'removerank'])
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def rmrank(self, ctx, member: discord.Member = None, *rankName: str):
        rank = discord.utils.get(ctx.guild.roles, name=' '.join(rankName))
        if member is not None:
            await member.remove_roles(rank)
            await ctx.send(f':white_check_mark: Rolle **{rank.name}** wurde von **{member.name}** entfernt')
        else:
            await ctx.send(':no_entry: Du musst einen Benutzer angeben!')
    @commands.command()
    async def servers(self, ctx):
        msg = '```js\n'
        msg += '{!s:19s} | {!s:>5s} | {} | {}\n'.format('ID', 'Member', 'Name', 'Owner')
        for guild in self.bot.guilds:
            msg += '{!s:19s} | {!s:>5s}| {} | {}\n'.format(guild.id, guild.member_count, guild.name, guild.owner)
        msg += '```'
        await ctx.send(msg)

    @commands.command(hidden=True)
    async def leaveserver(self, ctx, guildid: str):
        if guildid == 'this':
            await ctx.guild.leave()
            return
        else:
            guild = self.bot.get_guild(guildid)
            if guild:
                await guild.leave()
                msg = f':ok: Austritt aus {guild.name} erfolgreich!'
            else:
                msg = ':x: Konnte keine passende Guild zu dieser ID finden!'
        await ctx.send(msg)
    @commands.command(hidden=True)
    @commands.bot_has_permissions(manage_nicknames = True)
    async def nickname(self, ctx, *name):
        nickname = ' '.join(name)
        await ctx.me.edit(nick=nickname)
        if nickname:
            msg = f':ok: Ändere meinen Server Nickname zu: **{nickname}**'
        else:
            msg = f':ok: Reset von meinem Server Nickname auf: **{ctx.me.name}**'
        await ctx.send(msg)
    @commands.command(hidden=True,allias="nick")
    @commands.bot_has_permissions(manage_nicknames = True)
    async def setnickname(self, ctx, member: discord.Member=None, *name):
        if member == None:
            member = ctx.author
        nickname = ' '.join(name)
        await member.edit(nick=nickname)
        if nickname:
            msg = f':ok: Ändere Nickname von {member} zu: **{nickname}**'
        else:
            msg = f':ok: Reset von Nickname für {member} auf: **{member.name}**'
        await ctx.send(msg)
    @commands.command(hidden=True)
    async def geninvite(self, ctx, serverid: str):
        '''Generiert einen Invite für eine Guild wenn möglich (BOT OWNER ONLY)'''
        guild = self.bot.get_guild(int(serverid))
        invite = await self.bot.create_invite(guild, max_uses=1, unique=False)
        msg = f'Invite für **{guild.name}** ({guild.id})\n{invite.url}'
        await ctx.send("Invite Erststellt")

def setup(bot):
    bot.add_cog(Admin(bot))