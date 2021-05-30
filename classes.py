#Introduction to OOPS

class Point:

    #class attribute - same for all instances (objects) of this class
    desciption="2D point"

    #constructor
    def __init__(self,x,y):
    
        #x and y are instance attributes - different for every instance of this class
        self.x=x
        self.y=y
    
    def getx(self):
        return self.x
    
    
    # to print the point
    def __str__(self):
    
        return f"The point is ({self.x},{self.y})"
    
    #overloading the + operator
    def __add__(self,other):
        x=self.x + other.x
        y=self.y + other.y
        return Point(x,y) 
    
        
    

origin=Point(0,0)

#If you don't define the __str__, this will give the memory location of origin object.
print(origin)

#If you don't define the __str__, this will give the memory location of start object.
start=Point(1,5)
print(start)

#As start and origin are at different memory locations, they will be different
print(start==origin)

print(origin+start)

#address of the class function
print(Point.getx)

#gives the address of the instance method
print(origin.getx)

