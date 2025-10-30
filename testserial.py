import serial 
import time
import colorcomp


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


# Open Serial Port 
ser = serial.Serial('/dev/tty.usbserial-110', 9600, timeout=1)
time.sleep(2)


for c in cords:
    # Move to drill supply location
    drill_x, drill_y = 10, 20  # example supply location, To be Changed to reflect changing drill pick up locations

    ser.write(f"G0 X{drill_x} Y{drill_y}\n".encode())
    print(f"Moving to drill supply")
    time.sleep(4)  

    # Pick up drill
    ser.write("M3\n".encode())
    print("Picking up drill")
    time.sleep(4)  # wait for servo

    # Move to canvas position
    ser.write(f"G01 X{c.x} Y{c.y}\n".encode())
    print(f"Moving to canvas: X{c.x} Y{c.y}")
    time.sleep(4)

    # Place drill
    ser.write("M3\n".encode())
    print("Placing drill")
    time.sleep(4)


ser.close()

