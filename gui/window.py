import random

from PySide6.QtWidgets import (QLabel, QTabWidget, QVBoxLayout,
                               QWidget, QMainWindow)

from gui.pages.pokedex import PokedexEditor
from model.dataManager import DataManager


class MainTabBar(QWidget):
  def __init__(self, dataManager: DataManager):
    super().__init__()

    self.layout = QVBoxLayout()
    self.layout.setContentsMargins(0, 0, 0, 0)

    # Create a QTabWidget
    tab_widget = QTabWidget(self)

    # Create tabs
    self.tab1 = PokedexEditor(dataManager)
    self.tab2 = QLabel("Contents of Tab 2")

    # Add tabs to the QTabWidget
    tab_widget.addTab(self.tab1, "PokeDex")
    tab_widget.addTab(self.tab2, "ItemDex")

    self.layout.addWidget(tab_widget)

    self.setLayout(self.layout)


class MainWindow(QMainWindow):
  # def printChildGeometryCoords(self, widget: QWidget):
  #  print(self, self.geometry().getCoords(), self.frameGeometry().getCoords())
  #  for i in range(len(widget.children())):
  #    item: QWidget | QLayout | None = widget.children()[i]
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
    # self.printChildGeometryCoords(self)
