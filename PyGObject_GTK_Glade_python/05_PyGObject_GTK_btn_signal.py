#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                05_PyGObject_GTK_btn_signal.py
#            
#          USAGE: 
#				 ./05_PyGObject_GTK_btn_signal.py
#				or
#				  python3 05_PyGObject_GTK_btn_signal.py
# 
#    DESCRIPTION: In this program, I try to create a modular code using 
#                 a class to creating three Gtk Buttons and connecting 
#				  each signal which related to each Button to a separate 
#				  function. In this program, we will also get acquainted
# 			      with the concepts of Signals, Events, and callbacks.
# 
#        OPTIONS: ---
#   REQUIREMENTS: Python, GTK
#           BUGS: ---
#          NOTES: PyGObject tutorial
#         AUTHOR: Mahdi Bahmani (www.itstorage.co)
#   ORGANIZATION: merdasco
#        CREATED: 2020/03/24 23:49
#    LAST EDITED: 
#       REVISION: 1.1
#**********************************************************************/
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
		Gtk.Window.__init__(self, title="PyGObject Form")
		self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.label1 = Gtk.Label()
		self.button1 = Gtk.Button(label="Run a Function---button1")
		self.button2 = Gtk.Button(label="Change Label---button2")
		self.button3 = Gtk.Button(label="exit---button3")
		
		#  Set attributes
		self.label1.set_text('Gtk.Button, Gtk.Label, Signal and function')
		self.set_size_request(300, 50)
		
		# Register callbacks
		self.connect("destroy", Gtk.main_quit)
		self.button1.connect("clicked", self.on_button1_clicked)
		self.button2.connect("clicked", self.on_button2_clicked)
		self.button3.connect("clicked", self.on_button3_clicked)
					
		# Pack everything and display
		self.add(self.box)
		self.box.pack_start(self.label1, True, True, 0)
		self.box.pack_start(self.button1, True, True, 0)
		self.box.pack_start(self.button2, True, True, 0)
		self.box.pack_start(self.button3, True, True, 0)
		self.show_all()
		
	# function definition
	def on_button1_clicked(self, widget):
		print("button1 clicked")
		
	# function definition
	def on_button2_clicked(self, widget):
		self.label1.set_text("button2 clicked")
		
	# function definition
	def on_button3_clicked(self, widget):
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
