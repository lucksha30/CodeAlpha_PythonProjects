import os
import shutil

src = "source_folder"
dest = "destination_folder"

os.makedirs(dest, exist_ok=True)
if os.path.isdir(src):
    for file in os.listdir(src):
        source_file_path = os.path.join(src, fil
        if os.path.isfile(source_file_path) and file.endswith('.jpg'):
            destination_file_path = os.path.join(dest, file)
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved: {file}")
    print("All JPG files moved successfully!")
else:
    print(f"Error: Source directory '{src}' not found. Please create it.")
