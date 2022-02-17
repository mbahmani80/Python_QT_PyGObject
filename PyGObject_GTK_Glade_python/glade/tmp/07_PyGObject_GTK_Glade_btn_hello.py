#!/usr/bin/env python3
#===============================================================================
# 
#          FILES:
#                07_PyGObject_GTK_Glade_btn_hello.py
#                07_PyGObject_GTK_Glade_btn_hello.glade
#
#         USAGE: ./07_PyGObject_GTK_Glade_btn_hello.py
# 
#   DESCRIPTION: This program creates a simple form with a label and a 
#                button to show how signals work
# 
#       OPTIONS: ---
#  REQUIREMENTS: GTK+, Glade, Python3
#          BUGS: ---
#         NOTES: PyGTK Glade tutorial
#        AUTHOR: Mahdi Bahmani (www.itstorage.co)
#  ORGANIZATION: merdasco
#       CREATED: 13.05.2020 18:59:07
#   LAST EDITED: 
#      REVISION: 1.1
#===============================================================================


import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file('07_PyGObject_GTK_Glade_btn_hello.glade')
		builder.connect_signals(self)
		
		self.label = builder.get_object('label')
		
		self.button1 = builder.get_object('button1')
		self.button1.connect("clicked", self.on_button1_clicked)
		
		window = builder.get_object('main_window')
		window.connect('delete-event', Gtk.main_quit)
		window.show_all()
		
	def on_button1_clicked(self, widget):
		print("on_button1_clicked")
		self.label.set_text('Hello World')
				
		
if __name__ == '__main__':
	win = MyWindow()
	Gtk.main()
