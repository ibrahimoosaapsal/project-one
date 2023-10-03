"""#polymorphism read the code this does not much that difficult
def add(a,b,c=0):
    print(a+b+c)

add(1,2)
add(1,2,3)
# a single fuction will be used in multiple ways
#excercise 1 this also called polymorphism

class Animal():
    def sound():
        print("Animal makes sound")
class dog(Animal):
    def sound():
     print("dog barks")
class bird(Animal):
   def sound():
      print("bird is singing")

d1=dog()
b2=bird()
bird.sound()

#excercise no 2

class shape():
    def area(self):
     return 0
class rectangle(shape):
   def area(self,lenth,breath):
      self.lenth=lenth
      self.breath=breath
      print(lenth*breath)

    
    
obj=rectangle()
obj.area(12,12)

# excercise no 3 :-

class person(): #creating a class called person
    
    def __init__(self,name):#start the constructor function
       self.name=name#pass the name variable as parameter

    def fun(self):#this fun will be just for inheritance understanding
        print("hello")
    

class student(person):#inherte the person class to it
    
    def __init__(self,name,grade):# contructor function is for taking name and grade
        super().__init__(name)#calling person class constructor in the use of super keyord
        self.grade=grade
    
    
    def display(self):
        print(self.name,self.grade)

apsal=student("apsal","b grade")#giving a two parameter to the student class and defaultly called two constructor
apsal.display()#calling the final function
apsal.fun()#just for simple understang for in heritance

#constructor is a funtion which is cakked defaultly when theobj is created

#excercise no 4

class vehicle():
    def start(self):
        print("vehicle start")
class car():
    def start(self):
        print("car start....")

benze=car()
benze.start()"""

#excercise 05

class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
     def __init__(self,department,name,salary):
         super(). __init__(name,salary)
         self.department=department


     def display(self):
         print(self.name,self.salary,self.department)

emp1=manager("apsal","10,000","biotech")

emp1.display()
         


