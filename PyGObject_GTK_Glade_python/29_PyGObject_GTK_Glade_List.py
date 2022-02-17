import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GObject
import sys

class Song(GObject.GObject):

    path = GObject.Property(type=str)
    name = GObject.Property(type=str)

    def __init__(self, path, name):
        GObject.GObject.__init__(self)
        self.path = path
        self.name = name
class GUI:

    def __init__(self):        
        self.playlist = Gio.ListStore()
        self.playlist.append(Song("path1", "name1"))
        self.playlist.append(Song("path2", "name2"))
        self.playlist.append(Song("path3", "name3"))

        play_listbox = Gtk.ListBox()
        play_listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        play_listbox.bind_model(self.playlist, self.create_widget_func)
        play_listbox.connect('row-selected', self.on_row_selected_1)
        #play_listbox.connect('row-selected', self.on_row_selected_2)
        play_listbox.connect('selected-rows-changed', self.on_selected_rows_changed)

        window = Gtk.Window()
        window.add(play_listbox)
        window.connect("destroy", self.on_window_destroy)
        window.show_all()

    def create_widget_func(self, song):
        return Gtk.Label(label = song.name)

    def on_row_selected_1(self ,container, row):
        #print("on_row_selected_1")
        song = self.playlist.get_item(row.get_index())
        #print(song.path)
        #print(row.get_child().get_text())

    def on_row_selected_2(self ,container, row):
        print("on_row_selected_2")
        print(row.get_child().get_text())

    def on_selected_rows_changed(self, container):      
        print("on_selected_rows_changed", len(container.get_selected_rows()), "item(s) selected")
        for row in container.get_selected_rows():
            song = self.playlist.get_item(row.get_index())
            print(song.name, song.path)
        print("---")

    def on_window_destroy(self, window):
        Gtk.main_quit()

def main():

    app = GUI()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())
