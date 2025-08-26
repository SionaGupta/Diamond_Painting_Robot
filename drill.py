from classes import drill 
from PIL import Image 


def generate_vector(imgName):
    img = Image.open(imgName)
    pixels = img.load()
    r, g, b, a = pixels[0, 0]
    print (r)
    print(g)
    print(b)
    print(a)
    
name = "black.png"

generate_vector(name)