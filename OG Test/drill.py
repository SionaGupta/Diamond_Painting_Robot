import classes 
from skimage.metrics import structural_similarity as ssim
from PIL import Image 
import numpy as np
import var

white = (255,)
black = (0,)

def generate_vector(x, y):

    # find the location of the drill based on pixels  
    x0 = (var.pxl * x)
    y0 = (var.pxl * y)

    img = Image.open(var.name)
    crop_box = (x * 16, y * 16, x * 16 + 16, y * 16 + 16)  # x1, y1, x2, y2
    cropped_img = img.crop(crop_box)

    arr = np.array(cropped_img)

    # temp return 
    return arr


def compare_vectors(drill, index_v):
    score, diff = ssim(drill.vector, index_v, full=True)
    if (score > 0.5):
        print("SIMIALR !!! SSIM:", score)
        print("X: " + str(drill.x))
        print("Y: " + str(drill.y))