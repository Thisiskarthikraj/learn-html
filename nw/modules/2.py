p=input("enter your password: ")
import re
a=r'[a-z]' 
b=r'[A-Z]'
c=r'[0-9]'
if re.search(a,p):
    pass
if re.search(b,p) :
    pass

 if re.search(c,p) :
    pass
if len(p)>7:
    print("strong")
else:print("reenter") 

