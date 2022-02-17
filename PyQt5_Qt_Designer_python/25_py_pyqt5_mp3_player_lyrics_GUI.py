#!/usr/bin/env python3
#===============================================================================
# 
#          FILES:
#                25_py_pyqt5_mp3_player_lyrics_GUI.py
#                25_py_pyqt5_mp3_player_lyrics_GUI.ui
#
#         USAGE: ./25_py_pyqt5_mp3_player_lyrics_GUI.py
# 
#   DESCRIPTION: This program creates a simple form with a TextEdit and 
#				 two push Buttons to illustrate the usage of signal 
#				 handling and importing designed UI in Qt Designer. 
#                
# 
#       OPTIONS: ---
#  REQUIREMENTS: QT5, Qt Designer, Python3
#          BUGS: ---
#         NOTES: PyQt5 Qt Designer tutorial
#        AUTHOR: Mahdi Bahmani (), 
#  ORGANIZATION: www.itstorage.co
#       CREATED: 13.05.2020 18:59:07
#   LAST EDITED: 
#      REVISION: 1.1
#===============================================================================


import os
import pathlib
import re
import sys
import vlc, eyed3
import time, datetime
from PyQt5.QtCore import pyqtSignal, QTimer
from itertools import count
from threading import Event
from datetime import datetime, timedelta

from os.path import basename, expanduser, isfile
from threading import Timer

import PyQt5.uic
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import (QDate, QDateTime, QRegExp, 
						  QSortFilterProxyModel, Qt,
						  QTime, QThread)
						  
from PyQt5.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, 
							 QFileSystemModel, QHBoxLayout, QLabel, 
							 QMessageBox, QTreeView, QAction, 
                             QVBoxLayout, QWidget, QTreeWidgetItem, 
                             QTreeWidget, QPlainTextEdit, QPushButton, 
                             QDialog, QStatusBar, QSpinBox, QSlider)
                             
#-----------------------------------------------------------------------
try:
    unicode        # Python 2
except NameError:
    unicode = str  # Python 3

#-----------------------------------------------------------------------
GPLlicense="""
					GNU GENERAL PUBLIC LICENSE
						Version 2, June 1991
                       
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.
  
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 """

########################################################################
TIME_LIMIT = 100

class External(QThread):
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count +=1
            time.sleep(1)
            self.countChanged.emit(count)
            
########################################################################
# ------ func_play_show_mp3_tags_info(mp3name, repeat_numbers) ------- #

class Player_Class():
	
	# Initializer function
	def __init__(self):
		#options = '--input-repeat=1'
		self.vlcPlayer = None
		self.media = None
		self.media_list = None
		self.duration = 0
		self.played = count()
		#self.finished = Event()
		self.finished = 0
		self.is_player_active = False
		self.is_playing = False
		self.player_paused = True
		self.player_stoped = True

		
		
		
    # VLC player controls
	#def on_setup_player(self, options):
	def on_setup_player(self):
		try:
			#self.vlcInstance = vlc.Instance(options)
			self.vlcInstance = vlc.Instance('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
        
		except NameError:
			raise Exception("ERROR: VLC is not installed")
			
		#Create a MediaPlayer with the default instance
		self.vlcPlayer = self.vlcInstance.media_player_new()
		#self.vlcPlayer.set_xwindow(self.win_id)
		self.media_list = self.vlcInstance.media_list_new()
		self.media_list_player = self.vlcInstance.media_list_player_new()
		self.media_list_player.set_media_player(self.vlcPlayer)
		event_manager = self.vlcPlayer.event_manager()
		#event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.on_end_reached)
		
		event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, self.SongFinished)
		
	
	def on_add_media(self, filename):
		""" Function on_play """
		if isfile(filename):  # Creation
			#Load the media file
			self.media = self.vlcInstance.media_new(unicode(filename))
			#Add the media to the player
			self.vlcPlayer.set_media(self.media)
			
	def on_play(self):
		""" Function on_play """
		#self.vlcPlayer.is_player_active = True
		self.player_paused = False
		self.player_stoped = False
		self.is_playing = True
		self.is_player_active = True
		self.vlcPlayer.play()
	
	def on_add_media_list(self,listname):
		for i in range(len(listname)):
			print(listname[i])
			self.media_list.add_media(unicode(listname[i]))
     
	def on_play_list(self):
		self.media_list_player.set_media_list(self.media_list)
		self.media_list_player.play()
#-----------------------------------------------------------------------    
	def on_wait(self):
		self.finished.wait()
