#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                14_PyGObject_GTK_Glade_FileChooserDialog.py
#				 glade/14_PyGObject_GTK_Glade_FileChooserDialog.glade
#            
#          USAGE: 
#				 ./14_PyGObject_GTK_Glade_FileChooserDialog.py
#				or
#				  python3 14_PyGObject_GTK_Glade_FileChooserDialog.py
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

#-----------------------------------------------------------------------
# class is used to manipulate window widgets
class MyWindow(Gtk.Window):
	
	# Initializer function
	def __init__(self):
	
		# A Gtk.Builder is an auxiliary object that reads textual 
		# descriptions of a user interface and instantiates the 
		# described objects. 
		builder = Gtk.Builder()
		
		# Import UI designed via Glade and connect signals
		builder.add_from_file('glade/14_PyGObject_GTK_Glade_FileChooserDialog.glade')
		builder.connect_signals(self)
		
		# The functions builder.get_object() can be used to access 
		# the widgets in the interface by the names assigned to them 
		# inside the UI description. 
		window = builder.get_object('window1')
		self.miopen = builder.get_object('miopen')
		self.miopendir = builder.get_object('miopendir')
		self.miquit = builder.get_object('miquit')
		self.textview1 = builder.get_object('textview1')
		self.textbuffer1 = self.textview1.get_buffer()
		
		#  Set attributes
		window.set_border_width(10)
		window.set_size_request(800, 420)
		window.set_title("PyGObject - Treeview/ListStore")
		self.textview1.set_wrap_mode(True)
		self.textview1.set_justification(Gtk.Justification.LEFT)
		
		# Register callbacks
		self.miopen.connect("activate", self.on_miopen_activate)
		self.miopendir.connect("activate", self.on_miopendir_activate)
		self.miquit.connect("activate", self.on_miquit_activate)
		window.connect("destroy", self.on_MyWindow_destroy)
				
		window.show_all()
	
	# Create filter for file dialog
	def on_add_filters(self, dialog):
		filter_mp3 = Gtk.FileFilter()
		filter_mp3.set_name("Mp3 files")
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
		self.on_open_file_dialog()
		
	# function definition
	def on_miopendir_activate(self, event):
		self.on_open_dir_dialog()	
		
	def on_open_file_dialog(self):
		# create a filechooserdialog to open:
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
		# connect the dialog with the callback function open_response_cb()
		open_dialog.connect("response", self.open_file_response_cb)
		# show the dialog
		open_dialog.show()

	# callback function for the dialog open_dialog
	def open_file_response_cb(self, dialog, response_id):
		open_dialog = dialog
		# if response is "ACCEPT" (the button "Open" has been clicked)
		if response_id == Gtk.ResponseType.OK:
			 
			# self.filelists are the files that we get from the FileChooserDialog
			self.filelists = sorted(open_dialog.get_filenames())
			
			for i in range(len(self.filelists)):
				filename=os.path.basename(self.filelists[i])
				dirpath=os.path.dirname(self.filelists[i])
				#
				iter = self.textbuffer1.get_end_iter()
				self.textbuffer1.insert(iter, dirpath+filename+"\n\n")

		# if response is "CANCEL" (the button "Cancel" has been clicked)
		elif response_id == Gtk.ResponseType.CANCEL:
			print("cancelled: FileChooserAction.OPEN")
		# destroy the FileChooserDialog
		dialog.destroy()
			 
	def on_open_dir_dialog(self):
		# create a filechooserdialog to open:
		open_dialog = Gtk.FileChooserDialog()
		open_dialog.set_select_multiple(True)
		open_dialog.set_action(Gtk.FileChooserAction.SELECT_FOLDER)
		open_dialog.set_title("Open Folder")
		open_dialog.add_button('Cancel', Gtk.ResponseType.CANCEL)
		open_dialog.add_button('Open', Gtk.ResponseType.OK)

		# not only local files can be selected in the file selector
		open_dialog.set_local_only(False)
		# dialog always on top of the textview window
		open_dialog.set_modal(True)
		# connect the dialog with the callback function open_response_cb()
		open_dialog.connect("response", self.open_dir_response_cb)
		# show the dialog
		open_dialog.show()

	# callback function for the dialog open_dialog
	def open_dir_response_cb(self, dialog, response_id):
		open_dialog = dialog
		# if response is "ACCEPT" (the button "Open" has been clicked)
		if response_id == Gtk.ResponseType.OK:
			 
			# self.filelists are the files that we get from the FileChooserDialog
			self.filelists = sorted(open_dialog.get_filenames())
			
			for i in range(len(self.filelists)):
				iter = self.textbuffer1.get_end_iter()
				self.textbuffer1.insert(iter, self.filelists[i]+"/"+"\n\n")

		# if response is "CANCEL" (the button "Cancel" has been clicked)
		elif response_id == Gtk.ResponseType.CANCEL:
			print("cancelled: FileChooserAction.OPEN")
		# destroy the FileChooserDialog
		dialog.destroy()
		
		
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

