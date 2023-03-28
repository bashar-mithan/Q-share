from enums import Location
from models import DetailsScheme

from string import ascii_letters, digits
from dataclasses import asdict
from PIL import Image
import datetime
import os
import qrcode
import random 
import json

class QR:
    """Generates the qrcode."""
    def __init__(self, data: None) -> None:
        self.data = data
        self.title = Title()
        self.path = Path(self.title)
        self.__generateQR()
        self.__writeImage()
        self.__save()

    def __generateQR(self) -> None:
        self.base = qrcode.QRCode(version = 2, box_size = 10, border = 5)
        
        self.base.add_data(self.data)
        self.base.make(fit=True)

    def __writeImage(self) -> None:
        self.image = self.base.make_image(fill_border='black', back_color='white')

    def __save(self) -> None:
        self.image.save(self.path.png)
        # Resizing the image to be 350 by 350 to let it fit in the hold funtion. gui/app.py:Hold  
        Image.open(self.path.png).resize((350, 350)).save(self.path.png)
        Details(self.path.json, content=self.data).save()


class Title:
    """Generates the title for naming the .json and .png"""
    def __init__(self) -> None:
        self.code = self.__build()

    def __repr__(self) -> str:
        return self.__build()

    def __build(self):
        length = 14
        return ''.join(random.choice(ascii_letters + digits) for _ in range(length))
          


class Path:
    
    def __init__(self, title: Title):
        self.title = str(title)
        self.generate()
        self.path = str(os.path.join(Location.history.value, self.title)) \
        if os.path.isdir(os.path.join(Location.history.value, self.title)) else None 
        
        # extensions
        self.json = os.path.join(self.path, f'{self.title}.json') 
        self.png = os.path.join(self.path, f'{self.title}.png') 



    def __str__(self) -> str:
        return self.path

    def generate(self) -> os:
        os.mkdir(os.path.join(Location.history.value, str(self.title)))


class Details:
    """Generated the details that must be stored in the json file."""
    def __init__(self, path: str, content: str) -> None:
        self.path = path
        self.title = os.path.basename(self.path)
        self.content = content
        self.details = self.__fillDetails()


    def __fillDetails(self) -> None:
        return asdict(DetailsScheme(title=self.title, content=self.content, time=str(datetime.datetime.now())))

    def save(self) -> None:
        with open(self.path, 'w') as JsonFile:
            json.dump(self.details, JsonFile)

