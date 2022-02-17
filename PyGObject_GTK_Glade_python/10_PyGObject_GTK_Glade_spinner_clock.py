#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                10_PyGObject_GTK_Glade_spinner_clock.py
#				 glade/10_PyGObject_GTK_Glade_spinner_clock.glade
#            
#          USAGE: 
#				 ./10_PyGObject_GTK_Glade_spinner_clock.py
#				or
#				  python3 10_PyGObject_GTK_Glade_spinner_clock.py
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
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, GObject
from datetime import datetime
#-----------------------------------------------------------------------
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
		builder.add_from_file('glade/10_PyGObject_GTK_Glade_spinner_clock.glade')
		builder.connect_signals(self)
		
		# The functions builder.get_object() can be used to access 
		# the widgets in the interface by the names assigned to them 
		# inside the UI description. 
		window = builder.get_object('window1')
		self.spinner1 = builder.get_object('spinner1')
		self.label1 = builder.get_object('label1')
		self.entry1 = builder.get_object('entry1')
		self.buttonStart = builder.get_object('buttonStart')
		self.buttonStop = builder.get_object('buttonStop')
		
		#  Set attributes
		window.set_border_width(10)
		window.set_size_request(320, 320)
		window.set_title("PyGObject - Spinner/Clock Demo")
		self.label1.set_text("Clock: ")
		self.buttonStop.set_sensitive(False)
		
		
		# Register callbacks
		self.buttonStart.connect("clicked", self.on_buttonStart_clicked)
		self.buttonStop.connect("clicked", self.on_buttonStop_clicked)
		window.connect("destroy", self.on_MyWindow_destroy)
		
		window.show_all()
		
	# function definition
	def on_buttonStart_clicked(self, widget, *args):
		""" Handles "clicked" event of buttonStart. """
		self.start_clock_timer()
		
	# function definition
	def on_buttonStop_clicked(self, widget, *args):
		""" Handles "clicked" event of buttonStop. """
		self.stop_clock_timer('Stopped from button')
		
	# function definition
	def on_MyWindow_destroy(self, widget, *args):
		""" Handles destroy event of main window. """
		# ensure the timeout function is stopped
		if self.timeout_id:
			GLib.source_remove(self.timeout_id)
			self.timeout_id = None
			Gtk.main_quit()
		
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
		self.buttonStart.set_sensitive(False)
		self.buttonStop.set_sensitive(True)
		self.spinner1.start()
		self.timeout_id = GLib.timeout_add(250, self.display_clock, None)
		
	# function definition
	def stop_clock_timer(self, alabeltext):
		""" Stop the timer. """
		if self.timeout_id:
			GLib.source_remove(self.timeout_id)
			self.timeout_id = None
			self.spinner1.stop()
			self.buttonStart.set_sensitive(True)
			self.buttonStop.set_sensitive(False)
			self.label1.set_label(alabeltext)
			
	
			
#-----------------------------------------------------------------------
# main function
def main():
	
	window = MyWindow()
	
	# GTK main loop
	Gtk.main()
#-----------------------------------------------------------------------
		
if __name__ == '__main__':
    main()
