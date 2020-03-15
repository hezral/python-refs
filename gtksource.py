#!/usr/bin/env python3
# 

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')

from gi.repository import Gtk
from gi.repository import GtkSource
from gi.repository import GObject

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", Gtk.main_quit)

textview = GtkSource.View()
textview.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
textview.set_editable(False)
textbuffer = textview.get_buffer()
textbuffer.set_text("Hello world"*2, -1)

#draw_spaces = GtkSource.DrawSpacesFlags.ALL
#draw_spaces = 0
#textview.set_draw_spaces(draw_spaces)

window.add(textview)
window.show_all()

Gtk.main()