import os
import shutil
import tkinter as tk
from tkinter.filedialog import askdirectory

root = tk.Tk()


extensions = [".jpg", ".exe", ".png", ".jpeg", ".pdf", ".ppsx", ".txt", ".wvm",
              ".zip", ".gif", ".jfif", ".psd", ".raw", ".tiff", ".mp3", ".docx", ".py"]


def starting_location():
    print("What is your starting location")
    starting_file = askdirectory()
    return starting_file


def ending_location():
    print("What is your ending location")
    ending_file = askdirectory()
    return ending_file


def printing_directory(ending):

    print(f"You are attempting to move the {ending}'s")
    directory = starting_location()
    ending_file = ending_location()
    move_all = input(f"You will be moving all of the {ending}'s. Do you want to move all of them?")
    if move_all.lower() == 'yes':
        for filename in os.listdir(directory):
            if filename.endswith(ending):
                print(f"{directory}/{filename}")
                os.rename(f"{directory}/{filename}", f"{ending_file}/{filename}")
                print(f"\tMoved to {ending_file}/{filename}")
            else:
                continue
    else:
        holder = input("Do you want to move any of the files?")
        if holder.lower() == 'yes':
            for filename in os.listdir(directory):
                if filename.endswith(ending):
                    print(f"{directory}/{filename}")
                    response = input(f"Would you like to move this file?")
                    if response.lower() == 'yes':
                        os.rename(f"{directory}/{filename}", f"{ending_file}/{filename}")
                        print(f"\tMoved to {ending_file}/{filename}")
                    else:
                        print("File was not moved")
        else:
            print("No files were moved.")


def run_programs():
    for item in extensions:
        printing_directory(item)


run_programs()
