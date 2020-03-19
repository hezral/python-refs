#!/usr/bin/env python3

import subprocess
import gi
gi.require_version("Wnck", "3.0")
from gi.repository import Wnck

def get_active_app():
    scr = Wnck.Screen.get_default()
    scr.force_update()
    pid = scr.get_active_window().get_pid()

    if pid != None:
        return scr.get_active_window().get_class_group_name()

#    process = subprocess.Popen(["ps -o cmd= {}".format(pid)], stdout=subprocess.PIPE, shell=True)

#    if process != None:
#        return str(process.communicate()[0]).split('/')[3].title()

    return None

if __name__ == "__main__":
    print(get_active_app())