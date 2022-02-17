#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                09_PyGObject_GTK_Glade_Clock.py
#				 glade/09_PyGObject_GTK_Glade_Clock.glade
#            
#          USAGE: 
#				 ./09_PyGObject_GTK_Glade_Clock.py
#				or
#				  python3 09_PyGObject_GTK_Glade_Clock.py
# 
#   DESCRIPTION: This code consist of the following:
#                1- Designed GTK + UI with Glade
#                2- creates a modular code using a class to creating window widgets
#                3- Practical use of signals, events, callbacks, 
#                   and functions concepts.
#				 4- Using GLib.timeout_add function
#
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
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, GObject
from datetime import datetime


# class is used to manipulate window widgets
class MyWindow(Gtk.Window):
	
	timeout_id = None
	counter = 0
	# Initializer function
	def __init__(self):
		
		# A Gtk.Builder is an auxiliary object that reads textual 
		# descriptions of a user interface and instantiates the 
		# described objects. 
		builder = Gtk.Builder()
		
		# Import UI designed via Glade and connect signals
		builder.add_from_file('glade/09_PyGObject_GTK_Glade_Clock.glade')
		builder.connect_signals(self)
		
		# The functions builder.get_object() can be used to access 
		# the widgets in the interface by the names assigned to them 
		# inside the UI description. 
		window = builder.get_object('window1')
		self.label1 = builder.get_object('label1')
		self.buttonStart = builder.get_object('button1')

		
		#  Set attributes
		window.set_border_width(10)
		window.set_size_request(320, 100)
		window.set_title("PyGObject - Show Date/Time")
		self.label1.set_text("Date/Time: ")
		
		# Register callbacks
		self.buttonStart.connect("clicked", self.on_buttonStart_clicked)
		window.connect("destroy", Gtk.main_quit)
		window.connect("delete-event", Gtk.main_quit)
		
		window.show_all()
		
	# function definition
	def on_buttonStart_clicked(self, widget, *args):
		""" Handles "clicked" event of buttonStart. """
		self.buttonStart.set_sensitive(False)
		self.start_clock_timer()
		
	# Displays Timer
	def display_clock(self, *args, **kwargs):
		#  putting our datetime into a var and setting our label to the result. 
		#  we need to return "True" to ensure the timer continues to run, otherwise it will only run once.
		now = datetime.now()
		datetimenow = str(now.strftime("%Y-%M-%d %X"))
		self.label1.set_label(datetimenow)
		return True

	# Initialize Timer
	def start_clock_timer(self):
		GLib.timeout_add(250, self.display_clock, None)


#-----------------------------------------------------------------------
# main function
def main():
	
	window = MyWindow()
	
	# GTK main loop
	Gtk.main()
#-----------------------------------------------------------------------

		
if __name__ == '__main__':
    main()

