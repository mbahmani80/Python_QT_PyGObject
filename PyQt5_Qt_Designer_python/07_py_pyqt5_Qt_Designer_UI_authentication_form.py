#!/usr/bin/env python3
#===============================================================================
# 
#          FILES:
#                07_py_pyqt5_Qt_Designer_UI_authentication_form.py
#                07_py_pyqt5_Qt_Designer_UI_authentication_form.ui
#
#         USAGE: ./07_py_pyqt5_Qt_Designer_UI_authentication_form.py
# 
#   DESCRIPTION: This program is an Authentication form consists of 
#                 QPushButtons, QLabel, and QLineEdit with fully 
#                 separated Header and Implementation Files , and 
#                 standard use of the class, signals, and slots.
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
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys
#-----------------------------------------------------------------------

# Window class definition
class MyMainWindow(QMainWindow):
	
	# initialize class var
	counter = 0
	
	# Initializer function
	def __init__(self):
		super(MyMainWindow, self).__init__()
		
		# Read Qt Designer .ui
		uic.loadUi("ui/07_py_pyqt5_Qt_Designer_UI_authentication_form.ui", self)
 
        # find the widgets in the xml file
 		# The functions findChild() can be used to access 
		# the widgets in the interface by the names assigned to them 
		# inside the UI description.
		self.label1 = self.findChild(QLabel, "label1")
		self.label2 = self.findChild(QLabel, "label2")
		self.button = self.findChild(QPushButton, "pushButton")
		
		# Set attributes 
		self.setWindowTitle('py_pyqt5_Qt_Designer')
		
		# Register SIGNALS/SLOTS
		self.button.clicked.connect(self.clickedBtn)
		
		# Display
		self.show()
 
	# function definition
	def clickedBtn(self):
		self.counter += 1
		str1 = "pushButton clicked: " + str(self.counter)
		str2 = str(self.counter)
		self.label1.setText(str1)
		self.label2.setText(str2)
		print(str1)
		print(str2)
		
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
