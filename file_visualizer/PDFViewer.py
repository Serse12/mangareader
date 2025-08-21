import os
import sys
from tkinter import Scrollbar, BOTTOM, X, RIGHT, Y

import fitz
from PIL import Image, ImageTk
import pillow_avif

from actions.mouse import on_mouse_wheel
from globals import *


def is_pdf(file_path):
    """Check if the file is a PDF based on extension."""
    return file_path.lower().endswith(".pdf")


def open_pdf(file_path, scale_factor=1):
    """Open a PDF and return the first page as an Image object, scaled by the scale_factor."""
    pdf_document = fitz.open(file_path)
    page = pdf_document.load_page(0)  # Load first page
    pix = page.get_pixmap()

    # Convert to a PIL Image
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Resize image based on scale_factor
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    return image


def open_image(file_path, scale_factor=1):
    """Open an image file directly and scale it by scale_factor."""
    image = Image.open(file_path)

    # Resize image based on scale_factor
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    return image


def configure_pdf_frame():
    globals = Globals()
    print(globals.current_folder)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)

    if globals.image_frame:
        globals.image_frame.destroy()
    if globals.current_folder:
        # Create a new frame for the image
        globals.image_frame = tk.Frame(window)
        globals.image_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")

        # Create Canvas and Scrollbars
        canvas = tk.Canvas(globals.image_frame, bg="white")
        h_scroll = Scrollbar(globals.image_frame, orient='horizontal', command=canvas.xview)
        v_scroll = Scrollbar(globals.image_frame, orient='vertical', command=canvas.yview)
        canvas.configure(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

        # Pack Scrollbars and Canvas
        h_scroll.pack(side=BOTTOM, fill=X)
        v_scroll.pack(side=RIGHT, fill=Y)
        canvas.pack(fill="both", expand=True)

        if sys.platform == "win32":
            canvas.bind("<MouseWheel>", lambda event: on_mouse_wheel(event, canvas))
        else:
            canvas.bind("<Button-4>", lambda event: on_mouse_wheel(event, canvas))
            canvas.bind("<Button-5>", lambda event: on_mouse_wheel(event, canvas))

        # Determine the file name based on the current page index
        file_name = f"/{os.path.basename(globals.current_folder)}"
        if globals.index_of_page != 0:
            file_name += f"_{globals.index_of_page + 1}"
        complete_name = globals.current_folder + file_name
        print("Complete file name:", complete_name)

        try:
            # Open the image using the appropriate function
            if is_pdf(complete_name):
                image = open_pdf(complete_name, globals.scale_factor)
            else:
                image = open_image(complete_name, globals.scale_factor)  # Handles JPG, PNG, WebP, etc.

            photo = ImageTk.PhotoImage(image)

            # Create the image on the canvas at the initial center position
            image_id = canvas.create_image(0, 0, image=photo, anchor='center')

            # Update the scroll region to the size of the image
            canvas.config(scrollregion=canvas.bbox(image_id))

            # Keep a reference to the image to prevent garbage collection
            canvas.image = photo
        except Exception as e:
            print("The error is: ", e)
            pass
