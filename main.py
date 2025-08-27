from classes import Drill 
from drill import generate_vector, compare_vectors
import var
from PIL import Image, ImageEnhance
import numpy as np

canvas = []


# iterate over each drill 
for y in range(var.d_height):
    row = []

    for x in range(var.d_length): 
        # create a drill object
        drill = Drill(x, y)

        # create drill vector
        drill.vector = generate_vector(x, y)

        #compare drill vector to color vectors 
        img = Image.open(var.index_name)  # grayscale
        arr = np.array(img)

        compare_vectors(drill, arr)

        #append drill to row
        row.append(drill)

    # append row y to canvas   
    canvas.append(row)

print("done")
