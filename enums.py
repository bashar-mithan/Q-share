from enum import Enum
from pathlib import Path
import os



class Location(Enum):
   """Contains the necessary path constants."""
   root = Path(__file__).parent
   main = os.path.join(root, 'main.py') if os.path.isfile(os.path.join(root, 'main.py')) else None
   history =  os.path.join(root, 'history/') if os.path.isdir(os.path.join(root, 'history')) else None
   home = os.getenv('HOME')

