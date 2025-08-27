import classes 
from PIL import Image 
import numpy
import var

white = (255,)
black = (0,)

def generate_vector(x, y):
    # find the location of the drill based on pixels  
    x0 = (var.pxl * x)
    y0 = (var.pxl * y)

    # temp return 
    return y0