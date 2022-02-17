#!/usr/bin/python3

from gi.repository import Gtk

class Window(Gtk.Window):

	def __init__(self):
	    Gtk.Window.__init__(self, title="MyWindow")
	
	    self.set_default_size(200, 200)
	
	    self.liststore = Gtk.ListStore(str, str)
	    for i in range(1,10):
	        row = "Row"+ str(i)
	        value = "Value"+str(i)
	        self.liststore.append([row, value])
	
	
	    treeview = Gtk.TreeView(model=self.liststore)
	
	    renderer_text = Gtk.CellRendererText()
	    column = Gtk.TreeViewColumn("Col1", renderer_text, text=0)
	    treeview.append_column(column)
	
	    column = Gtk.TreeViewColumn("Col2", renderer_text, text=1)
	    treeview.append_column(column)
	
	    treeview.get_selection().set_mode(Gtk.SelectionMode.MULTIPLE)
	    treeview.get_selection().set_select_function(self.select_function)
	
	    self.add(treeview)
	
	def select_function(self, treeselection, model, path, current):
	    state = True
	
	    if treeselection.count_selected_rows() < 2:
	        state = True
	    else:
	        if treeselection.path_is_selected(path):
	            state = True
	        else:
	            state = False
	
	    return state

win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
