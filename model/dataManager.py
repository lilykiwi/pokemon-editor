import os

from lxml import etree


class DataManager:
  def __init__(self: "DataManager") -> None:
    supported_categories = [
        "pokedex",
        "moves",
        # 'abilities',
        "items",
        # 'types',
    ]

    # Get the user's appdata folder
    self.appdata_folder = os.getenv("APPDATA")

    app_folder = os.path.join(self.appdata_folder, "PokemonPy")
    # Create a directory for your app (optional)
    if not os.path.exists(app_folder):
      os.makedirs(app_folder, exist_ok=True)

    # Create a file for your app (optional)
    self.xml_file_path = os.path.join(app_folder, "data.xml")

    self.data: etree.ElementBase = self.get_xml(self.xml_file_path)

  def get_category(self, category_name: str) -> list | None:
    # Get the pokedex
    return self.data.find(category_name)

  def add_category(self, category_name):
    # Add a new category to the dictionary
    if category_name not in self.data:
      self.data[category_name] = []

  def get_xml(self, path: str) -> etree.ElementBase | None:
    # Read the stored XML file
    with open(path, "r") as file:
      tree = etree.parse(file)
      file.close()
      return tree

  def save_data(self) -> None:
    # Write the XML file
    with open(self.xml_file_path, "w") as file:
      file.write(etree.tostring(self.data, pretty_print=True).decode("utf-8"))
      file.close()
      print("Data saved!")

  def check_data(self) -> bool:
    if self.data is None:
      print("Data is empty!")
      return False
    else:
      for category in self.data:
        print(category)
        for item in category:
          print(item)
      return True
