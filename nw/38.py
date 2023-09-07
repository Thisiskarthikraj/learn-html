# class A:
#     def func():
#         print("hello") 
# class B:
#     def fun():
#             print("namaste")
# class C(A,B):
#     def f():
#          print("hai")
# ob=C()
# ob.fun()
# ob.func()
# ob.f()

class a:
     def sample(self):
          print("hello")

class b:
     def sample2(self):
          print("hai")

class c(a,b):
     def sample3(self):
          print("welcome")
o = c()
o.sample3()
o.sample2()
o.sample() 