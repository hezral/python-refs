#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def draw_cb(widget, cr):
  cr = widget.get_property('window').cairo_create()
  cr.set_source_rgba(0,0,0,0.5)
  cr.rectangle(50,75,100,100)
  cr.fill()
  return False

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", Gtk.main_quit)

overlay = Gtk.Overlay()
window.add(overlay)

textview = Gtk.TextView()
textview.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
textbuffer = textview.get_buffer()
textbuffer.set_text("Hello world"*18, -1)
overlay.add(textview)

da=Gtk.DrawingArea()
da.connect('draw', draw_cb)
overlay.add_overlay(da)

overlay.show_all()

window.show_all()

Gtk.main()
