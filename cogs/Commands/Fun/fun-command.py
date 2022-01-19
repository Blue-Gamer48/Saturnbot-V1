import aiohttp
from discord.ext import commands
import asyncio
import aiohttp
import random
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="witz")
    async def witz(self,ctx):
        with open('witze.txt', 'r',encoding='utf-8') as f:
            read = f.read()
            array = read.split('\n')
            witz = random.choice(array)
        await ctx.channel.send(witz,)
    @commands.command(name="ball")
    async def ball(self, ctx, *, frage):
        antwort = ["Ja", "Nein", "Vileicht"]
        await ctx.send(f"``{ctx.author}`` deine antwort auf deine Frage ``{frage}`` lautet: ``{random.choice(antwort)}``")
    @commands.command()
    async def countdown(self, ctx):
        '''It's the final countdown'''
        countdown = ['five', 'four', 'three', 'two', 'one']
        for num in countdown:
            await ctx.send('**:{0}:**'.format(num))
            await asyncio.sleep(1)
        await ctx.send('**:ok:** DING DING DING')

    @commands.command(aliases=['randomcat'])
    async def cat(self, ctx):
        '''Zufällige Katzen Bilder nyan~'''
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://aws.random.cat/meow') as r:
                res = await r.json()
                emojis = [':cat2: ', ':cat: ', ':heart_eyes_cat: ']
                await ctx.send(random.choice(emojis) + res['file'])
    @commands.command()
    async def steinigt(self, ctx, member:str):
        await ctx.send(f'R.I.P. {member}\nhttps://media.giphy.com/media/l41lGAcThnMc29u2Q/giphy.gif')
    @commands.command(aliases=['hypu', 'train'])
    async def hype(self, ctx):
        '''HYPE TRAIN CHOO CHOO'''
        hypu = ['https://cdn.discordapp.com/attachments/102817255661772800/219514281136357376/tumblr_nr6ndeEpus1u21ng6o1_540.gif',
                'https://cdn.discordapp.com/attachments/102817255661772800/219518372839161859/tumblr_n1h2afSbCu1ttmhgqo1_500.gif',
                'https://gfycat.com/HairyFloweryBarebirdbat',
                'https://i.imgur.com/PFAQSLA.gif',
                'https://abload.de/img/ezgif-32008219442iq0i.gif',
                'https://i.imgur.com/vOVwq5o.jpg',
                'https://i.imgur.com/Ki12X4j.jpg',
                'https://media.giphy.com/media/b1o4elYH8Tqjm/giphy.gif']
        msg = f':train2: CHOO CHOO {random.choice(hypu)}'
        await ctx.send(msg)

    @commands.command()
    async def coinflip(self, ctx):
        choices = ["Kopf", "Zahl", "Die Münze ist Runtergefallen, bitte Versuche es Nochmal"]
        rancoin = random.choice(choices)
        await ctx.send(rancoin)
def setup(bot):
    bot.add_cog(Fun(bot))