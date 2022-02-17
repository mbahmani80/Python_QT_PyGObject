#!/usr/bin/python
#
# Filename: 02_PyGObject_GTK_hello.py
#
# PyGObject tutorial 
#
# Author: Mahdi Bahmani
# Website: itstorage.co
# Last edited: 2020/03/24 23:49

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#-----------------------------------------------------------------------

# class is used to manipulate window widgets
class MyWindow(Gtk.Window):

	# Initializer function
	def __init__(self):
		
		#   Create Widgets
		#   Create a new window
		Gtk.Window.__init__(self, title="PyGObject - Hello World")
		self.box = Gtk.Box(spacing=6)
		self.label1 = Gtk.Label()

		#  Set attributes
		self.label1.set_text('Hello World')
		self.set_size_request(290, 100)
		
		# Pack everything and display
		self.add(self.box)
		self.box.pack_start(self.label1, True, True, 0)
		self.show_all()
#-----------------------------------------------------------------------

# main
if __name__ == '__main__':
	
	window = MyWindow()
	
	# Register callbacks
	window.connect("destroy", Gtk.main_quit)
	
	# GTK main loop
	Gtk.main()
	
