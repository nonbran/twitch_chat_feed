from constant.user import username
from script.read_file import client_id, oauth_token
from twitch_listener import listener
# login
reader = listener.connect_twitch(nickname=username,
                                 oauth=oauth_token,
                                 client_id=client_id)
del client_id, oauth_token
pass
