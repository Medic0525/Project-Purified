import discord
from discord.ext import commands
from core.cog import cog
class fun(cog):

    @commands.command()
    async def say(self, ctx,*sentence):
        await ctx.message.delete(delay=0)
        a=" "
        for i in sentence:
            a=a+" "+i
        await ctx.send(a)

    



def setup(bot):
    bot.add_cog(fun(bot))
