#!/usr/bin/env python3


import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Granite, GObject


welcome = Granite.WidgetsWelcome()


# welcome = welcome.new("Welcome", "cn.App.application_descriptio")

# # Welcome voices
# welcome.append("object-inverse", "Dark mode", "Switch to the dark side")
# welcome.append("utilities-terminal", "Open Terminal", "Just an example of action")
# welcome.append("help-contents", "Info", "Learn more about this application")

# box.add(welcome)

win = Gtk.Window()

#win.add(welcome)
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()