import math


class Vector():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):

        return "Vector" +str(self.x)+ "," +str(self.y) 

    def __add__(self):
        sum = x + y
        return sum


    def __sub__(self):
        minus = x-y
        return minus

    def __mul__(self):
        multiply = x*y
        return multiply
        
    def __len__(self):
        length = x + y 
        return length    # chose to use this calculation for length

    def comparison(self):
        if x > Y:
            return "x is the larger value"
        elif x < y:
            return "x is smaller than y"
        else:
            return "x and y values are equal"




import cmath

class MyComplex(Vector):

    z = complex(x,y)                    #creating a complex number, using 2 values as not clear on how many values to use
    z1 = complex(x1,y2)
    complex_mul = (z)*(z1)
    return complex_mul


    def complex_conjugate:             
        con1 = z.conjugate()
        con2 = z1.conjugate()
        return con1,con2
        


    def __str__(self):

        return "MyComplex" +str(self.x)+ "," +str(self.y) 



 

    



