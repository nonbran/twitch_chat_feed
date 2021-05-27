from configparser import RawConfigParser
from constant.filename import fn_secrets, fn_settings
from constant.pathname import dn_settings
from os import getcwd
from os import stat
from os.path import exists
from pathlib import Path
# init paths
runtime_path = Path(getcwd())
project_path = runtime_path.parent
python_path = project_path.parent
user_path = project_path.parent.parent
# init filenames
path_secrets = Path(python_path, fn_secrets)
# path_settings = Path(project_path, dn_settings, fn_settings)
# TODO WIP init configparser & read settings.cfg
# path_stat = stat(path_settings)
# path_exists = True if exists(path_settings) else False
# ocp = RawConfigParser() if path_exists else None
# if ocp is None:
#     print(f'\nno settings.cfg found at path')
#     exit()
pass
