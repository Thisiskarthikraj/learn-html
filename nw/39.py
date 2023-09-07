class a:
    def a(self):
        print(2)
class b(a):
    def b(self):
        print(7)
class c(a):
    def c(self):
        print(5)
obj=c()
obj1=b()
obj.c()
obj1.b()
obj.a()

