import os

# Specify the folder path
folder_path = r'folder path'  # Replace with the path of your folder

# Get a list of all files in the folder
files = os.listdir(folder_path)

# Initialize a counter for the number of files
file_count = 0

# Create a text file and write the file names into it (without extensions)
with open('file_names.txt', 'w', encoding='utf-8') as f:
    for file in files:
        # Check if it is a file (not a subfolder)
        if os.path.isfile(os.path.join(folder_path, file)):
            # Remove the file extension using os.path.splitext
            file_name_without_extension = os.path.splitext(file)[0]
            f.write(file_name_without_extension + '\n')
            file_count += 1  # Increment the file count

    # Write the total number of files at the end
    f.write(f"\nTotal number of files: {file_count}\n")

print(f"File names without extensions have been written to file_names.txt. Total files: {file_count}")
