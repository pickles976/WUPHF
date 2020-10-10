from instabot import Bot
from auth import (
    password,
    username
)
from thumbnail_downloader import download_thumb
import os

def post_insta(photo,caption):

    bot = Bot()
    bot.login(username=username,password=password)

    filepath = download_thumb(photo)

    try:
        bot.upload_photo("./" + filepath,caption=caption)
    except:
        print("failed to upload the photo")

    try:
        os.remove("./" + filepath)
    except:
        print("failed to remove the image")

    try:
        os.remove("./" + filepath + ".jpg.REMOVE_ME")
    except:
        print("failed to remove stuff")
