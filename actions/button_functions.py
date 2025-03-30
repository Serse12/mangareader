from tkinter import filedialog

from file_visualizer.PDFViewer import configure_pdf_frame
from globals import *


def first_print():
    text = "Hello World!"
    text_output = tk.Label(window, text=text, fg="red", font=("Helvetica", 16))
    text_output.grid(row=0, column=1, padx=50, sticky="W")


def second_function():
    text = "Nuovo Messaggio! Nuova Funzione!"
    text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
    text_output.grid(row=1, column=1, padx=50, sticky="W")


def next_page():
    globals = Globals()
    globals.index_of_page = (globals.index_of_page + 1) % globals.num_files
    configure_pdf_frame()


def prev_page():
    globals = Globals()
    globals.index_of_page = (globals.index_of_page - 1) % globals.num_files
    configure_pdf_frame()


def zoom_in():
    globals = Globals()
    globals.scale_factor = globals.scale_factor + 0.1
    configure_pdf_frame()


def zoom_out():
    globals = Globals()
    globals.scale_factor = globals.scale_factor - 0.1
    configure_pdf_frame()


def get_directory_path():
    globals = Globals()
    globals.current_folder = filedialog.askdirectory()
    print(globals.current_folder)
    configure_pdf_frame()


def add_bookmark():
    globals = Globals()
    file_path = './bookmarks.txt'
    with open(file_path, 'a') as file:
        file.write(globals.current_folder + '\n')
    print(globals.current_folder)
    configure_pdf_frame()
