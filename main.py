from gui.main_frame import Main_Frame
from gui.buildings_frame import Buildings_Frame
from gui.converter_frame import Converter_Frame
from tkinter import Tk
from pathlib import Path

import os, pyglet

ASSETS_PATH = os.path.dirname(__file__) + "/gui/assets"


def init_fonts():
    if os.name == "nt":
        pyglet.options['win32_gdi_font'] = True
    pyglet.font.add_file(str(ASSETS_PATH / Path("commons/fonts/IrishGrover-Regular.ttf")))


class App():

    def __init__(self, *args, **kwargs):
        self.window = Tk()

        self.window.geometry("698x671")
        self.window.configure(bg = "#FFFFFF")
        self.window.resizable(False, False)
        self._current_frame = None

        self.frames = {
            "Main_Frame": Main_Frame(self, self.window),
            "Buildings_Frame": Buildings_Frame(self, self.window),
            "Converter_Frame": Converter_Frame(self, self.window)
        }

        self.switch_frame("Main_Frame")

    def switch_frame(self, next_frame):
        """Destroys current frame and replaces it with a new one."""
        if self.frames[next_frame] == self._current_frame:
            self._current_frame.destroy()
        
        self._current_frame = self.frames[next_frame]
        self._current_frame.create_elements()



if __name__ == "__main__":
    init_fonts()
    app = App()
    app.window.mainloop()
