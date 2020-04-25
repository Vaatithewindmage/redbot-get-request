import urllib.request
from redbot.core import commands
temp = 3

class URLSTAT(commands.Cog):


    @commands.command()
    async def status(self, ctx):
        fp = urllib.request.urlopen("https://tz2.us/temp.php")
        mybytes = fp.read()
        
        mystr = mybytes.decode("utf8")
        fp.close()
        await ctx.send(mystr)
        #await ctx.send(urllib.request.urlopen("https://tz2.us/temp.php").read())
