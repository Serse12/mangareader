import re
import tkinter as tk
from enum import Enum
from pathlib import Path


class Globals:
    _instance = None  # Singleton instance
    DirectoryEnum = Enum("DirectoryEnum", {})  # Empty enum at class level

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Globals, cls).__new__(cls)
            cls._instance._current_folder = None
            cls._instance._index_of_page = 0
            cls._instance._image_frame = None
            cls._instance._num_files = 0
            cls._instance._scale_factor = 1.0
            cls._instance._current_index_enum = 1
        return cls._instance

    # scale_factor
    @property
    def scale_factor(self):
        return self._scale_factor

    @scale_factor.setter
    def scale_factor(self, value):
        if isinstance(value, float) and value > 0:
            self._scale_factor = value
        else:
            raise ValueError("scale_factor must be a positive float.")

    # current_folder
    @property
    def current_folder(self):
        return self._current_folder

    @current_folder.setter
    def current_folder(self, folder):
        if folder is not None and not isinstance(folder, (str, Path)):
            raise ValueError("current_folder must be a string, Path, or None")

        folder_path = Path(folder) if folder is not None else None
        self._current_folder = str(folder_path)

        if folder_path is None:
            self._num_files = 0
            Globals.DirectoryEnum = Enum("DirectoryEnum", {})
            return

        # count files in the current folder
        self._num_files = len(list(folder_path.glob("*")))

        # rebuild enum from parent subdirectories
        result = folder_path.parent
        subdirs = [str(p) for p in result.iterdir() if p.is_dir()]

        sorted_subdirs = sorted(subdirs, key=Globals.chapter_number)

        Globals.DirectoryEnum = Enum(
            "DirectoryEnum",
            {f"_{i + 1}": p for i, p in enumerate(sorted_subdirs)}
        )

        for d in Globals.DirectoryEnum:
            print(d.name, "->", d.value, type(d.value))

    def chapter_number(path_str):
        match = re.search(r"Capitolo(\d+)", path_str)
        return int(match.group(1)) if match else 0
    # index_of_page
    @property
    def index_of_page(self):
        return self._index_of_page

    @index_of_page.setter
    def index_of_page(self, index):
        if not isinstance(index, int) or index < 0:
            raise ValueError("index_of_page must be a non-negative integer")
        self._index_of_page = index

    # num_files
    @property
    def num_files(self):
        return self._num_files

    @num_files.setter
    def num_files(self, value):
        self._num_files = value

    # image_frame
    @property
    def image_frame(self):
        return self._image_frame

    @image_frame.setter
    def image_frame(self, image_frame_obj):
        self._image_frame = image_frame_obj

    def get_enum_index(self, path: str) -> int | None:
        """Return 1-based index of a path in DirectoryEnum, or None if not found."""
        values = list(self.DirectoryEnum)
        return next((i for i, e in enumerate(values, start=1) if e.value == path), None)

    def get_directory_by_index(self, index: int) -> str | None:
        """Return the Path of DirectoryEnum member by 1-based index."""
        name = f"_{index}"
        return getattr(self.DirectoryEnum, name, None).value if hasattr(self.DirectoryEnum, name) else None


window = tk.Tk()
