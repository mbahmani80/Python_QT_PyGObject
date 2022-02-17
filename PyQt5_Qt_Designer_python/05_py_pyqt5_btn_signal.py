#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                05_py_pyqt5_btn_signal.py
#            
#          USAGE: 
#				 ./05_py_pyqt5_btn_signal.py
#				or
#				  python3 05_py_pyqt5_btn_signal.py
# 
#    DESCRIPTION: In this program, I try to create a modular code using 
#                 a class to creating three QPushButtons and connecting 
#				  each signal which related to each QPushButton to a 
#				  separate function. In this program, we will also get 
#                 acquainted with the concepts of Signals, Slots, 
#				  and functions
# 
#        OPTIONS: ---
#   REQUIREMENTS: Python, Qt5
#           BUGS: ---
#          NOTES: Qt5 Python tutorial
#         AUTHOR: Mahdi Bahmani (www.itstorage.co)
#   ORGANIZATION: merdasco
#        CREATED: 2020/05/22 22:11:21
#    LAST EDITED: 
#       REVISION: 1.1
#**********************************************************************/
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
#-----------------------------------------------------------------------

# Window class definition
class MyMainWindow(QWidget):
	
	# Initializer function
	def __init__(self):
		super().__init__()
		
		# Initial Parameters
		self.title = 'PyQt5 Form'
		self.left = 500
		self.top = 500
		self.width = 220
		self.height = 150
		self.initUI()


	def initUI(self):

		# Create Widgets
		layout = QVBoxLayout()
		self.label1 = QLabel(self)
		button1 = QPushButton('Run a Function---button1')
		button2 = QPushButton('Change Label---button2')	
		button3 = QPushButton('exit---button3')
		
		# Set attributes
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)		
		self.label1.setText('QPushButton, QLabel, Signal, Slot and function')
		
		# Register SIGNALS/SLOTS
		button1.clicked.connect(self.on_button1_clicked)
		button2.clicked.connect(self.on_button2_clicked)
		button3.clicked.connect(self.on_button3_clicked)
        
		# Pack everything and display
		layout.addWidget(self.label1)
		layout.addWidget(button1)
		layout.addWidget(button2)
		layout.addWidget(button3)
		self.setLayout(layout)
		
		# Display
		self.show()	
	
	# function definition
	def on_button1_clicked(self):
		print("button1 clicked")
	
	# function definition
	def on_button2_clicked(self):
		self.label1.setText("button2 clicked")
	
	# function definition
	def on_button3_clicked(self):
		self.close()
#----------------------------------------------------------------------- 
# main function
def main():
	
	# Initialize the environment 
	app = QtWidgets.QApplication(sys.argv)
	window = MyMainWindow()
	sys.exit(app.exec_())
#----------------------------------------------------------------------- 		
if __name__ == '__main__':
    main()
