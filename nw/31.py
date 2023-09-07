class A:
    def display(self):
        print("hello") 
        self.__a = 20

       
class b(A):
    def sample(self):
            print("hai")
class c(b):
     def ik(self):
          print(10)
ob=c() 
ob.ik()
ob.display()  
ob.sample ()  

print(ob._A__a)
