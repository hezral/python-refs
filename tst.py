#!/usr/bin/env python
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk


wnd=gtk.Window()
img=gtk.Image()


img.set_from_icon_name( "/home/adi/Work/publicapi-tests/avatar.png", gtk.ICON_SIZE_BUTTON
img.show()
wnd.show(); gtk.main()