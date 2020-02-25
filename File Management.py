import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory


root = tk.Tk()

school_extensions = {".jpg": "C:/Users/016407037/Sorted/JPG", ".exe": "C:/Users/016407037/Sorted/EXE",
                     ".png": "C:/Users/016407037/Sorted/PNG", ".jpeg": "C:/Users/016407037/Sorted/JPEG",
                     ".pdf": "C:/Users/016407037/Sorted/PDF", ".ppsx": "C:/Users/016407037/Sorted/PPSX",
                     ".txt": "C:/Users/016407037/Sorted/TXT", ".wvm": "C:/Users/016407037/Sorted/WVM",
                     ".zip": "C:/Users/016407037/Sorted/ZIP", ".gif": "C:/Users/016407037/Sorted/GIF",
                     ".jfif": "C:/Users/016407037/Sorted/JFIF",  ".py": "C:/Users/016407037/Sorted/PY",
                     ".psd": "C:/Users/016407037/Sorted/PSD", ".raw": "C:/Users/016407037/Sorted/RAW",
                     ".tiff": "C:/Users/016407037/Sorted/TIFF", ".mp3": "C:/Users/016407037/Sorted/MP3",
                     ".docx": "C:/Users/016407037/Sorted/DOCX", "msi": "C:/Users/016407037/Sorted/MSI"}

home_extensions = {".jpg": "C:/Sorted/JPG", ".exe": "C:/Sorted/EXE",
                   ".png": "C:/Sorted/PNG", ".jpeg": "C:/Sorted/JPEG",
                   ".pdf": "C:/Sorted/PDF", ".ppsx": "C:/Sorted/PPSX",
                   ".txt": "C:/Sorted/TXT", ".wvm": "C:/Sorted/WVM",
                   ".zip": "C:/Sorted/ZIP", ".gif": "C:/Sorted/GIF",
                   ".jfif": "C:/Sorted/JFIF",  ".py": "C:/Sorted/PY",
                   ".psd": "C:/Sorted/PSD", ".raw": "C:/Sorted/RAW",
                   ".tiff": "C:/Sorted/TIFF", ".mp3": "C:/Sorted/MP3",
                   ".docx": "C:/Sorted/DOCX", "msi": "C:/Sorted/MSI"}


def starting_location(place):
    if place == "home":
        starting_file = "C:/Users/patri/downloads"
    else:
        starting_file = "C:/Users/016407037/downloads"
    print(f"Your starting location is {starting_file}")
    return starting_file


def ending_location(key, place):
    print("What is your ending location")
    if place == "home":
        ending_file = home_extensions.get(key)
    else:
        ending_file = school_extensions.get(key)
    return ending_file


def printing_directory(ending, place):
    try:
        print(f"You are attempting to move the {ending}'s")
        directory = starting_location(place)
        ending_file = ending_location(ending, place)

        for filename in os.listdir(directory):
            if filename.endswith(ending):
                print(f"{directory}/{filename}")
                os.rename(f"{directory}/{filename}", f"{ending_file}/{filename}")
                print(f"\tMoved to {ending_file}/{filename}")
            else:
                continue
    except:
        print("There were either no files to be moved, or there was an error moving the files. "
              "Contact Creator to fix the problem.... Like everything else.")


def run_programs():
    place = input("Are you at home or at school?")
    if place.lower() == "home":
        print("You have selected home!")
        perms = input("Do you want to move all of the files?")
        if perms.lower() == 'yes':
            for item in home_extensions:
                printing_directory(item, place)
        else:
            print("Have a nice day!")
    elif place.lower() == "school":
        print("You have selected school!")
        perms = input("Do you want to move all of the files?")
        if perms.lower() == 'yes':
            for item in school_extensions:
                printing_directory(item, place)
        else:
            print("Have a nice day!")
    else:
        print("You did not select a correct option, goodbye!")


run_programs()
