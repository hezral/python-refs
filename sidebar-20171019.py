import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Sidebar(Gtk.HPaned):
    def __init__(self):
        Gtk.HPaned.__init__(self)
        self.scrolled_window = Gtk.ScrolledWindow()
        self.set_size_request(300, -1)

        # TreeView
        self.tree_view = Gtk.TreeView()
        self.tree_view.set_headers_visible(True)
        self.tree_view.set_enable_tree_lines(False)
        self.tree_view.set_enable_search(True)
        #self.tree_view.set_level_indentation(1)

        # Renderer
        self.cell_renderer = Gtk.CellRendererText()

        # TreeViewColumn
        self.log_list = Gtk.TreeViewColumn()
        self.log_list.set_title("Local Logs")
        self.log_list.pack_start(self.cell_renderer, True)
        self.log_list.add_attribute(self.cell_renderer, "text", 0)

        # TreeStore
        self.tree_store = Gtk.TreeStore(str)
        # item
        self.list_item = self.tree_store.append(None, ["System"])
        self.tree_store.append(self.list_item, ["system.log"])
        self.list_item = self.tree_store.append(None, ["User"])
        self.tree_store.append(self.list_item, ["some.log"])
        # add to list
        self.tree_view.append_column(self.log_list)
        self.tree_view.set_model(self.tree_store)

        # add to HPaned
        self.add1(self.tree_view)
        self.text_view = Gtk.TextView()
        self.add2(self.text_view)
        self.set_position(150)
        self.tree_view.connect("row-activated", self.on_activated)

    def on_activated(self, widget, row, col):
        model = widget.get_model()
        text = model[row][0]
        print(text)

        buffer = Gtk.TextBuffer()
        buffer.set_text(text+" is selected")
        #self.tv.set_buffer(buffer)