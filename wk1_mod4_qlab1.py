#!/usr/bin/env python3
# Import os and sys modules for taking arguments and reading the filesystem.
import os, sys
# Import Image from the pillow module PIL to read and process images.
from PIL import Image

# Take arguments from the command line and apply them as the variables for later
# parameters for opening and saving files.
image_folder = sys.argv[1]
dest_folder = sys.argv[2]

# Variable containing a tuple for the x/y dimension of the image in pixels
size = (128,128)

# For loop to iterate files in a directory and process each file until done.
for file in os.listdir(image_folder):
  # Joining paths to filename for opening and saving file.
  filepath = os.path.join(image_folder, file)
  destpath = os.path.join(dest_folder, file)
  # Try/except block to catch OSErrors and continue the loop.
  # The try will attempt to open file and process the file as a new file and path.
  try:
    with Image.open(filepath) as im:
      # For whatever reason the save() method operates without having to be applied to the 
      # variable while the other Image related methods need to be applied to the variable.
      im = im.convert("RGB").rotate(270).resize(size)
      im.save(destpath, "JPEG", optimize=True, quality=90)
  # The except block will print an error for file and continue the loop without a traceback.
  except OSError:
    print("conversion failed:", file)

# Signal to user that the script has completed.
print("Batch operation completed")

