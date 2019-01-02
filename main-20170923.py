''' main application '''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import headerbar as hb
import sidebar as sb
import os
import subprocess

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Rogu")
        #self.set_border_width(5)
        self.set_size_request(1024, 700)
        self.set_resizable(True)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Window theme light or dark
        settings = Gtk.Settings.get_default()
        settings.set_property("gtk-application-prefer-dark-theme", True)

        # Header Bar
        hbar = hb.Headerbar()
        hbar.connect("destroy", Gtk.main_quit)
        self.set_titlebar(hbar)

        # MAIN WINDOW
        #main_window = Gtk.Grid(column_homogeneous=False, column_spacing=0)
        
        # SIDEBAR
        self.sidebar = sb.Sidebar()
        #self.sidebar.view.connect("row_activated", self.show_note)

        #main_window.attach(self.sidebar, 0, 0, 1, 2)
        #self.add(main_window)
        self.add(self.sidebar)


def start():
    win = MainWindow()
    #win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__=='__main__':
    start()

