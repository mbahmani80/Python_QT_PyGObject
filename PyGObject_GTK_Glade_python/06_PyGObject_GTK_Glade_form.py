#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                06_PyGObject_GTK_Glade_form.py
#				 glade/06_PyGObject_GTK_Glade_form.glade
#            
#          USAGE: 
#				 ./06_PyGObject_GTK_Glade_form.py
#				or
#				  python3 06_PyGObject_GTK_Glade_form.py
# 
#   DESCRIPTION: This code consist of the following:
#                1- Designed GTK + UI with Glade
#                2- creates a modular code using a class to creating window widgets
#                3- Practical use of signals, events, callbacks, 
#                   and functions concepts.
#
#        OPTIONS: ---
#   REQUIREMENTS: Python, GTK+, Glade
#           BUGS: ---
#          NOTES: PyGObject tutorial
#         AUTHOR: Mahdi Bahmani (www.itstorage.co)
#   ORGANIZATION: merdasco
#        CREATED: 2020/03/24 23:49
#    LAST EDITED: 
#       REVISION: 1.1
#**********************************************************************/

import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
#-----------------------------------------------------------------------
# class is used to manipulate window widgets
class MyWindow(Gtk.Window):
	
	# initialize class var
	countbtn1 = 0 
	
	# Initializer function
	def __init__(self):
		
		# A Gtk.Builder is an auxiliary object that reads textual 
		# descriptions of a user interface and instantiates the 
		# described objects. 
		builder = Gtk.Builder()
		
		# Import UI designed via Glade and connect signals
		builder.add_from_file('glade/06_PyGObject_GTK_Glade_form.glade')
		builder.connect_signals(self)
		
		# The functions builder.get_object() can be used to access 
		# the widgets in the interface by the names assigned to them 
		# inside the UI description. 
		self.label1 = builder.get_object('label1')
		self.label2 = builder.get_object('label2')
		self.button1 = builder.get_object('button1')
		window = builder.get_object('window1')
		
		# Register callbacks
		window.connect('delete-event', Gtk.main_quit)
		window.connect("destroy", Gtk.main_quit)
		self.button1.connect("clicked", self.on_button1_clicked)
		
		window.show_all()
	
	# function definition
	def on_button1_clicked(self, widget):
		self.countbtn1 += 1
		str1 = "Button1 Clicked: " + str(self.countbtn1)
		str2 = str(self.countbtn1)
		self.label1.set_text(str1)
		self.label2.set_text(str2)
		print(str1)
		print(str2)

#-----------------------------------------------------------------------
# main function
def main():
	
	window = MyWindow()
	
	# GTK main loop
	Gtk.main()
#-----------------------------------------------------------------------
		
if __name__ == '__main__':
    main()
