#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                04_PyGObject_GTK_h_layout.py
#            
#          USAGE: 
#				 ./04_PyGObject_GTK_h_layout.py
#				or
#				  python3 04_PyGObject_GTK_h_layout.py
# 
#    DESCRIPTION: PyGObject Form Horizontal layout example.
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
		self.box = Gtk.Box(spacing=6)
		self.label1 = Gtk.Label()
		self.button1 = Gtk.Button(label="Left")
		self.button2 = Gtk.Button(label="Center")
		self.button3 = Gtk.Button(label="Right")
		
		#  Set attributes
		self.label1.set_text('PyGObject Form Horizontal layout example:')
		self.set_size_request(300, 50)
		
		# Register callbacks		
		self.connect("destroy", Gtk.main_quit)
		
		# Pack everything and display
		self.add(self.box)
		self.box.pack_start(self.label1, True, True, 0)
		self.box.pack_start(self.button1, True, True, 0)
		self.box.pack_start(self.button2, True, True, 0)
		self.box.pack_start(self.button3, True, True, 0)
		self.show_all()
#-----------------------------------------------------------------------
# main function
def main():
	
	window = MyWindow()
	
	# GTK main loop
	Gtk.main()
#-----------------------------------------------------------------------
		
if __name__ == '__main__':
    main()
