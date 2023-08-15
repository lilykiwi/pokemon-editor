import random
from PySide6 import QtCore, QtWidgets

from gui.tabs import MainTabBar

from model.dataManager import DataManager

class MainWidget(QtWidgets.QMainWindow):
  #def printChildGeometryCoords(self, widget: QtWidgets.QWidget):
  #  print(self, self.geometry().getCoords(), self.frameGeometry().getCoords())
  #  for i in range(len(widget.children())):
  #    item: QtWidgets.QWidget | QtWidgets.QLayout | None = widget.children()[i]
  #    try:
  #      print(item, item.geometry().getCoords(), item.frameGeometry().getCoords())
  #      self.printChildGeometryCoords(item)
  #    except:
  #      print(item)
      

  def __init__(self, dataManager: DataManager):
    super().__init__()

    self.tabBar = MainTabBar(dataManager)
    self.setCentralWidget(self.tabBar)
    self.setContentsMargins(0, 0, 0, 0)
    
    self.resize(800, 600)
    #self.printChildGeometryCoords(self)
    
      
