from PIL import Image
import numpy as np


# pixels per diamond symbol 
diamond_size = 16


# all colors 
diamond_colors = {
    "1": (169, 181, 204),
    "2": (250, 234, 224),
    "3": (0, 0, 0),
    "4": (101, 106, 113),
    "5": (165, 171, 177),
    "6": (134, 136, 140),
    "7": (255, 255, 255), # Fill out Later
    "8": (66, 124, 170),
    "9": (195, 198, 178),
    "A": (218, 97, 36),
    "B": (246, 155, 32),
    "C": (239, 198, 53),
    "D": (236, 218, 102),
    "E": (239, 236, 165),
    "F": (235, 185, 156),
    "G": (222, 239, 241),
    "H": (104, 115, 158), 
    "J": (122, 159, 206),
    "K": (180, 207, 226),
    "L": (37, 73, 107),
    "N": (255, 255, 255),
    "O": (32, 54, 120),
    "P": (48, 52, 68),
    "R": (250, 254, 247),
    "S": (167, 77, 39),
    "T": (55, 84, 92),
    "U": (65, 57, 32),
    "V": (38, 43, 46),
    "X": (215, 171, 89),
    "Y": (31, 169, 237),
    "Z": (76, 71, 40),
    "?": (203, 195, 202),
    "Y/": (206, 216, 225), 
    "m": (136, 190, 199),
    "b": (243, 240, 219),
    ">": (205, 124, 62),
    "triangle": (71, 83, 76),
    "upside arrow": (128, 134, 165),
    "block": (107, 128, 186),
    "spade": (40, 96, 144),
    "+": (141, 116, 100),
    "h": (166, 140, 103),
    "/": (250, 254, 247)
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

    # Compute the average color across all pixels
    avg_color = np.mean(pixels, axis=0)

    # Convert to integer RGB tuple
    return tuple(avg_color.astype(int))

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

def get_color(x, y):
    i = y - 1 #Y 
    j = x - 1 # X 
        
        #pixel block
    block = img_array[
            (i*diamond_size):int((i+1)*diamond_size) ,
            j*diamond_size+1:int((j+0.25)*diamond_size) 
        ]

    dominant = get_dominant_color(block)

    # testing boundries 
    crop_box = (j * diamond_size, i*diamond_size,(j+1)*diamond_size ,(i+1)*diamond_size)  # x1, y1, x2, y2
    cropped_img = image.crop(crop_box)

    # Save under a new name
    cropped_img.save("b.png")


    for color_name, rgb in diamond_colors.items():
        if np.linalg.norm(np.array(dominant) - np.array(rgb)) < 25:  # tolerance
            print("diamond color:", color_name)  # diamond coordinates start at 1
            break


    print(dominant)

get_color(21, 19)