#-----------------------------------------------------------------------	
	def SongFinished(self, event):
		print ("Event reports - finished")
		self.is_player_active = False
		self.is_playing = False
		self.player_paused = True
		self.player_stoped= True
		self.finished = 1
#-----------------------------------------------------------------------    
	def on_end_reached(self, event):
		if event.type.value == vlc.EventType.MediaPlayerEndReached.value:
			if next(self.played) == self.media_list.count():
				self.finished.set()
#-----------------------------------------------------------------------			
	def on_play_mp3_show_tags_duration(self, filename,plaintextedit):
			# handle I/O error
			rep = 0
			try:

				self.mediafiletag = eyed3.load(filename)
				if self.mediafiletag:
					print (self.mediafiletag.tag.artist)
					print (self.mediafiletag.tag.album)
					print (self.mediafiletag.tag.title)
					# handle index error
					try:
						print (self.mediafiletag.tag.lyrics[0].text)
						plaintextedit.clear()
						plaintextedit.insertPlainText(self.mediafiletag.tag.lyrics[0].text)
					except IndexError:
						print("The lyric part is empty. ...!")
				else:
					print("There is no tag information ...!")

			except IOError:
					print("I/O Error! ...")
			except :
				print("Unknown error occurred!...")
				plaintextedit.insertPlainText("The lyric part is empty. ...")
#-----------------------------------------------------------------------				
	def on_pause(self):
		"""Pause the player.
		"""
		self.is_player_active = True
		self.is_playing = False
		self.player_paused = True
		self.player_stop = False
		self.vlcPlayer.pause()
#-----------------------------------------------------------------------
	def on_stop(self):
		"""Stop the player.
		"""
		self.is_player_active = False
		self.is_playing = False
		self.player_paused = True
		self.player_stop = True
		self.vlcPlayer.stop()
		print("on_stop")
	
	def on_get_duration(self,filename):
		mediafilelen = eyed3.load(filename)
		self.duration = int(mediafilelen.info.time_secs)
		#self.duration = self.mediafiletag.info.time_secs
		#duration = self.vlcPlayer.get_length() / 1000
		#mm, ss = divmod(duration, 60)
		#print(ss)
		return self.duration
	
	def OnTimer(self, evt):
		"""Update the time slider according to the current movie time.
		"""
		# since the self.vlcPlayer.get_length can change while playing,
		# re-set the timeslider to the correct range.
		length = self.vlcPlayer.get_length()
		##self.timeslider.SetRange(-1, length)
		
		# update the time on the slider
		time = self.vlcPlayer.get_time()
		##self.timeslider.SetValue(time)
#-----------------------------------------------------------------------
# class is used to manipulate window widgets
class MyMainWindow(QMainWindow):
	
	timer = None
	check_playall_state_id = None
	current_media_name = ""
	playrepeat = 1
	playlist = []
	tree_selection = None
	elapsed_time_tmp = 1
	total_time_tmp = 0
	elapsed_time = "--:--"
	total_time = "--:--"
	is_play_all_active = False
	TITLE, PATH = range(2)
	
	# Initializer function
	def __init__(self):
		super(MyMainWindow, self).__init__()
		
		# Read Qt Designer .ui
		uic.loadUi("ui/25_py_pyqt5_mp3_player_lyrics_GUI.ui", self)
 
        # find the widgets in the xml file
		# The functions findChild() can be used to access 
		# the widgets in the interface by the names assigned to them 
		# inside the UI description.
		self.miopen = self.findChild(QAction, "miopen")
		self.miopendir = self.findChild(QAction, "miopendir")
		self.miquit = self.findChild(QAction, "miquit")
		self.miabout = self.findChild(QAction, "miabout")
		self.treeView1 = self.findChild(QTreeView, "treeView1")
		self.statusbar = self.findChild(QStatusBar,"statusbar")
		self.plaintextedit = self.findChild(QPlainTextEdit, "plainTextEdit")
		self.playpausebtn = self.findChild(QPushButton, "playpausebtn")
		self.previousbtn = self.findChild(QPushButton, "previousbtn")
		self.nextbtn = self.findChild(QPushButton, "nextbtn")
		self.stopbtn = self.findChild(QPushButton, "stopbtn")
		self.clearlistbtn = self.findChild(QPushButton, "clearlistbtn")
		self.removebtn = self.findChild(QPushButton, "removebtn")
		self.playallbtn = self.findChild(QPushButton, "playallbtn")
		self.spinbox1 = self.findChild(QSpinBox, "spinbox1")
		self.progress = self.findChild(QSlider, "progress")
	
		# Register SIGNALS/SLOTS
		self.miopen.triggered.connect(self.clicked_miopen)
		self.miopendir.triggered.connect(self.clicked_miopendir)
		self.miquit.triggered.connect(self.clicked_miquit)
		self.miabout.triggered.connect(self.clicked_miabout)
		self.playpausebtn.clicked.connect(self.clicked_playpausebtn)
		self.previousbtn.clicked.connect(self.clicked_previousbtn)
		self.nextbtn.clicked.connect(self.clicked_nextbtn)
		self.stopbtn.clicked.connect(self.clicked_stopbtn)
		self.clearlistbtn.clicked.connect(self.clicked_clearlistbtn)
		self.removebtn.clicked.connect(self.clicked_removebtn)
		self.playallbtn.clicked.connect(self.clicked_playallbtn)
		self.treeView1.clicked.connect(self.on_treeview1_activated)
		self.progress.valueChanged[int].connect(self.on_progress_change_value)
		
		# Set attributes
		self.progress.setMaximum(100)
        ## treeview     
		self.treeView1.setRootIsDecorated(False)
		self.treeView1.setAlternatingRowColors(True)
		self.treeView1.setSortingEnabled(True)
		self.treeView1.sortByColumn( 0, Qt.AscendingOrder )
		self.treeView1.resizeColumnToContents(0)
		self.treeView1.setAlternatingRowColors(True)
		self.treeView1.setAnimated(True)
		self.model = self.on_treeView_create_model_columns(self)
		self.treeView1.setModel(self.model)
        
		self.setWindowTitle('py_pyqt5_Qt_Designer')
		
		# Create an object from C_Player Class
		self.C_Player = Player_Class()
		#self.C_Player.on_setup_player(self.options)
		self.C_Player.on_setup_player()
		
		
		
		# Display
		self.show()
