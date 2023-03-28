from enum import Enum
from pathlib import Path
import os



class Location(Enum):
   """Contains the necessary path constants."""
   root = Path(__file__).parent
   main = os.path.join(root, 'main.py')
   history =  os.path.join(root, 'history/')
   home = os.getenv('HOME')

