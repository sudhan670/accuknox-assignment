# For custom question I give the element passing two value to get the perfect answer
class Rectangle:
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth 
    
    def __iter__(self):
        yield {'length': self.length}
        yield {'breadth': self.breadth}