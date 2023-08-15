import sys
from PySide6 import QtWidgets

from gui.window import MainWidget
from gui.pages.pokedex import SpeciesListItem

from model.dataManager import DataManager


if __name__ == "__main__":
  app = QtWidgets.QApplication([])
  data_manager = DataManager()
  
  app.setStyle("Fusion")
  with open("gui/style.qss", "r") as f:
    _style = f.read()
    app.setStyleSheet(_style)
  
  widget = MainWidget(data_manager)
  widget.resize(800, 600)
  widget.show()
      
  for pokemon in data_manager.get_category("pokedex"):
    species = SpeciesListItem(pokemon.attrib["id"], pokemon.text)
    widget.tabBar.tab1.listWidget.add_species(species)

  sys.exit(app.exec())
