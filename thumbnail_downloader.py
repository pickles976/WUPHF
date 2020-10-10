import wget
def download_thumb(photo):

    image_filename = ""

    try:
        image_filename = wget.download(photo)
    except:
        print("failed to download thumbnail")

    #print("Image downloaded successfully: ", image_filename)
    return image_filename