import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)
                             
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
		okButton = QPushButton("OK")
		cancelButton = QPushButton("Cancel")
		vbox = QVBoxLayout()
		hbox = QHBoxLayout()
		
		# Set attributes
		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle('Buttons')
		hbox.addStretch(1)
		vbox.addStretch(1)
		
		# Pack everything and display
		hbox.addWidget(okButton)
		hbox.addWidget(cancelButton)    
		vbox.addLayout(hbox)
		self.setLayout(vbox)
		
		# Display
		self.show()
#-----------------------------------------------------------------------
# main function
def main():
	
	# Initialize the environment 
    app = QApplication(sys.argv)
    window = MyMainWindow()
    sys.exit(app.exec_())
#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
