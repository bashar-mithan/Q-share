from tkinter import PhotoImage, Label
import customtkinter
import os

from genetators import Title
from enums import Location

def hold(title: Title, imagePath: str) -> None:
    """The `hold` function is responsable for displaying the qrcode on the buttom right corner of the screen."""
    customtkinter.set_default_color_theme("dark-blue")

    window = customtkinter.CTk()
    height, width = 350, 350
    x, y = 1119, 600

    window.title(f'{os.path.basename(Location.root.value)} - {title}')

    window.geometry(f'{width}x{height}+{x}+{y}')
    window.resizable(0, 0)

    image = PhotoImage(file=imagePath)
    Label(window, image=image).place(x=0, y=0)

    window.bind('<Escape>', lambda exit: window.destroy())

    window.mainloop()


