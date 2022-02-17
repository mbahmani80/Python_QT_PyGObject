#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                15_PyGObject_GTK_Glade_TreeView_ListStore.py
#				 glade/15_PyGObject_GTK_Glade_TreeView_ListStore.glade
#            
#          USAGE: 
#				 ./15_PyGObject_GTK_Glade_TreeView_ListStore.py
#				or
#				  python3 15_PyGObject_GTK_Glade_TreeView_ListStore.py
# 
#   DESCRIPTION: 
#
#        OPTIONS: ---
#   REQUIREMENTS: Python, GTK+, Glade
#           BUGS: ---
#          NOTES: PyGObject tutorial
#         AUTHOR: Mahdi Bahmani (www.itstorage.co)
#   ORGANIZATION: merdasco
#        CREATED: 06.06.2020
#    LAST EDITED: 
#       REVISION: 1.1
#**********************************************************************/
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

#python
#>>> import gi
#>>> gi.require_version('Gtk', '3.0')
#>>> from gi.repository import Gtk, GLib
#>>> help(Gtk.TreeView)
#>>> help (Gtk.TreeSelection)
#-----------------------------------------------------------------------
# class is used to manipulate window widgets
class MyWindow(Gtk.Window):
	
	playlist = []
	treeview1_listmodel = None
	# Initializer function
	def __init__(self):
		
		# A Gtk.Builder is an auxiliary object that reads textual 
		# descriptions of a user interface and instantiates the 
		# described objects. 
		builder = Gtk.Builder()
		
		# Import UI designed via Glade and connect signals
		builder.add_from_file('glade/15_PyGObject_GTK_Glade_TreeView_ListStore.glade')
		builder.connect_signals(self)
		
		# The functions builder.get_object() can be used to access 
		# the widgets in the interface by the names assigned to them 
		# inside the UI description. 
		window = builder.get_object('window1')
		self.menuitem1 = builder.get_object('menuitem1')
		self.miopen = builder.get_object('miopen')
		self.miquit = builder.get_object('miquit')
		self.addbtn = builder.get_object('addbtn')
		self.entry1 = builder.get_object('entry1')
		self.entry2 = builder.get_object('entry2')
		self.textview1 = builder.get_object('textview1')
		self.textview1_textbuffer1 = self.textview1.get_buffer()
		self.treeview1 = builder.get_object('treeview1')
		self.labelstatusbar = builder.get_object('labelstatusbar')
		self.printselected = builder.get_object('printselected')
		self.printall =builder.get_object('printall')
		self.nextbtn = builder.get_object('nextbtn')
		self.previousbtn = builder.get_object('previousbtn')
		self.clearlist = builder.get_object('clearlist')
		self.removeselected = builder.get_object('removeselected')
		
		#  Set attributes
		window.set_border_width(10)
		window.set_size_request(800, 320)
		window.set_title("PyGObject - Treeview/ListStore")
		self.textview1.set_wrap_mode(True)
		self.textview1.set_justification(Gtk.Justification.LEFT)
		# tree selection
		self.treeview1_selection = self.treeview1.get_selection()
		
		# Register callbacks
		self.miopen.connect("activate", self.on_miopen_activate)
		self.miquit.connect("activate", self.on_miquit_activate)
		self.printselected.connect("clicked", self.on_printselected_clicked)
		self.printall.connect("clicked", self.on_printall_clicked)
		self.addbtn.connect("clicked", self.on_addbtn_clicked)
		self.nextbtn.connect("clicked", self.on_nextbtn_clicked )
		self.previousbtn.connect("clicked", self.on_previousbtn_clicked)
		# treeview
		self.removeselected.connect("clicked", self.on_treeview_remove_selected)
		self.clearlist.connect("clicked", self.on_treeview_clearlist)
		self.treeview1.connect("row-activated", self.on_treeview_activated)
		# creating the treeview columns
		self.on_treeView_create_model_columns(self.treeview1)
		# List rows from Tree Selection 		
		self.treeview1_selection.connect("changed", self.on_treeview_selection_changed)

		window.connect("destroy", self.on_MyWindow_destroy)
				
		window.show_all()
	
	def on_treeView_create_model_columns(self, treeview):
		#self.treeview = Gtk.TreeView.new_with_ListStore1(self.language_filter)
		# create a liststore with two columns
		self.treeview1_listmodel = Gtk.ListStore(str,str)
		self.treeview1.set_model(self.treeview1_listmodel)
		for i, column_title in enumerate(["Path", "File Name"]):
			renderer = Gtk.CellRendererText()
			column = Gtk.TreeViewColumn(column_title, renderer, text=i)
			column.set_clickable(True)   
			column.set_resizable(True)
			treeview.append_column(column)

	
	# Create filter for file dialog
	def on_add_filters(self, dialog):
		filter_mp3 = Gtk.FileFilter()
		filter_mp3.set_name("Media files")
		filter_mp3.add_mime_type("audio/mp3")
		dialog.add_filter(filter_mp3)
	
		filter_ply = Gtk.FileFilter()
		filter_ply.set_name("Playlist")
		filter_ply.add_mime_type("text/plain")
		dialog.add_filter(filter_ply)
	
		filter_any = Gtk.FileFilter()
		filter_any.set_name("Any files")
		filter_any.add_pattern("*")
		dialog.add_filter(filter_any)
			   
	# function definition
	def on_miopen_activate(self, event):
		# Create a filechooserdialog to open:
		open_dialog = Gtk.FileChooserDialog()
		open_dialog.set_select_multiple(True)
		open_dialog.set_action(Gtk.FileChooserAction.OPEN)
		open_dialog.set_title("Open Files")
		open_dialog.add_button('Cancel', Gtk.ResponseType.CANCEL)
		open_dialog.add_button('Open', Gtk.ResponseType.OK)
		# Add filter
		self.on_add_filters(open_dialog)
		# not only local files can be selected in the file selector
		open_dialog.set_local_only(False)
		# dialog always on top of the textview window
		open_dialog.set_modal(True)
		# Connect the dialog with the callback function open_response_cb()
		open_dialog.connect("response", self.open_response_cb)
		# Show the dialog
		open_dialog.show()

	# Callback function for the dialog open_dialog
	def open_response_cb(self, dialog, response_id):
		open_dialog = dialog
		# if response is "ACCEPT" (the button "Open" has been clicked)
		if response_id == Gtk.ResponseType.OK:
			 
			# self.filelists are the files that we get from the FileChooserDialog
			self.filelists = sorted(open_dialog.get_filenames())
			
			for i in range(len(self.filelists)):
				filename=os.path.basename(self.filelists[i])
				dirpath=os.path.dirname(self.filelists[i])
				# append to the model the title that is in the entry
				self.treeview1_listmodel.append([dirpath,filename])

		# if response is "CANCEL" (the button "Cancel" has been clicked)
		elif response_id == Gtk.ResponseType.CANCEL:
			print("cancelled: FileChooserAction.OPEN")
		# Destroy the FileChooserDialog
		dialog.destroy()
		
	# Double click on a row
	def on_treeview_activated(self, widget, row, col):
		model = widget.get_model()
		rowpathfile = model[row][0] + "/" + model[row][1]
		self.labelstatusbar.set_text(model[row][1])	
		print(rowpathfile)
			 
	def on_treeview_selection_changed(self, treeview1_selection):
		(model, pathlist) = treeview1_selection.get_selected_rows()
		# Emptying the playlist
		del self.playlist[:]
		for path in pathlist :
			tree_iter = model.get_iter(path)
			value1 = model.get_value(tree_iter,0)
			value2 = model.get_value(tree_iter,1)
			print (value1+"/"+value2)
			self.playlist.append(value1+"/"+value2)
		
	
	def on_printselected_clicked(self, widget):
		print("on_printselected_clicked")
		self.on_treeview_selection_changed(self.treeview1_selection)
		if len(self.treeview1_listmodel) != 0:
			# printing the list using loop 
			for i in range(len(self.playlist)): 
				print (self.playlist[i])
				iter = self.textview1_textbuffer1.get_end_iter()
				if iter is not None:
					self.textview1_textbuffer1.insert(iter, self.playlist[i]+"\n\n")
				# otherwise, ask the user to select something to print
				else:
					print("Select a title to print")
		else:
			# print a message in the terminal alerting that the model is empty
			print("Empty list")
	
	def on_check_printall_state(self):	
		if self.index > self.max_index:
			return False
		else:
			self.index += 1	
			if self.index < self.max_index:
				# Get path pointing to 6th row in list store
				self.path = Gtk.TreePath(self.index)
				self.treeiter = self.treeview1_listmodel.get_iter(self.path)
				# Get value of all columns
				self.value1 = self.treeview1_listmodel.get_value(self.treeiter, 0)
				self.value2 = self.treeview1_listmodel.get_value(self.treeiter, 1)
				iter = self.textview1_textbuffer1.get_end_iter()
				if iter is not None:
					self.textview1_textbuffer1.insert(iter, self.value1+"/"+self.value2+"\n\n")
				print(self.value1+"/"+self.value2+"\n")
		return True # continue calling every x milli
		

	def on_printall_clicked(self, widget):
		print("on_printall_clicked")
		self.index = -1
		self.max_index = len(self.treeview1_listmodel)
		if self.max_index != 0:
			self.check_printall_state_id = GLib.timeout_add(1000, self.on_check_printall_state)
		else:
			print("Empty list")

	
	def on_treeview_clearlist(self, widget):
		print("on_treeview_clearlist")
		 # if there is still an entry in the model
		if len(self.treeview1_listmodel) != 0:
			model = self.treeview1.get_model()
			model.clear()	
		# else, if there are no entries in the model, print "Empty list"
		# in the terminal
		else:
			print("Empty list")
	
	def on_treeview_remove_selected(self, widget):
		# if there is still an entry in the model
		if len(self.treeview1_listmodel) != 0:
			(model, pathlist) = self.treeview1_selection.get_selected_rows()
			for p in reversed(pathlist):
				itr = model.get_iter(p)
				model.remove(itr)
		# else, if there are no entries in the model, print "Empty list"
        # in the terminal
		else:
			print("Empty list")          
	
	# callback function for the "Add" button
	def on_addbtn_clicked(self, button):
		print("on_addbtn_clicked")
		# append to the model the title that is in the entry
		path = self.entry1.get_text()
		filename = self.entry2.get_text()
		self.treeview1_listmodel.append([path,filename])
		# and print a message in the terminal
		print("%s has been added" % (path+filename))
	
	
	def on_nextbtn_clicked(self, button):
		print("on_nextbtn_clicked")	
		
		#get the selected row, and just return if none are selected
		model, rows = self.treeview1_selection.get_selected_rows()
		if len(rows) == 0:
		   return
		
		# calculate the next row to be selected by finding
		# the last selected row in the list of selected rows
		# Incrementing by 1
		next_to_select = rows[-1][0] + 1
		
		#if this is not the last row in the last
		#unselect all rows, select the previous row
		if next_to_select:
			self.treeview1_selection.unselect_all()
			self.treeview1_selection.select_path(next_to_select)
		
		
			
			
		
	def on_previousbtn_clicked(self, button):
		print("on_previousbtn_clicked")
		
		#get the selected row, and just return if none are selected
		model, rows = self.treeview1_selection.get_selected_rows()
		if len(rows) == 0:
		   return
		
		# calculate the next row to be selected by finding
		# the last selected row in the list of selected rows
		previous_to_select = rows[-1][0]
		
		#if this is not the last row in the last
		#unselect all rows, select the previous row
		if previous_to_select:
			# Decrementing by 1
			previous_to_select = rows[-1][0] - 1
			self.treeview1_selection.unselect_all()
			self.treeview1_selection.select_path(previous_to_select)
		
	
	# function definition	
	def on_miquit_activate(self, widget, *args):
		Gtk.main_quit()
		
	# function definition
	def on_MyWindow_destroy(self, widget, *args):
		""" Handles destroy event of main window. """
		Gtk.main_quit()	
#-----------------------------------------------------------------------
# main function
def main():
	
	window = MyWindow()
	
	# GTK main loop
	Gtk.main()
#-----------------------------------------------------------------------
		
if __name__ == '__main__':
    main()

# https://python-gtk-3-tutorial.readthedocs.io/en/latest/_sources/treeview.txt
