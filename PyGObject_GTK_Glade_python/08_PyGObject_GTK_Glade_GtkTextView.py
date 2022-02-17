#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                08_PyGObject_GTK_Glade_GtkTextView.py
#				 glade/08_PyGObject_GTK_Glade_GtkTextView.glade
#
#            
#          USAGE: 
#				 ./08_PyGObject_GTK_Glade_GtkTextView.py
#				or
#				  python3 08_PyGObject_GTK_Glade_GtkTextView.py
# 
#   DESCRIPTION: GtkTextView, GtkTextBuffer, GtkScrolledWindow
#				 GtkToolbar, GtkToolButton, GtkRadioToolButton
#				 GtkSeparatorToolItem
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
from gi.repository import Gtk, GLib, GObject, Pango
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
		builder.add_from_file('glade/08_PyGObject_GTK_Glade_GtkTextView.glade')
		builder.connect_signals(self)
		
		# The functions builder.get_object() can be used to access 
		# the widgets in the interface by the names assigned to them 
		# inside the UI description. 
		window = builder.get_object('window1')
		self.btninsert = builder.get_object('button1')
		self.btnquit = builder.get_object('button2')
		self.btnappend = builder.get_object('button3')
		scrolled_window = builder.get_object('scrolledwindow1')
		self.textview1 = builder.get_object('textview1')
		self.textbuffer = self.textview1.get_buffer()
		self.check_editable = builder.get_object('chkbtn1')
		self.radio_wrapnone = builder.get_object('radiobtn1')
		self.radio_wrapchar = builder.get_object('radiobtn2')
		self.radio_wrapword = builder.get_object('radiobtn3')
		
		toolbar = builder.get_object('toolbar1')
		button_bold = builder.get_object('button_bold')
		button_italic = builder.get_object('button_italic')
		button_underline = builder.get_object('button_underline')
		radio_justifyleft = builder.get_object('radio_justifyleft')
		radio_justifycenter = builder.get_object('radio_justifycenter')
		radio_justifyright = builder.get_object('radio_justifyright')
		radio_justifyfill = builder.get_object('radio_justifyfill')
		
		self.tag_bold = self.textbuffer.create_tag("bold",
			weight=Pango.Weight.BOLD)
		self.tag_italic = self.textbuffer.create_tag("italic",
			style=Pango.Style.ITALIC)
		self.tag_underline = self.textbuffer.create_tag("underline",
			underline=Pango.Underline.SINGLE)
		self.tag_found = self.textbuffer.create_tag("found",
			background="yellow")
		
		#  Set attributes
		window.set_border_width(10)
		window.set_size_request(320, 300)
		window.set_title("PyGObject - GtkTextView")
		#self.textview1.set_wrap_mode(True)
		self.textview1.set_justification(Gtk.Justification.LEFT)
		scrolled_window.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
		self.check_editable.set_active(True)
        
		
		# Register callbacks
		self.btninsert.connect("clicked", self.on_btninsert_clicked)
		self.btnquit.connect("clicked", self.on_btnquit_clicked)
		self.btnappend.connect("clicked", self.on_btnappend_clicked)
		window.connect("destroy", self.on_MyWindow_destroy)
		self.check_editable.connect("toggled", self.on_editable_toggled)
		self.radio_wrapnone.connect("toggled", self.on_wrap_toggled,
			Gtk.WrapMode.NONE)
		self.radio_wrapchar.connect("toggled", self.on_wrap_toggled,
			Gtk.WrapMode.CHAR)
		self.radio_wrapword.connect("toggled", self.on_wrap_toggled,
			Gtk.WrapMode.WORD)
		button_bold.connect("clicked", self.on_button_clicked, self.tag_bold)
		button_italic.connect("clicked", self.on_button_clicked,
			self.tag_italic)
		button_underline.connect("clicked", self.on_button_clicked,
			self.tag_underline)
		radio_justifyleft.connect("toggled", self.on_justify_toggled,
			Gtk.Justification.LEFT)
		radio_justifycenter.connect("toggled", self.on_justify_toggled,
			Gtk.Justification.CENTER)
		radio_justifyright.connect("toggled", self.on_justify_toggled,
			Gtk.Justification.RIGHT)
		radio_justifyfill.connect("toggled", self.on_justify_toggled,
			Gtk.Justification.FILL)
		
		
		window.show_all()
		
	# function definition
	def on_btninsert_clicked(self, widget, *args):
		self.textbuffer.set_text("Knowledge is Power is a True Saying.\n"
		+ "What about you?\n")
		iter = self.textbuffer.get_end_iter()
		self.textbuffer.insert(iter, "Are you agree?\n")

	def on_btnappend_clicked(self, widget, *args):
		iter = self.textbuffer.get_end_iter()
		self.textbuffer.insert(iter, 
			"Knowledge is Power is a True Saying. What about you?"
			+ "Are you agree? What do you think.\n")
		
	# function definition
	def on_btnquit_clicked(self, widget, *args):
		Gtk.main_quit()
		
	def on_editable_toggled(self, widget):
	    self.textview1.set_editable(widget.get_active())
	
	def on_wrap_toggled(self, widget, mode):
	    self.textview1.set_wrap_mode(mode)
	
	def on_MyWindow_destroy(self, widget):
		Gtk.main_quit()
	
	def on_justify_toggled(self, widget, justification):
	    self.textview1.set_justification(justification)
	    
	def on_button_clicked(self, widget, tag):
	    bounds = self.textbuffer.get_selection_bounds()
	    if len(bounds) != 0:
	        start, end = bounds
	        self.textbuffer.apply_tag(tag, start, end)
		

			
#-----------------------------------------------------------------------
# main function
def main():
	
	window = MyWindow()
	
	# GTK main loop
	Gtk.main()
#-----------------------------------------------------------------------
		
if __name__ == '__main__':
    main()


