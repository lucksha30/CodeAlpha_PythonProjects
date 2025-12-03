import os
import shutil

src = "source_folder"
dest = "destination_folder"

os.makedirs(dest, exist_ok=True)

for file in os.listdir(src):
    if file.endswith(".jpg"):
        shutil.move(os.path.join(src, file),
                    os.path.join(dest, file))

print("All JPG files moved successfully!")
