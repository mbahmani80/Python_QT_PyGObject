#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                11_PyGObject_GTK_Glade_spinner_countdown.py
#				 glade/11_PyGObject_GTK_Glade_spinner_countdown.glade
#            
#          USAGE: 
#				 ./11_PyGObject_GTK_Glade_spinner_countdown.py
#				or
#				  python3 11_PyGObject_GTK_Glade_spinner_countdown.py
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
import time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
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
		builder.add_from_file('glade/11_PyGObject_GTK_Glade_spinner_countdown.glade')
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
		window.set_title("PyGObject - Spinner Demo")
		self.entry1.set_text('10')
		self.label1.set_text("Remaining: ")
		self.buttonStop.set_sensitive(False)
		
		
		# Register callbacks
		self.buttonStart.connect("clicked", self.on_buttonStart_clicked)
		self.buttonStop.connect("clicked", self.on_buttonStop_clicked)
		window.connect("destroy", self.on_MyWindow_destroy)
		
		window.show_all()
		
	# function definition
	def on_buttonStart_clicked(self, widget, *args):
		""" Handles "clicked" event of buttonStart. """
		self.start_timer()
		
	# function definition
	def on_buttonStop_clicked(self, widget, *args):
		""" Handles "clicked" event of buttonStop. """
		self.stop_timer('Stopped from button')
		
	# function definition
	def on_MyWindow_destroy(self, widget, *args):
		""" Handles destroy event of main window. """
		# ensure the timeout function is stopped
		if self.timeout_id:
			GLib.source_remove(self.timeout_id)
			self.timeout_id = None
			Gtk.main_quit()
			
	# function definition
	def on_timeout(self, *args, **kwargs):
		""" A timeout function.

		Return True to stop it.
		This is not a precise timer since next timeout
		is recalculated based on the current time."""
		self.counter -= 1
		if self.counter <= 0:
			self.stop_timer('Reached time out')
			return False
		self.label1.set_label('Remaining: ' + str(int(self.counter / 4)))
		return True
		
	# function definition
	def start_timer(self):
		""" Start the timer. """
		self.buttonStart.set_sensitive(False)
		self.buttonStop.set_sensitive(True)
		# time out will check every 250 miliseconds (1/4 of a second)
		self.counter = 4 * int(self.entry1.get_text())
		self.label1.set_label('Remaining: ' + str(int(self.counter / 4)))
		self.spinner1.start()
		self.timeout_id = GLib.timeout_add(250, self.on_timeout, None)
	
	def on_countdown(t):
		while t:
			mins, secs = divmod(t, 60)
			timeformat = '{:02d}:{:02d}'.format(mins, secs)
			print(timeformat, end='\r')
			#print(timeformat)
			time.sleep(1)
			t -= 1
		print('Goodbye!\n\n\n\n\n')
	
	# function definition
	def stop_timer(self, alabeltext):
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

#https://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html
#https://www.darkartistry.com/2019/12/simple-python-3-threaded-timer-in-gtk3/
