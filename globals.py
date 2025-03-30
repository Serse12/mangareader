import tkinter as tk
from pathlib import Path
from pathlib import Path

class Globals:
    _instance = None  # Stores the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Globals, cls).__new__(cls)
            cls._instance._current_folder = None
            cls._instance._index_of_page = 0
            cls._instance._canvas = None
            cls._instance.num_files = 0
            cls._instance._scale_factor = 1
        return cls._instance

    @property
    def scale_factor(self):
        return self._scale_factor

    @scale_factor.setter
    def scale_factor(self, value):
        if isinstance(value, float) and value > 0:
            self._scale_factor = value
        else:
            raise ValueError("Width must be a positive integer.")

    # Getter and Setter for current_folder
    @property
    def current_folder(self):
        return self._current_folder

    @current_folder.setter
    def current_folder(self, folder):
        if not isinstance(folder, str) and folder is not None:
            raise ValueError("current_folder must be a string or None")
        self._current_folder = folder
        dir_path = Path(self._current_folder)
        self._num_files = len(list(dir_path.glob("*")))
        print(self._num_files)

    # Getter and Setter for index_of_page
    @property
    def index_of_page(self):
        return self._index_of_page

    @property
    def num_files(self):
        return self._num_files

    @index_of_page.setter
    def index_of_page(self, index):
        if not isinstance(index, int) or index < 0:
            raise ValueError("index_of_page must be a non-negative integer")
        self._index_of_page = index

    # Getter and Setter for canvas
    @property
    def canvas(self):
        return self._canvas

    @canvas.setter
    def canvas(self, canvas_obj):
        self._canvas = canvas_obj  # No restriction; can be a tkinter Canvas or another object

    @num_files.setter
    def num_files(self, value):
        self._num_files = value


window = tk.Tk()
