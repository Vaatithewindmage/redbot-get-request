import urllib.request
from redbot.core import commands
temp = 3

class Mycog(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def status(self, ctx):
        await ctx.send(urllib.request.urlopen("https://tz2.us/temp.php").read())
