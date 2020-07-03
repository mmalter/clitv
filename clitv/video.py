from clitv import configuration
from clitv import tools
import subprocess
import os
import shutil
import time
import logging

def download_proc(source, identifier):
    sources = configuration.sources()
    source = sources[source]
    file = tools.get_tmpdir() + "/" + tools.sane_filename(identifier)
    command = tools.make_command(source["download"], [file, identifier])
    proc = subprocess.Popen(command,
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.PIPE)
    return proc

def view(source, identifier):
    proc_dl = download_proc(source, identifier)
    time.sleep(int(configuration.config['general']['cache_time']))
    command = configuration.config['general']['video_player']
    file = tools.get_tmpdir() + "/" + tools.sane_filename(identifier)
    partfile = tools.get_tmpdir() + "/" + identifier + ".part"
    if os.path.isfile(partfile):
        file = partfile
    command = tools.make_command(command, [file])
    proc_player = subprocess.Popen(command,
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)
    return proc_player, proc_dl

def save_from_tmp(identifier, title):
    file = tools.get_tmpdir() + "/" + tools.sane_filename(identifier)
    target = os.path.expanduser(configuration.config['general']['library_path']) + "/" +tools.sane_filename(title)
    shutil.copy(file, target)

def remove_from_tmp(identifier):
    file = tools.get_tmpdir() + "/" + tools.sane_filename(identifier)
    os.remove(file)
