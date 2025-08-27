from classes import Drill 
from drill import generate_vector
import var 
from PIL import Image, ImageEnhance
import numpy as np

canvas = []

img = Image.open(var.name).convert("L")  # grayscale
img.save("og_img.png")

# increase contrast
enhancer = ImageEnhance.Contrast(img)
enhancer = ImageEnhance.Contrast(img)
contrast_img = enhancer.enhance(2.0)
contrast_img.save("contrast.png")

arr = np.array(img)

# threshold
arr = np.where(arr > 125, 255, 0).astype(np.uint8)
bw_img = Image.fromarray(arr)
bw_img.save("BW_space.png")

"""
# iterate over each drill 
for y in range(var.d_height):
    row = []

    for x in range(var.d_length): 
        # create a drill object
        drill = Drill(x, y)

        # create drill vector
        drill.vector = generate_vector(x, y)

        #compare drill vector to color vectors 

        #append drill to row
        row.append(drill)

    # append row y to canvas   
    canvas.append(row)
"""

print("done")
