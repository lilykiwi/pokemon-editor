from PySide6 import QtCore
from PySide6.QtWidgets import (QAbstractItemView, QHBoxLayout, QLabel,
                               QListView, QListWidget, QListWidgetItem,
                               QVBoxLayout, QWidget, QLineEdit)

from model.dataManager import DataManager


class PokedexEditor(QWidget):
  def __init__(self: "PokedexEditor", dataManager: "DataManager"):
    # initialise QWidget stuff
    super().__init__()

    # we want a horizontal layout for this segment.
    # on the left is a treeview which shows the pokemon
    # on the right is a form which shows the pokemon's details
    self.layout = QHBoxLayout()

    self.leftBox = PokedexList()
    self.layout.addLayout(self.leftBox)

    # add the form
    self.rightBox = SpeciesEditor()
    self.layout.addLayout(self.rightBox)

    # set the layout
    self.setLayout(self.layout)

    # connect the treeview itemSelectionChanged signal to the function that updates the form
    self.leftBox.listWidget.itemSelectionChanged.connect(self.updateForm)

  @QtCore.Slot()
  def updateForm(self: "PokedexEditor"):
    # get the selected pokemon
    if len(self.leftBox.listWidget.selectedItems()) == 0:
      return
    selected = self.leftBox.listWidget.get_species(
      self.leftBox.listWidget.selectedItems()[0])
    if isinstance(selected, SpeciesListItem) == False:
      print("selected item is not a SpeciesListItem")
      print(selected.__class__)
      return

    # add the info to the form
    self.rightBox.nameBox.setText(selected.name)


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


class PokedexList(QVBoxLayout):
  def __init__(self: "PokedexList"):
    # initialise QVBoxLayout stuff
    super().__init__()
    self.setAlignment(QtCore.Qt.AlignTop)

    # add the treeview
    self.listWidget = SpeciesList()
    self.addWidget(self.listWidget)
    self.listWidget.viewMode = QListView.IconMode
    self.listWidget.setMaximumWidth(200)
    self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)


class SpeciesEditor(QVBoxLayout):
  def __init__(self: "SpeciesEditor"):
    # initialise QVBoxLayout stuff
    super().__init__()
    self.setAlignment(QtCore.Qt.AlignTop)

    nameLabel = QLabel("Name: ")
    self.nameBox = QLineEdit()
    self.addLayout(Helpers.WrapInHBoxLayout(nameLabel, self.nameBox))


class Helpers():
  def WrapInVBoxLayout(*widgets) -> QVBoxLayout:
    layout = QVBoxLayout()
    for widget in widgets:
      layout.addWidget(widget)
    return layout

  def WrapInHBoxLayout(*widgets) -> QHBoxLayout:
    layout = QHBoxLayout()
    for widget in widgets:
      layout.addWidget(widget)
    return layout
