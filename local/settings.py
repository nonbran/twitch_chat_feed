from constant.filename import fn_secrets, fn_settings
from os import getcwd
from pathlib import Path
# init paths
runtime_path = Path(getcwd())
project_path = runtime_path.parent
python_path = project_path.parent
user_path = project_path.parent.parent
# init filenames
path_secrets = Path(python_path, fn_secrets)
pass
