from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QListWidget, QListView, QListWidgetItem, QAbstractItemView
from model.dataManager import DataManager

class PokedexEditor(QWidget):
  def __init__(self: "PokedexEditor", dataManager: "DataManager"):
    # initialise QWidget stuff
    super().__init__()
    
    # we want a horizontal layout for this segment.
    # on the left is a treeview which shows the pokemon
    # on the right is a form which shows the pokemon's details
    self.layout = QHBoxLayout()
    self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
    
    # add the treeview
    self.listWidget = SpeciesList()
    self.layout.addWidget(self.listWidget)
    self.listWidget.viewMode = QListView.IconMode
    self.listWidget.setMaximumWidth(200)
    self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
    
    # add the form
    self.form = SpeciesEditor()
    self.layout.addWidget(self.form)

    # set the layout
    self.setLayout(self.layout)
    
    # connect the treeview itemSelectionChanged signal to the function that updates the form
    self.listWidget.itemSelectionChanged.connect(self.updateForm)
    
    
  @QtCore.Slot()
  def updateForm(self: "PokedexEditor"):
    # get the selected pokemon
    selected = self.listWidget.get_species(self.listWidget.selectedItems()[0])
    if isinstance(selected, SpeciesListItem) == False:
      print("selected item is not a SpeciesListItem")
      print(selected.__class__)
      return
    
    # add the info to the form
    self.form.idLabel.setText("#" + str(selected.id))
    self.form.nameLabel.setText(selected.name)


class SpeciesList(QListWidget):
  def __init__(self: "SpeciesList"):
    super().__init__()
    self.heldData: dict(str, SpeciesListItem) = {}
  
  def add_species(self, species: "SpeciesListItem") -> None:
    item = QListWidgetItem(species.name)
    self.addItem(item)
    self.heldData[item.text()] = species
    
  def get_species(self, item: QListWidgetItem) -> "SpeciesListItem":
    return self.heldData[item.text()]


# TODO: integrate model.species.Species rather than using this
class SpeciesListItem():
  def __init__(self: "SpeciesListItem", id: int, name: str):
    self.id = id
    self.name = name

class SpeciesEditor(QWidget):
  def __init__(self: "SpeciesEditor"):
    # initialise QWidget stuff
    super().__init__()
    
    # set layout
    self.layout = QVBoxLayout()
    self.layout.setAlignment(QtCore.Qt.AlignTop)
    
    # add a placeholder header
    self.idLabel = QLabel("#[id]")
    self.layout.addWidget(self.idLabel)
    self.nameLabel = QLabel("[name]")
    self.layout.addWidget(self.nameLabel)
    
    self.setLayout(self.layout)
