# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import os, pyglet

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from tkinter.font import Font


ASSETS_PATH = os.path.dirname(__file__) + "/assets"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Main_Frame():
    def __init__(self, parent, window):
        self.parent = parent
        self.window = window

    def create_elements(self):
        self.elements = {}
        self.create_canvas()
        self.create_header()
        self.create_body()
        self.create_footer()

    def create_canvas(self):
        self.elements["canvas"] = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 671,
            width = 698,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.elements["canvas"].place(x = 0, y = 0)

    def create_zoro_image(self):
        self.image_zoro = PhotoImage(file=relative_to_assets("frame0/zoro.png"))
        
        self.elements["zoro_logo"] = self.elements["canvas"].create_image(634.0, 611.0, image=self.image_zoro)

    def create_header_background(self):
        self.header_background_image = PhotoImage(file=relative_to_assets("commons/header_background.png"))

        self.elements["header_background"] = self.elements["canvas"].create_image(349.0, 144.0, image=self.header_background_image)
    
    def create_title(self):
        self.elements["canvas"].create_text(
            167.0,
            31.0,
            anchor="nw",
            text="Summoners War \nTools",
            fill="#2F0F73",
            font=("Irish Grover", 64 * -1),
            justify="center"
        )

    def create_trademark(self):
        self.elements["canvas"].create_text(
            12.0,
            638.0,
            anchor="nw",
            text="Developed by Quentin Norbert",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

    def create_quit_button(self):
        self.quit_button_image = PhotoImage( 
            file=relative_to_assets("frame0/quit_button.png"))
        self.elements["quit_button"] = Button(
            image=self.quit_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.window.destroy(),
            relief="flat"
        )
        self.elements["quit_button"].place(
            x=281.0,
            y=402.0,
            width=136.0,
            height=44.0
        )

    def create_buildings_button(self):
        self.buildings_button_image = PhotoImage(
            file=relative_to_assets("frame0/buildings_button.png"))
        self.elements["buildings_button"] = Button(
            image=self.buildings_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.switch_frame("Buildings_Frame"),
            relief="flat"
        )
        self.elements["buildings_button"].place(
            x=281.0,
            y=335.0,
            width=136.0,
            height=44.0
        )

    def create_header(self):
        self.create_header_background()
        self.create_title()

    def create_body(self):
        self.create_buildings_button()
        self.create_quit_button()

    def create_footer(self):
        self.create_trademark()
        self.create_zoro_image()

    def destroy(self):
        [element.place_forget() for element in self.elements]
