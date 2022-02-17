#!/usr/bin/env python3
#===============================================================================
# 
#          FILES:
#                08_py_pyqt5_Qt_Designer_QTextEdit.py
#                08_py_pyqt5_Qt_Designer_QTextEdit.ui
#
#         USAGE: ./08_py_pyqt5_Qt_Designer_QTextEdit.py
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
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit
from PyQt5 import uic
import sys
 
#----------------------------------------------------------------------- 
# Window class definition
class MyMainWindow(QMainWindow):
	
	# Initializer function
	def __init__(self):
		super(MyMainWindow, self).__init__()
		
		# Read Qt Designer .ui
		uic.loadUi("ui/08_py_pyqt5_Qt_Designer_QTextEdit.ui", self)
 
        # find the widgets in the xml file
		# The functions findChild() can be used to access 
		# the widgets in the interface by the names assigned to them 
		# inside the UI description.
		self.textedit = self.findChild(QTextEdit, "textEdit")
		self.button = self.findChild(QPushButton, "pushButton")
		self.button2 = self.findChild(QPushButton, "pushButton2")
		
		
		# Register SIGNALS/SLOTS
		self.button.clicked.connect(self.clickedBtn)
		self.button2.clicked.connect(self.clickedBtn2)
		
		# Set attributes
		self.setWindowTitle('py_pyqt5_Qt_Designer')
		
		# Display
		self.show()
 
	# function definition
	def clickedBtn(self):
		self.textEdit.setPlainText("Knowledge is Power is a True Saying.")
	
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
