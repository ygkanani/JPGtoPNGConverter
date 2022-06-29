import sys
import os
from PIL import Image

# grab first and second arguments
sourceDir = sys.argv[1]
targetDir = sys.argv[2]

# check if targetDir exists
# If not, create new Directory
if not os.path.exists(targetDir):
    os.mkdir(targetDir)

# loop through pokedex
for file in os.listdir(sourceDir):
    # convert file from JPG to PNG
    img = Image.open(f'{sourceDir}{file}')
    # save to the new folder
    img.save(f'{targetDir}{os.path.splitext(file)[0]}.png', 'png')

print('all done!')

