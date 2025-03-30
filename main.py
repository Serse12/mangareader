from file_visualizer.PDFViewer import configure_pdf_frame
from globals import *
from actions.button_functions import *
from menus import configure_upper_menu
from actions.keyboard import run_keyboard


def configure_main_window():
    window.geometry("600x600")
    window.title("Hello TkInter!")
    window.resizable(True, True)
    window.configure(background="white")
    button1 = tk.Button(window, text='<', command=prev_page)
    button1.grid(row=0, column=0)
    button2 = tk.Button(window, text='>', command=next_page)
    button2.grid(row=0, column=1)
    button3 = tk.Button(window, text='Zoom +', command=zoom_in)
    button3.grid(row=0, column=2)
    button4 = tk.Button(window, text='Zoom -', command=zoom_out)
    button4.grid(row=0, column=3)
    configure_upper_menu()
    configure_pdf_frame()
    run_keyboard()
    for i in range(4):
        window.grid_columnconfigure(i, weight=1, uniform="equal")  # Make columns resizable and equal


def main():
    configure_main_window()
    window.mainloop()


if __name__ == "__main__":
    main()
