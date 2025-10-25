import serial 
import time

# Example Cords 
class Cord: 
    def __init__(self, x, y):
        # xth drill from the left  
        self.x = x

        #yth drill from the top 
        self.y = y

cords = [
    Cord(1, 2),
    Cord(2, 4),
    Cord(3, 6),
    Cord(4, 5),
    Cord(0, 0)
]


# Open Serial Port 
ser = serial.Serial('/dev/tty.usbserial-110', 9600, timeout=1)
time.sleep(2)

# Testing 
ser.write(b"Hello World\n")

# G-Code 
for c in cords: 
    ser.write(f"{c.x} {c.y}\n".encode())
    print("moving to " + c.x + " and " + c.y)
    time.sleep(0.1)


ser.close()

