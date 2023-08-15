import os
import xml.etree.ElementTree as ET

class DataManager:
  
  def __init__(self):
    # Get the user's appdata folder
    self.appdata_folder = os.getenv('APPDATA')
    
    app_folder = os.path.join(self.appdata_folder, 'PokemonPy')
    # Create a directory for your app (optional)
    if not os.path.exists(app_folder):
      os.makedirs(app_folder, exist_ok=True)

    # Create a file for your app (optional)
    self.xml_file_path = os.path.join(app_folder, 'data.xml')
    
    print(self.xml_file_path)
    
    # Create a dictionary to store main data
    self.data = {
      "pokedex": [],
      "moves": [],
    }
    
  
  def add_category(self, category_name):
    # Add a new category to the dictionary
    if category_name not in self.data:
      self.data[category_name] = []
      
  
  def add_item(self, category_name, item_id, item_name):
    if category_name in self.data:
      category = self.data[category_name]
      item = ET.Element("item", id=str(item_id))
      item.text = item_name
      category.append(item)
      
  
  def get_xml(self):
    root = ET.Element("data")
    for category_name, items in self.data.items():
      category_element = ET.SubElement(root, category_name)
      category_element.extend(items)
    return ET.tostring(root, encoding="utf-8").decode("utf-8")


  def check_for_existing_data(self):
    # we want to check for existing data in the appdata folder
    # Read the stored XML file
    tree = ET.parse(self.xml_file_path)
    root = tree.getroot()
    
    if root is None:
      print("No data found!")
      return
    
    else: 
      print("Data found!")
      self.process_xml_data(root)
      return


  def process_xml_data(self, root: ET.Element):
    for category in root:
      
      if (category.tag == "pokedex"):
        for pokemon in category:
          #print(pokemon)
          #print(pokemon.tag, pokemon.attrib, pokemon.text)
          self.data["pokedex"].append(pokemon)
          
      if (category.tag == "moves"):
        for move in category:
          self.data["moves"].append(move)

