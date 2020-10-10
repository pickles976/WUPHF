import discord
from auth import DISCORD_TOKEN as TOKEN
from auth import channel_name



def discord_post(message):

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def post_video():
        text_channel = []
        for guild in client.guilds:
            for channel in guild.text_channels:
                if channel.name == channel_name:
                    text_channel = channel.id
                    await channel.send("@everyone " + message)
        await client.close()

client = discord.Client()
client.run(TOKEN)