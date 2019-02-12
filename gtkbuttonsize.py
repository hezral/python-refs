import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()
window.set_size_request(400, 150)
window.connect("delete-event", Gtk.main_quit)
vbox = Gtk.VBox()
window.add(vbox)

 
title = Gtk.Label("Set the size of button to exactly 80 x 32")
title.set_size_request(-1, 40)
vbox.pack_start(title, 0, 0, 0)

button = Gtk.Button('b') 
button.set_size_request(16, 16) 
hbox = Gtk.HBox()
hbox.pack_start(button, 0, 0, 0) 

vbox.pack_start(hbox, 0, 0, 0) 

window.show_all()

Gtk.main()