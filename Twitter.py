def tweet(message):

    # Twitter stuff
    from twython import Twython
    from auth import (
        api_key,
        api_secret_key,
        access_token,
        access_token_secret
    )

    twitter = Twython(
        api_key,
        api_secret_key,
        access_token,
        access_token_secret
    )

    try:
        twitter.update_status(status=message)
    except:
        print("unable to post to Twitter")