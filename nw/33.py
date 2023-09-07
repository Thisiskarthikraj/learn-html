class  employee:
    def dis(self,name,salary):
        self.n=name
        self.x=salary
        print(self.n,self.x)
class manager(employee):
    def __init__(self, department):
        self.d=department

obj=manager(department=9)
print(obj.d) 
obj.dis("abc",10000) 
        