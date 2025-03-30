import os

import fitz
from PIL import Image, ImageTk
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
    if globals.canvas:
        globals.canvas.destroy()
    if globals.current_folder:
        file_name = None
        if globals.index_of_page == 0:
            file_name = "/" + os.path.basename(globals.current_folder)
        else:
            file_name = "/" + os.path.basename(globals.current_folder) + "_" + str(globals.index_of_page + 1)
        print("filename = " + file_name)
        complete_name = globals.current_folder + file_name
        print("complete name = " + complete_name)
        try:
            if is_pdf(complete_name):
                image = open_pdf(complete_name,globals.scale_factor)
            else:
                image = open_image(complete_name,globals.scale_factor)  # Handles JPG, PNG, WebP, etc.
            photo = ImageTk.PhotoImage(image)


            globals.canvas = tk.Canvas(window, width=image.width, height=image.height)
            globals.canvas.grid(row=1, column=0, columnspan=4, sticky="ew")

            window.update_idletasks()

            # Calculate the coordinates to center the image
            center_x = (image.width // 2)
            center_y = (image.height // 2)

            # Create the image at the center of the canvas
            globals.canvas.create_image(center_x, center_y, image=photo, anchor=tk.CENTER)


            # Keep reference to avoid garbage collection
            globals.canvas.image = photo
        except Exception as e:
            print("The error is: ", e)
            pass
