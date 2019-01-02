''' header bar '''

import gi
gi.require_version('Gtk', '3.0')
#gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk

class Headerbar(Gtk.HeaderBar):

    def __init__(self):

        Gtk.HeaderBar.__init__(self)

        self.set_show_close_button(True)
        self.props.title = "Rogu"

        box = Gtk.HBox(spacing=10)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        # # Create Button
        # self.create_button = Gtk.Button()
        # self.create_button.props.relief = Gtk.ReliefStyle(2)
        # image = Gtk.Image.new_from_icon_name(
        #     "document-new", Gtk.IconSize.LARGE_TOOLBAR)
        # image.set_tooltip_text("New Note (Ctrl+N)")
        # image.show()
        # self.create_button.add(image)
        # box.add(self.create_button)

        # # New Notebook Button
        # self.notebook_button = Gtk.Button()
        # self.notebook_button.props.relief = Gtk.ReliefStyle(2)

        # image = Gtk.Image.new_from_icon_name(
        #     "folder-new", Gtk.IconSize.LARGE_TOOLBAR)
        # image.set_tooltip_text("New Notebook (Ctrl+K)")
        # image.show()
        # self.notebook_button.add(image)
        # box.add(self.notebook_button)

        # # save button
        # self.save_button = Gtk.Button()
        # self.save_button.props.relief = Gtk.ReliefStyle(2)

        # image = Gtk.Image.new_from_icon_name(
        #     "document-save", Gtk.IconSize.LARGE_TOOLBAR)
        # image.set_tooltip_text("Save Note (Ctrl+S)")
        # image.show()
        # self.save_button.add(image)
        # box.add(self.save_button)

        # Delete Button
        # self.delete_button = Gtk.Button()
        # self.delete_button.props.relief = Gtk.ReliefStyle(2)
        # image = Gtk.Image.new_from_icon_name(
        #     "edit-delete", Gtk.IconSize.LARGE_TOOLBAR)
        # image.set_tooltip_text("Delete Note (Ctrl+D)")
        # image.show()
        # self.delete_button.add(image)
        # self.pack_end(self.delete_button)

        def on_match_selected(completion, treemodel, treeiter):
            print(treemodel[treeiter][completion.get_text_column()])

        urls = [ 
            'http://www.google.com',
            'http://www.google.com/android',
            'http://www.greatstuff.com',
            'http://www.facebook.com',
            ]   
        liststore = Gtk.ListStore(str)
        for s in urls:
            liststore.append([s])

        completion = Gtk.EntryCompletion()
        completion.set_model(liststore)
        completion.set_text_column(0)
        completion.connect('match-selected', on_match_selected)

        self.search_entry = Gtk.SearchEntry(
            placeholder_text="Search")
        self.search_entry.props.margin_left = 15
        self.search_entry.props.margin_right = 5
        self.search_entry.props.margin_top = 5
        self.search_entry.props.margin_bottom = 5
        self.search_entry.set_completion(completion)
        #self.entry.connect("search-changed", self._on_search)
        self.pack_end(self.search_entry)


        self.pack_start(box)
