import os
import shutil

# Define the folder name
folder_name = "DSA_Files"

# Check the folder exists
if os.path.exists(folder_name):
    # Remove the folder and all its contents
    shutil.rmtree(folder_name)
    print(f"All files in '{folder_name}' have been deleted.")
else:
    print(f"The folder '{folder_name}' does not exist.")
condition = True  # Replace with your actual condition

if condition:
    print("Hello World")
else:
    print("Goodbye World")
while True:
