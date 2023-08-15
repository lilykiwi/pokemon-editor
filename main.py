import sys

from PySide6 import QtWidgets

from gui.pages.pokedex import SpeciesListItem
from gui.window import MainWindow
from model.dataManager import DataManager

if __name__ == "__main__":
  app = QtWidgets.QApplication([])
  data_manager = DataManager()

  app.setStyle("Fusion")
  with open("gui/style.qss", "r") as f:
    _style = f.read()
    app.setStyleSheet(_style)

  window = MainWindow(data_manager)
  window.resize(800, 600)
  window.show()

  for pokemon in data_manager.get_category("pokedex"):
    species = SpeciesListItem(pokemon.attrib["id"], pokemon.text)
    window.tabBar.tab1.leftBox.listWidget.add_species(species)

  sys.exit(app.exec())
