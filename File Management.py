import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory
import json



root = tk.Tk()


extensions = {".jpg" : "C:/Sorted/JPG", ".exe" : "C:/Sorted/EXE", ".png" : "C:/Sorted/PNG", ".jpeg" : "C:/Sorted/JPEG", ".pdf" : "C:/Sorted/PDF", ".ppsx" : "C:/Sorted/PPSX",
              ".txt" : "C:/Sorted/TXT", ".wvm" : "C:/Sorted/WVM", ".zip" : "C:/Sorted/ZIP", ".gif" : "C:/Sorted/GIF", ".jfif" : "C:/Sorted/JFIF",  ".py" : "C:/Sorted/PY",
              ".psd" : "C:/Sorted/PSD", ".raw" : "C:/Sorted/RAW", ".tiff" : "C:/Sorted/TIFF", ".mp3" : "C:/Sorted/MP3", ".docx" : "C:/Sorted/DOCX", "msi" : "C:/Sorted/MSI"}


def starting_location():
    starting_file = "C:/Users/patri/downloads"
    print(f"Your starting location is {starting_file}")
    return starting_file


def ending_location(key):
    print("What is your ending location")
    ending_file = extensions.get(key)
    return ending_file


def printing_directory(ending):
    try:
        print(f"You are attempting to move the {ending}'s")
        directory = starting_location()
        ending_file = ending_location(ending)
        for filename in os.listdir(directory):
            if filename.endswith(ending):
                print(f"{directory}/{filename}")
                os.rename(f"{directory}/{filename}", f"{ending_file}/{filename}")
                print(f"\tMoved to {ending_file}/{filename}")
            else:
                continue
    except:
           print("There were either no files to be moved, or there was an error moving the files. Contact Creator to fix the problem.... Like everything else.")


def run_programs():
    perms = input("Do you want to move all of the files?")
    if perms.lower() == 'yes':
        for item in extensions:
            printing_directory(item)
    else:
        print("Have a nice day!")


run_programs()