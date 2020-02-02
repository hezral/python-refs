import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DynamicLabel(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)

        self.set_title("Dynamic Label")
        self.set_size_request(1, 1)
        self.set_default_size(300,300) 
        #self.set_position(Gtk.WIN_POS_CENTER)

        l = Gtk.Label("Painfully long text " * 30)
        l.set_line_wrap(True)
        l.connect("size-allocate", self.size_request)
        ImportantWidget  = Gtk.Label("ImportantWidget")

        vbox = Gtk.VBox(False, 2)
        HSeparator = Gtk.HSeparator()
        vbox.pack_start(ImportantWidget, False, False, 0)
        vbox.pack_start(HSeparator, False, False, 0)
        vbox.pack_start(l, False, False, 0)


        self.add(vbox)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def size_request(self, l, s ):
        l.set_size_request(s.width -1, -1)

DynamicLabel()
Gtk.main()