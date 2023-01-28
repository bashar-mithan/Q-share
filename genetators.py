from enums import Location
from models import DetailsScheme

from string import ascii_letters, digits
from dataclasses import asdict
import datetime
import os
import qrcode
import random 
import json

class QR:
    def __init__(self, data: None) -> None:
        self.data = data
        self.title = Title()
        self.path = Path(self.title)
        self.__generate()
        self.__image()
        self.__save()

    def __generate(self) -> None:
        self.base = qrcode.QRCode(version = 2, box_size = 10, border = 5)
        
        self.base.add_data(self.data)
        self.base.make(fit=True)

    def __image(self) -> None:
        self.image = self.base.make_image(fill_border='black', back_color='white')
        self.image.resize((350, 350))

    def __save(self) -> None:
        self.image.save(self.path.png)
        Details(self.path.json, content=self.data).save()


class Title:
    def __init__(self) -> None:
        self.code = self.__build()

    def __repr__(self) -> str:
        return self.__build()

    def __build(self):
        length = 14
        title = ''.join(random.choice(ascii_letters + digits) for _ in range(length))
        return title 


class Path:
    def __init__(self, title: Title):
        self.title = str(title)
        self.generate()
        self.path = str(os.path.join(Location.history.value, self.title)) if os.path.isdir(os.path.join(Location.history.value, self.title)) else None 
        
        # extensions
        self.json = os.path.join(self.path, f'{self.title}.json') 
        self.png = os.path.join(self.path, f'{self.title}.png') 



    def __str__(self) -> str:
        return self.path

    def generate(self) -> os:
        os.mkdir(os.path.join(Location.history.value, str(self.title)))


class Details:
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

