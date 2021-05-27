from local.settings import path_secrets
with open(path_secrets, 'r') as psf:
    secrets = psf.readlines()
client_id = secrets[1].strip()
oauth_token = secrets[3].strip()
