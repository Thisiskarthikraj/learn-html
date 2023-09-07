class shape:
    def __init__(self,color,size):
        self.k=color
        self.p=size
        print(self.k,self.p)
class circle(shape):
    def __init__(self,radius):
        self.r=radius
        print(self.r)
obj=circle(radius=3)
obj=shape(size=6,color="blue")