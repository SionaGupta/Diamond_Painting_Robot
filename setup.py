import var 
from PIL import Image, ImageEnhance
import numpy as np

img = Image.open(var.name).convert("L")  # grayscale
arr = np.array(img)

# threshold
arr = np.where(arr > 125, 255, 0).astype(np.uint8)
bw_img = Image.fromarray(arr)

"""# Define the crop box: (left, upper, right, lower)
x = 8
y= 9
crop_box = (x * 16, y * 16, x * 16 + 16, y * 16 + 16)  # x1, y1, x2, y2
cropped_img = bw_img.crop(crop_box)

# Save under a new name
cropped_img.save("A.png")"""

bw_img.save(var.BW_name)
