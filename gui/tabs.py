from PySide6.QtWidgets import QWidget, QTabWidget, QTextEdit, QLabel, QVBoxLayout

from gui.pages.pokedex import PokedexEditor

from model.dataManager import DataManager

class MainTabBar(QWidget):
  def __init__(self, dataManager: DataManager):
    super().__init__()

    self.layout = QVBoxLayout()
    self.layout.setContentsMargins(0,0,0,0)

    # Create a QTabWidget
    tab_widget = QTabWidget(self)
    tab_widget.setContentsMargins(0,0,0,0)

    # Create tabs
    self.tab1 = PokedexEditor(dataManager)
    self.tab2 = QLabel("Contents of Tab 2")

    # Add tabs to the QTabWidget
    tab_widget.addTab(self.tab1, "PokeDex")
    tab_widget.addTab(self.tab2, "ItemDex")

    self.layout.addWidget(tab_widget)

    self.setLayout(self.layout)
    
