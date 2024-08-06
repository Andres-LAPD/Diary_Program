"""
    This program is a digital personal diary that allows users
    record and read your daily thoughts, experiences and reflections.
    Offers a simple interface for creating new entries and a 
    reading to review the previous ones.

    By Luis Andrés Piñero Diez.
    06/08/2024
"""

#Imports
import datetime as DT

#Create files
def create_files():
    file_name = input("Enter entry name: ")
    file_name += "_" + DT.datetime.now().strftime("%d.%m.%y_%H.%M.%S") + ".txt"
    with open(file_name, "w") as new_file:
        print("Type END FILE to exit when done.")
        while True:
            text = input()
            if text == "END FILE":
                break
            new_file.write(text + "\n")

#Open to read files
def read_files():
    file_name = input("Enter entry name: ")
    try:
        with open(file_name, "r") as read_file:
            print(read_file.read())
    except FileNotFoundError:
        print("Entry not found.")

#Menu
while True:
    print("1. Create new entry.")
    print("2. Read entry.")
    print("3. Exit.")

    option = input("Select an option: ")

    if option == "1":
        create_files()

    elif option == "2":
        read_files()

    elif option == "3":
        break

    else:
        print("Invalid option.")