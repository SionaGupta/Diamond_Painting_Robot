from classes import Drill 
from drill import generate_vector
import var 

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

        #append drill to row
        row.append(drill)

    # append row y to canvas   
    canvas.append(row)


