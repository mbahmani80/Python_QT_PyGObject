#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                02_py_pyqt5_hello.py
#            
#          USAGE: 
#				 ./02_py_pyqt5_hello.py
#				or
#				  python3 02_py_pyqt5_hello.py
# 
#    DESCRIPTION: In this example there is a class to create a 
#				  form with a QLabel to show a message.
# 
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
from PyQt5 import QtWidgets

import sys
#-----------------------------------------------------------------------
# Window class definition
class MyMainWindow(QtWidgets.QMainWindow):
	
	# Initializer function
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
        # Create Widgets
		label = QtWidgets.QLabel("Hello World")
		
		# Set attributes
		self.setWindowTitle("itstorage.co")
		self.resize(220,150)
		
		# Pack everything and display
		label.setMargin(60)
		self.setCentralWidget(label)
		
		# Display
		self.show()
#-----------------------------------------------------------------------	
if __name__ == '__main__':
	
	# Initialize the environment 
	app = QtWidgets.QApplication(sys.argv)
	window = MyMainWindow()
	app.exec()
