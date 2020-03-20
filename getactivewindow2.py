#!/usr/bin/env python3

import subprocess
import gi
gi.require_version("Wnck", "3.0")
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Wnck

def get_active_app():
    
    label = Gtk.Label()
    label.props.max_width_chars = 100

    window = Gtk.Window(title="Clips Debug Window") #debug window to see contents displayed in Gtk.Window

    image = Gtk.Image.new_from_icon_name("image-x-generic", Gtk.IconSize.DIALOG)


    scr = Wnck.Screen.get_default()

    def updated(*args):
        scr.force_update()
        active = scr.get_active_window()

        if active is not None:
            pid = active.get_pid()
            icon = scr.get_active_window().get_icon()
            icon = icon.scale_simple(24, 24, GdkPixbuf.InterpType.BILINEAR)
            name = scr.get_active_window().get_class_group_name()
        else:
            name = scr.get_active_workspace().get_name()
            icon = Gtk.IconTheme.get_default().load_icon('preferences-desktop-wallpaper', 24, 0)

        image.set_from_pixbuf(icon)
        label.set_text(name)

    scr.connect('active-window-changed', updated)

    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    box.pack_start(image, True, True, 0)
    box.pack_start(label, True, True, 0)
    window.set_border_width(6)
    window.add(box)
    window.show_all()
    window.connect('destroy', Gtk.main_quit)
    
                

                

clips = get_active_app()
Gtk.main()