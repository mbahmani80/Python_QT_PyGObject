#!/usr/bin/env python3
#===============================================================================
# 
#          FILES:
#                26_py_pyqt5_mp3_player_lyrics_GUI.py
#                26_py_pyqt5_mp3_player_lyrics_GUI.ui
#
#         USAGE: ./26_py_pyqt5_mp3_player_lyrics_GUI.py
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
						  QTime, QThread, QUrl)
						  
from PyQt5.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel, QPalette
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, 
							 QFileSystemModel, QHBoxLayout, QLabel, 
							 QMessageBox, QTreeView, QAction, 
                             QVBoxLayout, QWidget, QTreeWidgetItem, 
                             QTreeWidget, QPlainTextEdit, QPushButton, 
                             QDialog, QStatusBar, QSpinBox, QSlider,
                             QStyle)

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
                          
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
		uic.loadUi("ui/26_py_pyqt5_mp3_player_lyrics_GUI.ui", self)
 
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
		self.slider = self.findChild(QSlider, "slider")
		
		#create media player object
		self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
	
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
		#self.progress.valueChanged[int].connect(self.on_progress_change_value)
		
		
		self.slider.sliderMoved.connect(self.set_position)
		
		#media player signals
		self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
		self.mediaPlayer.positionChanged.connect(self.position_changed)
		self.mediaPlayer.durationChanged.connect(self.duration_changed)
		
		# Set attributes
		self.slider.setRange(0,0)
		self.playpausebtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
		self.playpausebtn.clicked.connect(self.play_video)
        
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
		
		self.duration = self.C_Player.on_get_duration(media_name)
		
		
		#self.on_set_sensitive(True)
		#self.playpausebtn.setIcon(QtGui.QIcon('ui/pause.png'))
		
		self.total_time_tmp = int(self.C_Player.on_get_duration(media_name))
		self.total_time = str("{:0>8}".format(str(timedelta(seconds=int(self.total_time_tmp)))))
		
		self.durationlabel1.setText(str(self.elapsed_time))
		self.durationlabel2.setText(str(self.total_time))
		

#-----------------------------------------------------------------------
	# function definition
	def on_stop_progress_timer(self):
		""" Stop the timer. """
		self.slider.setValue(0)
		self.elapsed_time_tmp = 1
		self.total_time_tmp = 0
		self.durationlabel2.setText("--:--")
		self.durationlabel1.setText("--:--")
		self.spinbox1.setEnabled(False)
		self.on_set_sensitive(False)
		self.playpausebtn.setIcon(QtGui.QIcon('ui/pause.png'))

#-----------------------------------------------------------------------
	# function definition
	def on_set_sensitive(self, status):
		self.playpausebtn.setEnabled(status)
		self.previousbtn.setEnabled(status)
		self.nextbtn.setEnabled(status)
		self.stopbtn.setEnabled(status)
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
		self.check_playall_state_id = None
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

	def play_video(self):
		if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
			self.mediaPlayer.pause()
	
		else:
			self.mediaPlayer.play()
	
	
	def mediastate_changed(self, state):
		if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
			self.playBtn.setIcon(
				self.style().standardIcon(QStyle.SP_MediaPause)
	
			)
	
		else:
			self.playBtn.setIcon(
				self.style().standardIcon(QStyle.SP_MediaPlay)
	
			)
	
	def position_changed(self, position):
		self.slider.setValue(position)
	
	
	def duration_changed(self, duration):
		self.slider.setRange(0, duration)
	
	
	def set_position(self, position):
		self.mediaPlayer.setPosition(position)
	
	
	def handle_errors(self):
		self.playBtn.setEnabled(False)
		self.label.setText("Error: " + self.mediaPlayer.errorString())
		
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
