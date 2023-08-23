import os
import shutil

# Get the path from the user
path = input("Enter Path: ")

# Get a list of all files in the specified path
files = os.listdir(path)

# Loop through each file in the list
for file in files:
    # Split the file name and extension
    filename, extension = os.path.splitext(file) 
    extension = extension[1:]  # Remove the leading dot from the extension

    # Check if a folder with the extension name exists in the path
    if os.path.exists(path+'/'+extension):
        # If the folder exists, move the file to that folder
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
    else:
        # If the folder doesn't exist, create it
        os.makedirs(path+'/'+extension)
        # Move the file to the newly created folder
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

# Organizing process completed
print("Files organized successfully!")
