import urllib.request

from discord.ext import commands
from wakeonlan import send_magic_packet


class IP(commands.Cog):
    """
    the basic system functions
    currently consisting of:
    on_ready, help, ping, load, unload 
    """
    def __init__(self, client):
        self.client = client


    @commands.is_owner()
    @commands.dm_only()
    @commands.command(brief="A command to get the global IPv4 and IPv6 the bot is running on.")
    async def ip(self, ctx):
        # get IPv4 if possible
        try: ipv4 = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
        except: ipv4 = "IPv4 could not be found."

        # get IPv6 if possible
        try: ipv6 = urllib.request.urlopen('https://v6.ident.me').read().decode('utf8')
        except: ipv6 = "IPv6 could not be found."

        # send message with information
        await ctx.send(f"IP Information:\nIPv4: {ipv4}\nIPv6: {ipv6}")



async def setup(client):
    await client.add_cog(IP(client))