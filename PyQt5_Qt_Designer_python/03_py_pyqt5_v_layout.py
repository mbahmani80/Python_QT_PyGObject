#!/usr/bin/python3
#***********************************************************************
#          FILES:
#                03_py_pyqt5_v_layout.py
#            
#          USAGE: 
#				 ./03_py_pyqt5_v_layout.py
#				or
#				  python3 03_py_pyqt5_v_layout.py
# 
#    DESCRIPTION: PyQt Form Vertical layout example
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

		self.initUI()
	
	# function definition
	def initUI(self):
		
		# Create Widgets
		layout = QVBoxLayout()
		label1 = QLabel('PyQt Form Vertical layout example:')
		qtbtn  = QPushButton('Top')
		qcbtn  = QPushButton('Center')
		qbbtn  = QPushButton('Bottom')
		
		
		# Set attributes
		self.resize(280,150)
		self.setWindowTitle('PyQt5 - QVBoxLayout')
		
		# Pack everything and display
		layout.addWidget(label1)
		layout.addWidget(qtbtn)
		layout.addWidget(qcbtn)
		layout.addWidget(qbbtn)
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