#-----------------------------------------------------------------------
	def on_treeView_create_model_columns(self, parent):
		# the data are stored in the model
		# create a model with two columns
		model = QStandardItemModel(0, 2, parent)
		model.setHeaderData(self.TITLE, Qt.Horizontal, "Title")
		model.setHeaderData(self.PATH, Qt.Horizontal, "Path")
		return model
		
#-----------------------------------------------------------------------				
	def on_treeView_model_add_data(self,model, title, path):
		model.insertRow(0)
		model.setData(model.index(0, self.TITLE), title)
		model.setData(model.index(0, self.PATH), path)
#-----------------------------------------------------------------------			
	def on_treeview1_activated(self, index):
		print ("on_treeview1_activated")
		# Get the text and index of the current selected QTreeView item
		fname = self.treeView1.selectedIndexes()[0].data(Qt.DisplayRole)
		Path = self.treeView1.selectedIndexes()[1].data(Qt.DisplayRole)
		self.current_media_name = Path  + "/" + fname
		print(self.current_media_name)
		self.statusbar.showMessage(fname)
		#for ix in self.treeView1.selectedIndexes():
		#	text = ix.data(Qt.DisplayRole) # or ix.data()
		#	print(text)
		self.on_call_other_function_to_play(self.current_media_name)
		
#-----------------------------------------------------------------------
	# function definition
	def on_call_other_function_to_play(self, media_name):
		self.on_stop_progress_timer()
		self.C_Player.on_add_media(media_name)
		self.C_Player.on_play_mp3_show_tags_duration(media_name, self.plaintextedit)
		self.duration = self.C_Player.on_get_duration(media_name)
		self.C_Player.on_play()
		
		self.on_set_sensitive(True)
		self.playpausebtn.setIcon(QtGui.QIcon('ui/pause.png'))
		
		self.total_time_tmp = int(self.C_Player.on_get_duration(media_name))
		self.total_time = str("{:0>8}".format(str(timedelta(seconds=int(self.total_time_tmp)))))
		
		self.durationlabel1.setText(str(self.elapsed_time))
		self.durationlabel2.setText(str(self.total_time))
		# make QTimer
		self.timer = QTimer()
		# set interval to 1 s
		self.timer.setInterval(1000)# 1000 ms = 1 s
		
		#self.timer.setTimerType(QtCore.Qt.PreciseTimer)
		# connect timeout signal to signal handler
		self.timer.timeout.connect(self.update_progress_timer)
		self.timer.start()

