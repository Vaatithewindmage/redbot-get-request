import urllib.request, json
from redbot.core import commands
temp = 3

class URLSTAT(commands.Cog):


    @commands.command()
    async def status(self, ctx):
        url = "https://mcapi.us/server/query?ip=104.238.222.158"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        pawait ctx.send(data)
