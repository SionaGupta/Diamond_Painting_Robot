import serial 
import time
import colorcomp

drill_size = 0.110236

# Example Cords 
class Cord: 
    def __init__(self, x, y):
        # xth drill from the left  
        self.x = x

        #yth drill from the top 
        self.y = y

cords = [
    Cord(1, 1),
    Cord(3, 3),
    Cord(2, 4),
    Cord(4, 5),
    Cord(0, 0)
]

# same as ser, but printing to terminal 
def test():
    index = 0; 

    # for black 
    for c in colorcomp.color_coords["3"]:
        # Move to drill supply location
        drill_x, drill_y = 10, 20  # example supply location, To be Changed to reflect changing drill pick up locations
    
        x, y = c
        print(x)
        print(y)

        print(f"G01 X{drill_x} Y{drill_y+index*drill_size}")
        print(f"Moving to drill supply")
        index += 1
        time.sleep(2)  

        # Pick up drill
        print("M3")
        print("Picking up drill")
        time.sleep(2)  # wait for servo

        # Move to canvas position
        print(f"G01 X{x*drill_size} Y{y*drill_size}")
        print(f"Moving to canvas: X{x*drill_size} Y{y*drill_size}")
        time.sleep(2)

        # Place drill
        print("M3\n")
        print("Placing drill")
        time.sleep(2)


# for activated serial 
def ser():
    # Open Serial Port 
    ser = serial.Serial('/dev/tty.usbserial-110', 9600, timeout=1)
    time.sleep(2)

    index = 0

    # for black drills 
    for c in colorcomp.color_coords["3"]:
        # Move to drill supply location
        drill_x, drill_y = 4, -5  # example supply location, To be Changed to reflect changing drill pick up locations

        # Get X and Y
        x, y = c

        # grab drill 
        ser.write(f"G01 X{drill_x} Y{drill_y+index*drill_size}\n".encode())
        print(f"Moving to drill supply")
        time.sleep(4)  

        # index += 1


        # Pick up drill
        ser.write("M03\n".encode())
        print("Picking up drill")
        time.sleep(4)  # wait for servo

        # Move to canvas position
        ser.write(f"G01 X{x*drill_size} Y{y*drill_size}\n".encode())
        print(f"Moving to canvas: X{x*drill_size} Y{y*drill_size}")
        time.sleep(4)

        # Place drill
        ser.write("M03\n".encode())
        print("Placing drill")
        time.sleep(4)


    ser.close()

ser()