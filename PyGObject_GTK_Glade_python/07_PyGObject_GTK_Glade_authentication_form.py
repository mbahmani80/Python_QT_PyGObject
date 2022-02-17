#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                07_PyGObject_GTK_Glade_authentication_form.py
#				 glade/07_PyGObject_GTK_Glade_authentication_form.glade
#            
#          USAGE: 
#				 ./07_PyGObject_GTK_Glade_authentication_form.py
#				or
#				  python3 06_PyGObject_GTK_Glade_form.py
# 
#   DESCRIPTION: This program is an Authentication form consists of 
#                 GtkButton, GtkLabel, and GtkEntry with standard use 
#				  of the class, signals, and callbacks.
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
		builder.add_from_file('glade/07_PyGObject_GTK_Glade_authentication_form.glade')
		builder.connect_signals(self)
		
		# The functions builder.get_object() can be used to access 
		# the widgets in the interface by the names assigned to them 
		# inside the UI description.
		window = builder.get_object('window1')
		self.lbluser = builder.get_object('lbluser')
		self.lblpass = builder.get_object('lblpass')
		self.lblstatus = builder.get_object('lblstatus')
		self.entryuser = builder.get_object('enteyuser')
		self.entrypass = builder.get_object('enterypass')
		self.btncheckpass = builder.get_object('btncheckpass')
		
		#  Set attributes
		window.set_border_width(10)
		window.set_size_request(320, 300)
		window.set_title("PyGObject - Authentication")
		self.entrypass.set_visibility(False)
		
		# Register callbacks
		window.connect('delete-event', Gtk.main_quit)
		window.connect("destroy", Gtk.main_quit)
		self.btncheckpass.connect("clicked", self.on_btncheckpass_clicked)
		
		window.show_all()
	
	# function definition
	def on_btncheckpass_clicked(self, widget):
		print("Checking Username Password!")
		username = Gtk.Entry.get_text(self.entryuser)
		password = Gtk.Entry.get_text(self.entrypass)
		if (username == "itstorage.co"):
			if(password == "123456"):
				self.lblstatus.set_text("Authentication was successful")
				print("Authentication was successful")
			else:
				self.lblstatus.set_text("Password is incorrect")
				print("Password is incorrect")
		else:
			self.lblstatus.set_text("Username is incorrect")
			print("Username is incorrect")


#-----------------------------------------------------------------------
# main function
def main():

	window = MyWindow()
	
	# GTK main loop
	Gtk.main()
#-----------------------------------------------------------------------
		
if __name__ == '__main__':
    main()