#-----------------------------------------------------------------------
	# function definition
	def on_stop_progress_timer(self):
		""" Stop the timer. """
		if self.timer:
			self.timer.stop()
			self.timer.deleteLater()
		self.progress.setValue(0)
		self.elapsed_time_tmp = 1
		self.total_time_tmp = 0
		self.durationlabel2.setText("--:--")
		self.durationlabel1.setText("--:--")
		self.spinbox1.setEnabled(False)
		self.on_set_sensitive(False)
		self.playpausebtn.setIcon(QtGui.QIcon('ui/pause.png'))
		self.C_Player.finished = 0
		self.C_Player.on_stop()
#-----------------------------------------------------------------------	
	# function definition
	def update_progress_timer(self):
		if not self.C_Player.is_player_active:
			self.C_Player.is_playing = False
			self.C_Player.is_player_active = False
			self.C_Player.player_stoped = True
			self.on_stop_progress_timer()
			#self.timer.stop() # cancel timeout
			return False
		if not self.C_Player.player_paused and self.C_Player.is_playing:
			pos = self.progress.value()
			new_pos = (pos + 100 / self.duration)
			#self.progress.setValue(new_pos)
			
			self.elapsed_time_tmp += 1
			self.elapsed_time =str("{:0>8}".format(str(timedelta(seconds=int(self.elapsed_time_tmp)))))
			self.durationlabel1.setText(str(self.elapsed_time))
			#if new_pos > 100 and self.total_time < 0:
			if new_pos > 100:
				self.C_Player.is_playing = False
				self.C_Player.is_player_active = False
				self.C_Player.player_stoped = True
				self.on_stop_progress_timer()
				print("self.progress.get_value finished")
		return True # continue calling every x milliseconds
#-----------------------------------------------------------------------
	# function definition
	def on_set_sensitive(self, status):
		self.playpausebtn.setEnabled(status)
		self.previousbtn.setEnabled(status)
		self.nextbtn.setEnabled(status)
		self.stopbtn.setEnabled(status)
#-----------------------------------------------------------------------
	# function definition
	def on_progress_change_value(self, value):
		self.C_Player.vlcPlayer.set_position(int(value) / 100)
		self.progress.setValue(value)
#-----------------------------------------------------------------------	
	# function definition
	def clicked_miopen(self):
		print("clicked_miopen")
		open_dialog = QFileDialog(self)
		open_dialog.setWindowTitle('Open File')
		open_dialog.setNameFilter('Media (*.mp3 *.ogg *.mp4)')
		open_dialog.setFileMode(QFileDialog.ExistingFiles)
		if open_dialog.exec_() == QDialog.Accepted:
			self.filelists = sorted(open_dialog.selectedFiles(),reverse=True)
			for i in range(len(self.filelists)):
				mp3name=os.path.basename(self.filelists[i])
				basename=os.path.dirname(self.filelists[i])
				# append to the model the title that is in the entry
				self.on_treeView_model_add_data(self.model, mp3name,basename)
				#print(self.filelists[i])
		# if response is "CANCEL" (the button "Cancel" has been clicked)
		else:
			print("cancelled: open_dialog")
			
#-----------------------------------------------------------------------				
	# function definition
	def clicked_miopendir(self):
		print("clicked_miopendir")
	
	# function definition
	def clicked_miquit(self):
		print("clicked_miquit")
		QtCore.QCoreApplication.quit()
	
	# function definition
	def clicked_miabout(self):
		print("clicked_miabout")
	
	# function definition
	def clicked_playpausebtn(self):
		print("clicked_playpausebtn")
	
	# function definition
	def clicked_previousbtn(self):
		print("clicked_previousbtn")
	
	# function definition
	def clicked_nextbtn(self):
		print("clicked_nextbtn")
	
	# function definition
	def clicked_stopbtn(self):
		print("clicked_stopbtn")
		""" Stop the timer. """
		if self.timer:
			self.timer.stop()
			self.timer.deleteLater()
		self.C_Player.is_player_active = False
		self.check_playall_state_id = None
		self.C_Player.finished = 0
		self.index = 0
		self.on_stop_progress_timer()
		
	# function definition
	def clicked_clearlistbtn(self):
		print("clicked_clearlistbtn")
	
	# function definition
	def clicked_removebtn(self):
		print("clicked_removebtn")
		
	# function definition
	def clicked_playallbtn(self):
		print("clicked_playallbtn")
	
	# function definition
	def clickedBtn2(self):
		self.close()
 
#----------------------------------------------------------------------- 
# main function
def main():
	# Initialize the environment 
	app = QApplication(sys.argv)
	window = MyMainWindow()
	app.exec_()
#----------------------------------------------------------------------- 	
if __name__ == '__main__':
    main()
