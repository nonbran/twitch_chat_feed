from constant.filename import fn_secrets
from os import getcwd
from pathlib import Path
# init paths
local_path = Path(getcwd())
project_path = local_path.parent
user_path = project_path.parent.parent
# init filenames
path_secrets = Path(user_path, fn_secrets)
