import os
import shutil
import tkinter
from tkinter.filedialog import askdirectory


tkinter.Tk().withdraw()


extensions = [".exe", ".jpg", ".png", ".jpeg", ".pdf", ".ppsx", ".txt", ".wvm",
              ".zip", ".gif"]



def starting_location():
    starting_file = askdirectory()
    return starting_file





def ending_location():
    ending_file = askdirectory()
    return ending_file


def printing_directory():
    files = []
    directory = starting_location()
    for filename in os.listdir(directory):
        if filename.endswith(extensions[".exe"]):
            files.append(filename)
        else:
            continue
    print(f"The items inside of your {directory} are: \n\t{files}")





printing_directory()
