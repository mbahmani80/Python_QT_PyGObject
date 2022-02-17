#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                25_py_mp3_player_lyrics_GUI.py
#				 glade/25_py_mp3_player_lyrics_GUI.glade
#            
#          USAGE: 
#				 ./25_py_mp3_player_lyrics_GUI.py
#				or
#				  python3 25_py_mp3_player_lyrics_GUI.py
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
import eyed3
import keyboard 
import vlc
import fnmatch, os, io, sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio, GObject
from multiprocessing.dummy import Pool as ThreadPool
# import standard libraries
from os.path import basename, expanduser, isfile, join as joined

try:
    unicode        # Python 2
except NameError:
    unicode = str  # Python 3

#-----------------------------------------------------------------------

list_of_dvd = [["The Usual Suspects"],
               ["Gilda"],
               ["The Godfather"],
               ["Pulp Fiction"],
               ["Once Upon a Time in the West"],
               ["Rear Window"]]
 
########################################################################
# ------ func_play_show_mp3_tags_info(mp3name, repeat_numbers) ------- #


		
class Song(GObject.GObject):

	#filename = GObject.Property(type=str)
	#filetype = GObject.Property(type=str, default="mp3")
	#playlist = GObject.Property(type=widget)
	#textbuffer1 = GObject.Property(type=Gtk.TextBuffer)
	
	def __init__(self, filename, playlist, textbuffer, playrepeat, progressbar):
		
		GObject.GObject.__init__(self)
		self.playlist = playlist
		self.filename = filename
		self.textbuffer = textbuffer
		self.playrepeat = playrepeat
		self.progressbar = progressbar
		
		# VLC player controls
		try:
			self.rep = '--input-repeat=' + str(self.playrepeat)
			self.Instance = vlc.Instance(self.rep)
		except NameError:
			raise Exception("ERROR: VLC is not installed")
		self.player = self.Instance.media_player_new()
		
        
		
	def on_play(self):
		""" Function doc """
		if isfile(self.filename):  # Creation
			self.media = self.Instance.media_new(unicode(self.filename))
			self.player.set_media(self.media)
			self.player.play()
		
		
	def on_play_mp3_show_tags(self):
			# handle I/O error
			rep = 0
			try:

				mediafile = eyed3.load(self.filename)
				if mediafile:
					print (mediafile.tag.artist)
					print (mediafile.tag.album)
					print (mediafile.tag.title)
					# handle index error
					try:
						print (mediafile.tag.lyrics[0].text)
						self.textbuffer.set_text(mediafile.tag.lyrics[0].text)
					except IndexError:
						print("The lyric part is empty. ...!")
				else:
					print("There is no tag information ...!")

			except IOError:
					print("I/O Error! ...")
			except :
				print("Unknown error occurred!...")
				self.textbuffer.set_text('The lyric part is empty. ...')
				
	def on_pause(self):
		"""Pause the player.
		"""
		self.player.pause()


	def on_stop(self):
		"""Stop the player.
		"""
		self.player.stop()
		# reset the time slider
		#self.timeslider.SetValue(0)
		#self.timer.Stop()

		
		
		
		print("Disable play, pause, button, and progressbar")
	
	def OnTimer(self, evt):
		"""Update the time slider according to the current movie time.
		"""
		# since the self.player.get_length can change while playing,
		# re-set the timeslider to the correct range.
		length = self.player.get_length()
		##self.timeslider.SetRange(-1, length)
		
		# update the time on the slider
		time = self.player.get_time()
		##self.timeslider.SetValue(time)
	
	
