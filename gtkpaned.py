''' a '''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ClipboardRowData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(ClipboardRowData, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class PyApp(Gtk.Window):
   def __init__(self):
      super(PyApp, self).__init__()
      self.set_title("HPaned widget Demo")
      self.set_default_size(640, 480)
      vp = Gtk.HPaned()
      sw = Gtk.ScrolledWindow()
      sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

      listbox_2 = Gtk.ListBox()
      items = 'This is a sorted ListBox that has very long sentences and lists that goes on and on and on and on'.split()

      for item in items:
         listbox_2.add(ClipboardRowData(item))

      def sort_func(row_1, row_2, data, notify_destroy):
         return row_1.data.lower() > row_2.data.lower()

      def filter_func(row, data, notify_destroy):
         return False if row.data == 'Fail' else True

      listbox_2.set_sort_func(sort_func, None, False)
      listbox_2.set_filter_func(filter_func, None, False)

      listbox_2.connect('row-activated', self.on_row_activated)

      listbox_2.show_all()

      sw.add_with_viewport(listbox_2)

      vp.add1(sw)
      self.tv = Gtk.TextView()
      vp.add2(self.tv)
      vp.set_position(100)
      
      self.add(vp)      
      self.connect("destroy", Gtk.main_quit)
      self.show_all()

   def on_row_activated(self, widget, row):
      text = row.data
      print(text)

      buffer = Gtk.TextBuffer()
      buffer.set_text(text+" is selected")
      self.tv.set_buffer(buffer)

if __name__ == '__main__':
    PyApp()
    Gtk.main()