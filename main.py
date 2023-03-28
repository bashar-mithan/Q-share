from genetators import QR
from gui.app import hold

import os, sys

# if the length of sys.argv is 1 means that there is not argument specified when calling the main.py file. 
if len(sys.argv) == 1:
    print("help message")
elif len(sys.argv) > 1:
    message = sys.argv[1]
    # Generating the qr code
    image = QR(message)
    # Getting access to the paths of the generated image above.
    path = image.path.png
    # Displaying the image in the right bottom corner of the screen. 
    hold(title=os.path.basename(path), imagePath=path)