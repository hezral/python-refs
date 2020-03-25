#!/usr/bin/env python3
# 

import gi
gi.require_version('Gtk', '3.0')
gi.require_version("Wnck", "3.0")
gi.require_version("Bamf", "3")

from gi.repository import Bamf, Gtk

matcher = Bamf.Matcher()

active_window = matcher.get_active_window()

app = matcher.get_application_for_window(active_window)

icon = app.get_icon().split('/')[4][:-4]

app_icon = Gtk.IconTheme.get_default().load_icon(icon, 48, 0)

print(app.get_name())

print(app_icon.get_height())

