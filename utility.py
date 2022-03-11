import discord
from discord.ext import commands
from core.cog import cog

class utility(cog):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(F'pong! {round((self.bot.latency)*1000)} [ms]')

def setup(bot):
    bot.add_cog(utility(bot))