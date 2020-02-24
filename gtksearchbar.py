#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2019 Purism SPC
# SPDX-License-Identifier: GPL-3.0+
# Author: David Boddie <david.boddie@puri.sm>

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GObject, Gtk

gi.require_version('Handy', '0.0')
from gi.repository import Handy


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='com.example.ex20_search_bar')

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)

        # Create a title bar with a header and a search button.
        title_bar = Handy.TitleBar()
        header_bar = Gtk.HeaderBar(title='Search Bar')
        toggle_button = Gtk.ToggleButton(
            image=Gtk.Image.new_from_icon_name('system-search-symbolic',
                                               Gtk.IconSize.BUTTON)
        )
        header_bar.add(toggle_button)
        title_bar.add(header_bar)
        window.set_titlebar(title_bar)

        # Add an overlay containing a search bar to the window.
        # The search bar itself contains an entry that accepts input from the
        # user.
        overlay = Gtk.Overlay()
        search_bar = Handy.SearchBar(halign='fill', valign='start')
        entry = Gtk.Entry()
        search_bar.add(entry)
        search_bar.connect_entry(entry)
        search_bar.set_show_close_button(True)
        
        overlay.add(search_bar)
        window.add(overlay)

        # Bind the search button's active property to the search-mode-enabled
        # property of the search bar so that the user can toggle the bar on and
        # off.
        toggle_button.bind_property('active', search_bar,
                                    'search-mode-enabled',
                                    GObject.BindingFlags.BIDIRECTIONAL)

        window.show_all()


if __name__ == "__main__":

    app = Application()
    result = app.run(sys.argv)
    sys.exit(result)
