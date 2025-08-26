# class for each drill on the canvas 
class drill: 
    def __init__(self, x, y, vector, color):
        # xth drill from the left  
        self.x = x

        #yth drill from the top 
        self.y = y

        # symbol vector
        self.vector = vector

        # drill color 
        self.color = color

# class for each color 
class color:
    def __init__(self, number, vector):
        # color number
        self.number = number
        # color symbol vector
        self.vector = vector