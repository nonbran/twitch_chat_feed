from script.read_file import client_id, client_secret
import twitch
helix = twitch.Helix(
    client_id=client_id,
    client_secret=client_secret)
del client_id, client_secret
pass
