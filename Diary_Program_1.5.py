"""
    This program is a digital personal diary that allows users
    record and read your daily thoughts, experiences and reflections.
    Offers a simple interface for creating new entries and a 
    reading to review the previous ones.

    By Luis Andrés Piñero Diez.
    06/08/2024
"""

#Imports
import os
import datetime as DT

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Create files
def create_files():
    diary_directory = os.path.join(current_directory, 'Diary')
    if not os.path.exists(diary_directory):
        os.makedirs(diary_directory)

    file_name = input("Enter entry name: ")
    file_name += "_" + DT.datetime.now().strftime("%d.%m.%y_%H.%M.%S") + ".txt"
    file_path = os.path.join(diary_directory, file_name)

    with open(file_path, "w") as new_file:
        print("Type END FILE to exit when done.")
        while True:
            text = input()
            if text == "END FILE":
                break
            new_file.write(text + "\n")

# Open to read files
def read_files():
    file_name = input("Enter entry name: ")
    diary_directory = os.path.join(current_directory, 'Diary')
    file_path = os.path.join(diary_directory, file_name)
    
    try:
        with open(file_path, "r") as read_file:
            print(read_file.read())
    except FileNotFoundError:
        print("Entry not found.")

# Menu
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
