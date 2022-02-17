#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                01_py_pyqt5_simple_form.py
#            
#          USAGE: 
#				 ./01_py_pyqt5_simple_form.py
#				or
#				  python3 01_py_pyqt5_simple_form.py
# 
#    DESCRIPTION: This example shows a simple PyQt form
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
        
		# Set attributes
        self.setWindowTitle("Hello World (PyQt)")
        self.resize(260,150)
        
        # Display
        self.show()
#-----------------------------------------------------------------------

if __name__ == '__main__':
	
	# Initialize the environment 
	app = QtWidgets.QApplication(sys.argv)
	window = MyMainWindow()
	app.exec()