#-----------------------------------------------------------------------
# class is used to manipulate window widgets
class MyWindow(Gtk.Window):
	
	timeout_id = None
	playrepeat1 = 2
	currentmp3name = "./25_py_mp3_player_lyrics_GUI.mp3"
	playlist = []
	# Initializer function
	def __init__(self):
		

		# A Gtk.Builder is an auxiliary object that reads textual 
		# descriptions of a user interface and instantiates the 
		# described objects. 
		builder = Gtk.Builder()
		
		# Import UI designed via Glade and connect signals
		builder.add_from_file('glade/25_py_mp3_player_lyrics_GUI.glade')
		builder.connect_signals(self)
		
		# The functions builder.get_object() can be used to access 
		# the widgets in the interface by the names assigned to them 
		# inside the UI description. 
		window = builder.get_object('window1')
		self.menuitem1 = builder.get_object('menuitem1')
		self.miopen = builder.get_object('miopen')
		self.miquit = builder.get_object('miquit')
		self.treeview1 = builder.get_object('treeview1')
		self.textview1 = builder.get_object('textview1')
		self.textbuffer1 = self.textview1.get_buffer()
		self.playbtn = builder.get_object('button1')
		self.pausebtn = builder.get_object('button2')
		self.previousbtn = builder.get_object('button3')
		self.nextbtn = builder.get_object('button4')
		self.stopbtn = builder.get_object('button5')
		self.radiobtn1 = builder.get_object('rbutton1')
		self.radiobtn2 = builder.get_object('rbutton2')
		self.radiobtn3 = builder.get_object('rbutton3')
		self.radiobtn4 = builder.get_object('rbutton4')
		self.radiobtn5 = builder.get_object('rbutton5')
		self.radiobtn6 = builder.get_object('rbutton6')
		self.progressbar1 = builder.get_object('progressbar1')
		
		

		
		#  Set attributes
		window.set_border_width(10)
		window.set_size_request(320, 320)
		window.set_title("PyGObject - Spinner Demo")
		self.playbtn.set_sensitive(False)
		#self.entry1.set_text('10')
		#self.label1.set_text("Remaining: ")
		#self.buttonStop.set_sensitive(False)
		#self.treeView1.set_rules_hint(True)
		
		
		# Register callbacks
		#self.buttonStop.connect("clicked", self.on_buttonStop_clicked)
		self.miopen.connect("activate", self.on_miopen_activate)
		self.miquit.connect("activate", self.on_miquit_activate)
		self.treeview1.connect("row-activated", self.on_treeview1_activated)
		self.playbtn.connect("clicked", self.on_playbtn_clicked)
		self.pausebtn.connect("clicked", self.on_pausebtn_clicked)
		self.previousbtn.connect("clicked", self.on_previousbtn_clicked)
		self.nextbtn.connect("clicked", self.on_nextbtn_clicked)
		self.stopbtn.connect("clicked", self.on_stopbtn_clicked)
		
		self.radiobtn1.connect("toggled", self.on_repeat_toggled)
		self.radiobtn2.connect("toggled", self.on_repeat_toggled)
		self.radiobtn3.connect("toggled", self.on_repeat_toggled)
		self.radiobtn4.connect("toggled", self.on_repeat_toggled)
		self.radiobtn5.connect("toggled", self.on_repeat_toggled)
		self.radiobtn6.connect("toggled", self.on_repeat_toggled)
		
		window.connect("destroy", self.on_MyWindow_destroy)
		
		#creating the treeview columns
		self.on_treeView_create_model_columns(self.treeview1)
		
		#(self, filename, playlist, textbuffer, playrepeat, progressbar)
		self.song = Song(self.currentmp3name,self.playlist, self.textbuffer1,
					self.playrepeat1, self.progressbar1)
	
		window.show_all()
	
	
	def on_treeView_create_model_columns(self, treeview):
		# the data are stored in the model
		# create a liststore with one column
		self.listmodel = Gtk.ListStore(str,str)
		#for i in range(len(list_of_dvd)):
		#	self.listmodel.append(list_of_dvd[i])
			
		self.treeview1.set_model(self.listmodel)
		for i, column_title in enumerate(["Title", "Path"]):
		#for i, column_title in enumerate(["Title"]):
			renderer = Gtk.CellRendererText()
			column = Gtk.TreeViewColumn(column_title, renderer, text=i)
			column.set_clickable(True)   
			column.set_resizable(True)
			treeview.append_column(column)
	
	def on_add_filters(self, dialog):
		filter_mp3 = Gtk.FileFilter()
		filter_mp3.set_name("Mp3 files")
		filter_mp3.add_mime_type("audio/mp3")
		dialog.add_filter(filter_mp3)
	
		filter_ply = Gtk.FileFilter()
		filter_ply.set_name("Playlist")
		filter_ply.add_mime_type("text/plain")
		dialog.add_filter(filter_ply)
	
		filter_any = Gtk.FileFilter()
		filter_any.set_name("Any files")
		filter_any.add_pattern("*")
		dialog.add_filter(filter_any)
			   
	# function definition
	def on_miopen_activate(self, event):
		# create a filechooserdialog to open:
		open_dialog = Gtk.FileChooserDialog()
		open_dialog.set_select_multiple(True)
		open_dialog.set_action(Gtk.FileChooserAction.OPEN)
		open_dialog.set_title("Open Files")
		open_dialog.add_button('Cancel', Gtk.ResponseType.CANCEL)
		open_dialog.add_button('Open', Gtk.ResponseType.OK)
		
		self.on_add_filters(open_dialog)
		
		# not only local files can be selected in the file selector
		open_dialog.set_local_only(False)
		# dialog always on top of the textview window
		open_dialog.set_modal(True)
		# connect the dialog with the callback function open_response_cb()
		open_dialog.connect("response", self.open_response_cb)
		# show the dialog
		open_dialog.show()

	# callback function for the dialog open_dialog
	def open_response_cb(self, dialog, response_id):
		open_dialog = dialog
		# if response is "ACCEPT" (the button "Open" has been clicked)
		if response_id == Gtk.ResponseType.OK:
			 
			# self.filelists are the files that we get from the FileChooserDialog
			self.filelists = sorted(open_dialog.get_filenames())
			
			for i in range(len(self.filelists)):
				mp3name=os.path.basename(self.filelists[i])
				basename=os.path.dirname(self.filelists[i])
				# append to the model the title that is in the entry
				self.listmodel.append([mp3name,basename])

		# if response is "CANCEL" (the button "Cancel" has been clicked)
		elif response_id == Gtk.ResponseType.CANCEL:
			print("cancelled: FileChooserAction.OPEN")
		# destroy the FileChooserDialog
		dialog.destroy()
		 
	def on_treeview1_activated(self, widget, row, col):
		model = widget.get_model()
		self.currentmp3name = model[row][1] + "/" + model[row][0]
		#self.statusbar.push(0, text)	
		print(self.currentmp3name)
		
		# filename, textbuffer, playrepeat, progressbar
		self.song.filename = self.currentmp3name
		self.song.playrepeat = self.playrepeat1
		self.song.on_play_mp3_show_tags()
		self.song.on_play()
		self.playbtn.set_sensitive(True)
	# not ok
	def on_treeview1_select_cursor_row (self, treeview, liststore):
		# get the file treeview and liststore
		file_view = treeview
		file_list = liststore
		# get the selected rows as paths
		sel_model, sel_rows = file_view.get_selection ().get_selected_rows ()
		# store the treeiters from paths
		iters = []
		for row in sel_rows:
			iters.append ( file_list.get_iter (row) )
		# remove the rows (treeiters)
		for i in iters:
			if i is not None:
				file_list.remove (i)
	
		
	# function definition	
	def on_miquit_activate(self, widget, *args):
		Gtk.main_quit()

	
	def on_playbtn_clicked(self, widget, *args):
		print("on_playbtn_clicked")
		self.song.on_play()
	
	def on_pausebtn_clicked(self, widget, *args):
		print("on_pausebtn_clicked")
		self.song.on_pause()
		if self.song.player.is_playing():
			self.playbtn.set_sensitive(False)
			self.pausebtn.set_sensitive(True)
			print("Disable play pause button")
		else:
			self.playbtn.set_sensitive(True)
			self.pausebtn.set_sensitive(True)

			print("Disable play pause button")
		
		#self.playbtn.set_sensitive(True)
		#self.pausebtn.set_sensitive(False)
		#self.previousbtn.set_sensitive(False)
		#self.nextbtn.set_sensitive(False)
		#self.stopbtn.set_sensitive(False)
	
	def on_previousbtn_clicked(self, widget, *args):
		print("on_previousbtn_clicked")
	
	def on_nextbtn_clicked(self, widget, *args):
		print("on_nextbtn_clicked")
	
	def on_stopbtn_clicked(self, widget, *args):
		self.song.on_stop()
		self.playbtn.set_sensitive(True)
		self.pausebtn.set_sensitive(False)
		self.previousbtn.set_sensitive(False)
		self.nextbtn.set_sensitive(False)
		self.stopbtn.set_sensitive(False)
	
	def on_repeat_toggled(self, rbutton):
		# a string to describe the state of the button
		state = "unknown"
		# whenever the button is turned on, state is on
		if rbutton.get_active():
			state = "on"
			l=str(rbutton.get_label())
			self.playrepeat1 = self.on_switch(l)
		# else state is off
		else:
			state = "off"
		# whenever the function is called (a button is turned on or off)
		# print on the terminal which button was turned on/off
		print(rbutton.get_label() + " was turned " + state)
		print(self.playrepeat1)
		self.song.playrepeat = self.playrepeat1
		#self.song.on_stop()
		
	def on_switch(self,argument):
	    switcher = {
	        "2": "2",
	        "3": "3",
	        "5": "5",
	        "10": "10",
	        "Loop": "100",
	        "No": "1"
	    }
	    # default, could also just omit condition
	    return switcher.get(argument, "1")
    
	# function definition
	def on_MyWindow_destroy(self, widget, *args):
		""" Handles destroy event of main window. """
		self.song.on_stop()
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

#https://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html
#https://stackoverflow.com/questions/54078538/get-selected-object-from-listbox-binded-to-liststore-in-python-gtk
