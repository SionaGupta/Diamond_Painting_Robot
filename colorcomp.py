from PIL import Image
import numpy as np


# pixels per diamond symbol 
diamond_size = 16


# all colors 
diamond_colors = {
    "1": (169, 181, 204),
    "2": (250, 234, 224),
    "3": (0, 0, 0),
    
}

#load image
image = Image.open("space.png").convert("RGB")
img_array = np.array(image)
height, width, _ = img_array.shape

# num diamonds in rows and columns
diamond_rows = height // diamond_size
diamond_cols = width // diamond_size


def get_dominant_color(block):
    # Flatten to a list of pixels
    pixels = block.reshape(-1, 3)

    # Count nearest match of each colors (change to average?)
    colors, counts = np.unique(pixels, axis=0, return_counts=True)
    dominant_color = colors[np.argmax(counts)]

    return tuple(dominant_color)

# dictionary to store diamond cords per color
color_coords = {color_name: [] for color_name in diamond_colors.keys()}

'''
for i in range(diamond_rows):
    for j in range(diamond_cols):

        # get the block of pixels for this diamond
        block = img_array[
            i*diamond_size:(i+1)*diamond_size,
            j*diamond_size:(j+1)*diamond_size
        ]

        # get the dom color
        dominant = get_dominant_color(block)
        
        # Match dominant color to diamond_colors
        for color_name, rgb in diamond_colors.items():
            if np.linalg.norm(np.array(dominant) - np.array(rgb)) < 30:  # tolerance
                color_coords[color_name].append((i+1, j+1))  # diamond coordinates start at 1
                break
'''

i = 4 - 1
j = 16 - 1
    
    #pixel block
block = img_array[
        i*diamond_size:(i*diamond_size + 5),
        j*diamond_size:(j*diamond_size + 5)
    ]

dominant = get_dominant_color(block)

for color_name, rgb in diamond_colors.items():
            if np.linalg.norm(np.array(dominant) - np.array(rgb)) < 30:  # tolerance
                print("diamond color:", color_name)  # diamond coordinates start at 1
                print(dominant)
                break

