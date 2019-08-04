#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("delete-event", self.on_delete)

        self.listbox = Gtk.ListBox()
        self.listbox.add(Gtk.Label('foo'))
        self.listbox.add(Gtk.Label('bar'))
        self.listbox.add(Gtk.Label('qux')) # ListBoxRow is added automatically

        button = Gtk.Button("Clear selection")
        button.connect("clicked", self.on_button_clicked)

        vbox = Gtk.VBox()
        vbox.pack_start(button, False, True, 0)
        vbox.pack_start(self.listbox, False, True, 0)

        self.add(vbox)
        self.show_all()


    def on_button_clicked(self, btn):
        self.listbox.unselect_all()

    def on_delete(self, win, event):
        Gtk.main_quit()


app = MainWindow()
app.connect("destroy", Gtk.main_quit)
Gtk.main()