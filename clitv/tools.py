import tempfile
import os
import shutil
import tempfile

tmpdir = tempfile.gettempdir() + "/clitv"

def make_command(command, options):
    command = command.split()
    cmd = []
    for e in command:
        if e == "%s":
            arg = "\"" + options.pop(0) + "\""
            cmd.append(arg)
        else:
            cmd.append(e)
    return cmd

def ensure_dir(dir):
    if os.path.exists(dir):
        return dir
    else:
        os.mkdir(dir)
        return dir

def get_tmpdir():
    return ensure_dir(tmpdir)

def clear_tmpdir():
    if os.path.exists(tmpdir):
        shutil.rmtree(tmpdir)

def sane_filename(fn):
    return "".join([c for c in fn if c.isalpha() or c.isdigit() or c==' ']).rstrip()
