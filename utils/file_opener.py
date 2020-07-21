import tkinter as tk
from tkinter import filedialog
import os
from shutil import copyfile


def image_open():
    """this function is used for open an image from any 
    location and paste it in capture folder
    """
    dst = "ImageSource/capture.png"
    root = tk.Tk()
    file_path = filedialog.askopenfilename()
    copyfile(file_path, dst)
    root.mainloop()
    return "done"


# image_open()

