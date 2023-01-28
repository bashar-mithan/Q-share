from genetators import QR
from gui.app import hold

import os

image = QR('D')
path = image.path.png
hold(title=os.path.basename(path), imagePath=path)