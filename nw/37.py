class person:
    def __init__(self,name,age):
        self.a=name
        self.b=age
class emplyoee:
    def __init__(self,salary):
        self.s=salary
class manager(emplyoee):
    def __init__(self, department):
        self.d=department
        print(self.d)
obj=manager(department="bca")