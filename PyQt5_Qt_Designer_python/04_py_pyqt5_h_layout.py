#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                04_py_pyqt5_h_layout.py
#            
#          USAGE: 
#				 ./04_py_pyqt5_h_layout.py
#				or
#				  python3 04_py_pyqt5_h_layout.py
# 
#    DESCRIPTION: PyQt Form Horizontal layout example
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
#-----------------------------------------------------------------------
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
#-----------------------------------------------------------------------
# Window class definition
class MyMainWindow(QWidget):
	
	# Initializer function
	def __init__(self):
		super().__init__()

		self.initUI()
		
	# function definition
	def initUI(self):
		
		# Create Widgets
		layout = QHBoxLayout()
		label1 = QLabel('PyQt Form Horizontal layout example:')
		qlbtn = QPushButton('Left')
		qcbtn = QPushButton('Center')
		qrbtn = QPushButton('Right')
		
		# Set attributes
		self.resize(280,40)
		self.setWindowTitle('PyQt5 - QHBoxLayout')
		
		# Pack everything and display
		layout.addWidget(label1)
		layout.addWidget(qlbtn)
		layout.addWidget(qcbtn)
		layout.addWidget(qrbtn)
		self.setLayout(layout)
		
		# Display
		self.show()
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
