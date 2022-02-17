#  Filename: 01_PyGObject_GTK_hello.py
#  
#  Copyright 2020 Mahdi Bahmani <www.itstorage.co>
#
# sudo apt install python3-pyqt5 python3-pyside2.qtwidgets python3-qtpy -y
# sudo apt install qt5-qmake qt5-qmake-bin -y
# sudo apt install qttools5-dev-tools qttools5-dev qt5-default -y
# sudo apt-get install qtbase5-examples qtbase5-doc-html  qt5-doc qt5-doc-html -y
# sudo apt install qtcreator -y


# sudo apt install pyqt5-dev-tools pyqt5-dev -y
# sudo apt install python3-pyside2.qtcore pyside2-tools  -y
# sudo apt install python3-pyqt5.qtmultimedia -y

# sudo pip3 install PySide2

# https://pythonprogramminglanguage.com/pyqt5-hello-world/
#
from PyQt5 import QtWidgets

import sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("Hello World")
        l = QtWidgets.QLabel("My simple app.")
        l.setMargin(10)
        self.setCentralWidget(l)
        self.show()

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	w = MainWindow()
	app.exec()
