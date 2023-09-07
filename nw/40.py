class animal():
    def __init__(self,name):
        self.n=name
class canfly():
    def fly():
        pass
class caswim():
    def swim():
        pass
class duck(animal):
    def __init__(self, color):
        self.n1=color
class duck(canfly):
    def __init__(self, color):
        self.n1=color
class duck(caswim):
    def __init__(self, color):
        self.n1=color
ob=duck(color="red")
print(ob.n1)

