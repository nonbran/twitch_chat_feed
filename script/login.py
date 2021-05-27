from constant.user import username
from script.read_file import client_id, client_secret
from twitch_listener import listener
# login
reader = listener.connect_twitch(nickname=username,
                                 oauth=client_secret,
                                 client_id=client_id)
del client_id, client_secret
pass
