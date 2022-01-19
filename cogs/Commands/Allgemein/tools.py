import discord
from discord.ext import commands
from googletrans import Translator
class Allgemein(commands.Cog):
    def __init__(self, bot):
        self.text = None
        self.bot = bot
    @commands.command(aliases=["tl", "Tl", "Translate"])
    async def translate(self, ctx, lang, *, thing):
        translator = Translator()
        translation = translator.translate(thing, dest=lang)
        self.embed = discord.Embed(title="Übersetzer.",
                                   description=translation.text,
                                   color=0x00ff00)
        self.embed.set_footer(text=f'Gesendet von: {ctx.author.name} • {ctx.author.id}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=self.embed)
def setup(bot):
    bot.add_cog(Allgemein(bot))