import classes 
from PIL import Image 
import numpy
import var

white = (255, 255, 255)
black = (0, 0, 0)

def generate_vector(x, y):
    # find the location of the drill based on pixels  
    x0 = (var.pxl * x)
    y0 = (var.pxl * y)

    # open image & load
    img = Image.open(var.name)
    img_gray = img.convert("L")
    pixels = img_gray.load()

    # iterate over every row
    for Y in range(var.pxl):
        # iterate over each drill in each row 
        for X in range(var.pxl):
            r, g, b, a = pixels[x0 + X, y0 + Y]
            avg = (r + g + b)/3
            if (avg > 255/2):
                # set color to white 
                img.putpixel((x0 + X, y0 + Y), white)
            else: 
                img.putpixel((x0 + X, y0 + Y), black)

    # save image 
    img.save("BW_space.png")
    # temp return 
    return r