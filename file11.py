"""#inheritance and its types
#single inheritance
class user():
    def name(self): 
     print("iam user")
class apple():
    def app():
      print("apple mobile")
class redmi():
    def red():
      print("redmi airpods")

ayan=user()#in this method we can't acces another class by this live
apsal=user()
ayan.name()
apsal.name()

#multiple inheritance
class user():#now we can use extra 2 classes
    def name(self): 
     print("iam user")
class apple():
    def app(self):
      print("apple mobile")
class redmi(user,apple):
    def red(self):
      print("redmi airpods")

ayan=user()
apsal=redmi()
ayan.name()
apsal.name()

#multi level inheritance

class user():
    def name(self): 
     print("iam user")
class apple(user):
    def app(self):
      print("apple mobile")
class redmi(apple):
    def red(self):
      print("redmi airpods")

ayan=redmi()#in this method we can't acces all class by this live
ayan.name()
ayan.app()
ayan.red()

apsal=apple()
apsal.name()

#another method

class lake():
    def water(self):
        print("water in litters")
class technician():
    def tech(self):
        print("water technician")
class plant1(lake,technician):
    pass
class plant2(lake):
    pass 
class plant3(lake):
    pass 

perambur=plant1()
veperi=plant2()
paris=plant3()

perambur.water()
veperi.water()
paris.water()
perambur.tech()

#super keywords and its types

class a():
       def __init__(self):#__init is a constructor it will be automatically called when the object is created
        print("a class")
       def display(self):
        print("diplay class")
class b(a):#class a is inherited into class b
    #def __init__(self):if the class b was not having constructor then class a contructor will be automatically called
        #print("b class ")
    def display(self):
        print("display class")


obj1=b()"""

#super keywords type2, if 2 class having 2 constructor but  we need to acces class a constructor then use super keyword

class a():
    def __init__(self):
        print("a class ")
    def display(self):
        print("you are in class a")

class b(a):
    def __init__(self):
        super().__init__()
        print("b class")
    def display(self):
        print("you are in class b")
        


object=b()