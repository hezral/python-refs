import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Granite, Gio

class Welcome(Gtk.Box):
        
    # Define variable for GTK global theme
    settings = Gtk.Settings.get_default()

    def __init__(self):
        Gtk.Box.__init__(self, False, 0)

        # Create welcome widget
        welcome = Granite.WidgetsWelcome()
        welcome = welcome.new("Welcome", 'cn.App.application_description')

        # Welcome voices
        welcome.append("object-inverse", "Dark mode", "Switch to the dark side")
        welcome.append("utilities-terminal", "Open Terminal", "Just an example of action")
        welcome.append("help-contents", "Info", "Learn more about this application")
        
        welcome.connect("activated", self.on_welcome_activated)

        self.add(welcome)

    def on_welcome_activated(self, widget, index):
        if index == 0:
            # Use GTK Dark theme
            if self.settings.get_property("gtk-application-prefer-dark-theme") == True:
                self.settings.set_property("gtk-application-prefer-dark-theme", False)
            else:
                self.settings.set_property("gtk-application-prefer-dark-theme", True)
        elif index == 0:
            # Open terminal
            os.system("io.elementary.terminal")
        else:
            # Open webpage
            webbrowser.open_new_tab("https://github.com/mirkobrombin/Rogu")
        print("Index: "+str(index))

settings = Gtk.Settings.get_default()
settings.set_property("gtk-application-prefer-dark-theme", True)
win = Gtk.Window()
win.set_size_request(1024, 700)
notebook = Granite.WidgetsDynamicNotebook.new()
notebook.show_tabs = True
notebook.allow_restoring = True
notebook.allow_duplication = True
notebook.allow_new_window = False
notebook.group_name = 'test'
notebook.icon = None

content1 = Welcome()
content2 = Welcome()
content3 = Welcome()
label = Gtk.Label(label='Left Pane')

tab_icon = Gio.FileIcon.new(Gio.File.new_for_path('data/blank.svg'))

tab1 = Granite.WidgetsTab.new("test1", tab_icon, content1)
tab2 = Granite.WidgetsTab.new("test2", tab_icon, content2)
tab3 = Granite.WidgetsTab.new("test3", tab_icon, content3)
tab = Granite.WidgetsTab.new("default", tab_icon, label)

notebook.insert_tab(tab1, 0)
notebook.insert_tab(tab2, 1)

notebook.current = tab1

def addtab(self):
    n = notebook.get_n_tabs()
    n = n + 1
    print(n)
    notebook.insert_tab(tab3, n)

def ontabclosed(self,widget):
    if notebook.get_n_tabs() == 0:
        n = notebook.get_n_tabs()
        n = n + 1
        #print(n)
        notebook.insert_tab(Granite.WidgetsTab.new("Welcome", tab_icon, Welcome()), n)

notebook.connect('new_tab_requested',addtab)
notebook.connect('tab_removed',ontabclosed)

notebook.show()

win.add(notebook)
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()