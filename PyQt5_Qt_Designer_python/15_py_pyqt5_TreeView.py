import sys
from PyQt5.QtCore import *
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
 
class ItemDsplyr(QTreeView):
    def __init__(self):
        QTreeView.__init__(self)
  
        HdrItem0 = QStandardItem()
        HdrItem1 = QStandardItem()
        HdrItem2 = QStandardItem()
  
        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        HdrItem0.setFont(font)
        HdrItem1.setFont(font)
        HdrItem2.setFont(font)
  
        brush = QBrush()
        brush.setColor(Qt.blue)
        brush.setStyle(Qt.SolidPattern)
        HdrItem0.setBackground(brush)
  
        HdrItem0.setForeground(brush)
        HdrItem1.setForeground(brush)
        HdrItem2.setForeground(brush)
  
        self.model = QStandardItemModel(0, 3)
        self.model.setHorizontalHeaderItem(0, HdrItem0)
        self.model.setHorizontalHeaderItem(1, HdrItem1)
        self.model.setHorizontalHeaderItem(2, HdrItem2)
        self.model.setHorizontalHeaderLabels(['Column1', 'Column2', 'Column3'])
  
        self.setModel(self.model)
        self.clicked.connect(self.itemSingleClicked)
 
    def itemSingleClicked(self, index):
        Item = self.selectedIndexes()[0]
        ItemVal = Item.model().itemFromIndex(index).text()
        print("Item Clicked:",ItemVal)
 
    def SetContent(self):
        self.model.setRowCount(0)
 
        ItmRecSet = [
            {'CatgryName':'Cat-1', 'GroupName':'Run-Grp-1', 'ItemName':'Run-Itm-1'},
            {'CatgryName':'Cat-1', 'GroupName':'Run-Grp-1', 'ItemName':'Run-Itm-2'},
            {'CatgryName':'Cat-1', 'GroupName':'Run-Grp-1', 'ItemName':'Run-Itm-3'}
            ]
 
        for Item in ItmRecSet:
            ItmNam = QStandardItem(Item['ItemName'])
            CatNam = QStandardItem(Item['CatgryName'])
            GrpNam = QStandardItem(Item['GroupName'])
 
            self.model.appendRow([CatNam, GrpNam, ItmNam])
 
class CenterPane(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self)
 
        self.MainWin = parent
 
        self.ItemDsply = ItemDsplyr()
        self.ItemDsply.SetContent()
 
        CntrPane = QSplitter(Qt.Horizontal, self)
        CntrPane.addWidget(QTextEdit())
        CntrPane.addWidget(self.ItemDsply)
        CntrPane.setSizes([75,200])
 
        hbox = QHBoxLayout(self)
        hbox.addWidget(CntrPane)
 
        self.setLayout(hbox)
 
    @property
    def MainWin(self):
        return self.__parent
 
    @MainWin.setter
    def MainWin(self, value):
        self.__parent = value
 
class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.setCentralWidget(CenterPane(self))
 
if __name__ == "__main__":
    qApp = QApplication([])
    GUI = Window()
    GUI.show()
    sys.exit(qApp.exec_())
