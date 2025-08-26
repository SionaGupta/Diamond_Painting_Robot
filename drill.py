import classes 
from PIL import Image 


def generate_vector(x, y, name, pxl):
    # find the location of the drill based on pixels  
    x0 = (pxl * x)
    y0 = (pxl * y)

    # open image & load
    img = Image.open(name)
    pixels = img.load()

    r, g, b, a = pixels[x0, y0]

    print(x)
    print(y)

    # temp return 
    return r