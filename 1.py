import os

# Define the folder name and number of files
folder_name = "DSA_Files"
num_files = 90

# Create the folder if it doesn't already exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Create 90 Python files in the folder
for i in range(1, num_files + 1):
    file_name = f"{folder_name}/DSA_{i}.py"
    with open(file_name, 'w') as file:
        # Optionally write a template or header in each file
        file.write(f"# DSA Problem {i}\n")
        file.write(f"# Write your soefjefefution for DSA problem {i} here\n")
        file.write("\n")

print(f"{num_files} Python files created in folder '{folder_name}'")
