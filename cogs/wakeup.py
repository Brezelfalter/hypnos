from discord.ext import commands
from wakeonlan import send_magic_packet


class WakeUp(commands.Cog):
    """
    the basic system functions
    currently consisting of:
    on_ready, help, ping, load, unload 
    """
    def __init__(self, client):
        self.client = client


    @commands.command(brief="Wakeup my PC from sleep.")
    async def wakeup(self, ctx):
        # send magic packet to my pc, using mac address and ip address
        send_magic_packet("04:42:1a:0d:cf:78", ip_address="192.168.178.146")
        await ctx.message.send("Sent magic packet to device. MAC: 04:42:1a:0d:cf:78\tIP: 192.168.178.146")

    
    @commands.command(brief="Wakeup a device on the network specifying the MAC and IP address manually.")
    async def wakeup_any(self, ctx, mac:str, ip:str):
        # send magic packet to any device on the network using the specified mac and ip address
        send_magic_packet(mac, ip_address=ip)
        await ctx.message.send("Sent magic packet to device. MAC: {mac}\tIP: {ip}")



async def setup(client):
    await client.add_cog(WakeUp(client))