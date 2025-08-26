from classes import Drill 
from drill import generate_vector

# number of drill horizontally 
d_length = 47

# number of drills vertically
d_height = 47

# name of image
name = "space.png"

# dimension of a drill in pixels 
pxl = 16

canvas = []

# iterate over each drill 
for y in range(d_height):
    row = []

    for x in range(d_length): 
        # create a drill object
        drill = Drill(x, y)

        # create drill vector
        drill.vector = generate_vector(x, y, name, pxl)

        #compare drill vector to color vectors 

        #append drill to row
        row.append(drill)

    # append row y to canvas   
    canvas.append(row)


