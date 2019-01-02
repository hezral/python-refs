#!/usr/bin/env python3
# simplified example from the tutorial

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

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

entry = Gtk.SearchEntry(
            placeholder_text="Search")
entry.props.margin_left = 5
entry.props.margin_right = 5
entry.props.margin_top = 5
entry.props.margin_bottom = 5 
entry.set_completion(completion)

# boilerplate
window = Gtk.Window()
window.add(entry)

window.connect('destroy', lambda w: Gtk.main_quit())
window.show_all()
Gtk.main()