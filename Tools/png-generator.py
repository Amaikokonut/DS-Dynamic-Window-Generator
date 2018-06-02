# Generates a bunch of files to use for DWG tiles
from PIL import Image

min = 1
max = 512
incr = 2

filecount = 0
width = min
height = min

while width <= max:
    while height <= max:
        img = Image.new('RGB', (height, width), (15, 113, 137))
        img.save("image-" + str(filecount) + ".png", "PNG")
        print("saving file ", height, "x", width)
        filecount += 1
        height *= incr
#       print("height: ", height)
    height = min
    width *= incr
#    print("width: ", width)
