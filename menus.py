from tkinter import Menu

from actions.button_functions import get_directory_path, add_bookmark
from globals import *

def configure_upper_menu():
    menu = Menu(window)
    window.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Open folder', command=get_directory_path)
    filemenu.add_command(label='Add bookmark', command=add_bookmark)
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=window.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')
