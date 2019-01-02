#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Tab():
    def __init__(self):
        header = Gtk.HBox()
        title_label = Gtk.Label()
        image = Gtk.Image()
        image.set_from_stock(Gtk.STOCK_CLOSE, Gtk.ICON_SIZE_MENU)
        close_button = Gtk.Button()
        close_button.set_image(image)
        close_button.set_relief(Gtk.RELIEF_NONE)
        self.connect(close_button, 'clicked', self.close_cb)
        header.pack_start(title_label, expand=True, fill=True, padding=0)
        header.pack_end(close_button, expand=False, fill=False, padding=0)
        header.show_all()
        self.header = header

class Notebook(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_title('Notebook')
        self.set_default_size(300, 200)
        self.connect('destroy', Gtk.main_quit)

        notebook = Gtk.Notebook()
        self.add(notebook)

        for page in range(1, 4):
            label1 = Gtk.Label('Notebook')
            label2 = Gtk.Label()
            label2.set_text('Page %i' % (page))
            notebook.append_page(label1, label2)
            notebook.set_tab_reorderable(label1, True)

window = Notebook()
window.show_all()

Gtk.main()