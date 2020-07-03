from clitv import configuration
from clitv import tools
import subprocess
import os

def list_files():
    path = os.path.expanduser(configuration.config['general']['library_path'])
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def view_stored(file):
    path = os.path.expanduser(configuration.config['general']['library_path'])
    file = os.path.join(path, file)
    command = configuration.config['general']['video_player']
    command = tools.make_command(command, [file])
    proc_player = subprocess.Popen(command,
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)
    return proc_player
