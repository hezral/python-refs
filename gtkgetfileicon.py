#!/usr/bin/env python3

import os , gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio , Gtk


def filechooser():
    filechooserdialog = Gtk.FileChooserDialog()
    filechooserdialog.set_title("Choose a file")
    filechooserdialog.add_button("_Open", Gtk.ResponseType.OK)
    filechooserdialog.add_button("_Cancel", Gtk.ResponseType.CANCEL)
    filechooserdialog.set_default_response(Gtk.ResponseType.OK)
    filechooserdialog.set_position(Gtk.WindowPosition.MOUSE)
    
    response = filechooserdialog.run()
    if response == Gtk.ResponseType.OK:
        file = filechooserdialog.get_filename()
        filechooserdialog.destroy()
    else:
        filechooserdialog.destroy()
    return file

def get_thumbnail(filename,size):
    if os.path.exists(filename):
        print('hey')
        file = Gio.File.new_for_path(filename)
        info = file.query_info('standard::icon' , 0 , Gio.Cancellable())
        
        print(type(info.get_icon().get_names()))

        i = 1
        icon_file = None
        for icon_name in info.get_icon().get_names():
            if icon_file is None:
                try:
                    print(i)
                    i = i + 1
                    print(icon_name)
                    icon_file = Gtk.IconTheme.get_default().load_icon(icon_name, size, 0)
                except:
                    print('pass')
        print(icon_file)


        try:
            icon = info.get_icon().get_names()[0]
            print('Try: ', icon)
            icon_file = Gtk.IconTheme.get_default().load_icon(icon, size, 0)
        except:
            icon = info.get_icon().get_names()[1]
            print('Except: ', icon)
            icon_file = Gtk.IconTheme.get_default().load_icon(icon, size, 0)

        print(icon_file)

        
        # if icon_file != None:
        #     print(type(icon_file))
        #     final_filename = icon_file.get_filename()
        # return final_filename
        #return icon_file

file = filechooser()
print(file)

get_thumbnail(file,32)


