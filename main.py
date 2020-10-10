from Twitter import tweet
from Instagram import post_insta
from auth import channel_id
import feedparser
import asyncio
import discord
from discord.ext import tasks, commands
from auth import DISCORD_TOKEN as TOKEN
from auth import channel_name

async def wait(time):
    await asyncio.sleep(time)

def post(message):
    global entry
    tweet(message)
    post_insta(entry["media_thumbnail"][0]["url"],message)

def check_message():

    global latest_video
    global entry

    #RSS stuff
    feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=" + channel_id)
    entry = feed.entries[0]

    print(entry)

    #if new video, post on all social medias
    if latest_video != entry["id"]:
        latest_video = entry["id"]
        message = "New Video! " + entry["title"] + ": " + entry["link"]
        return message
    else:
        return ""

#Get the latest video from the RSS feed
feed = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=" + channel_id)
entry = feed.entries[0]
print(entry)
latest_video = entry["id"]

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@tasks.loop(seconds=30.0)
async def my_background_task():

    global latest_video
    await client.wait_until_ready()
    message = check_message()

    if message != "":
        post(message)
        for guild in client.guilds:
            for channel in guild.text_channels:
                if channel.name == channel_name:
                    await channel.send("@everyone " + message)

my_background_task.start()
client.run(TOKEN)

