#classes and objects:-
#classes is nothing bur set of functions 
class coding:#this is class
    name="unname"
    age=123
    def c(self):#function 1
     print("start coding")
    def java(self):#function 2
       print("stat coding with java")
    def python(self):#function 3
       print("start coding with python")

ayan=coding()
apsal=coding()

ayan.name="ayan"
apsal.name="ibrahim"#to assign this value to that empty name variable;
apsal.age=23
ayan.age=24
print(apsal.name)
print(ayan.name)
apsal.python()
print(ayan.age)

#second problem:- 

class laptop:
    price=0
    processor="none"
    ram="none"

hp=laptop()
dell=laptop()
lenova=laptop()

hp.price=50000
hp.processor="i5"
hp.ram="6gb"

dell.price=40000
dell.processor="i6"
dell.ram="8gb"

lenova.price=60000
lenova.processor= "i8"
lenova.ram="12gb"


#third problem:-

class laptop: #creating a class
    def __init__(self):#__init__ is a default function which will be called automatically when the object was created
        self.price=""#common variable for all object
        self.ram=""
        self.processor="" 
    def info(self):#this is a normal function
        print("price :",self.price)#self will be help to identifier of the function
        print("ram :",self.ram)
        print("processor :",self.processor)

hp=laptop()#it will be help to define this object is for laptop class
hp.ram="6gb"# it will defines his configration 
hp.processor="i5"
hp.price=50000

dell=laptop()#same us above
dell.price=55000
dell.processor="i6"
dell.ram="6gb"

lenovo=laptop()# same us above
lenovo.price=60000
lenovo.ram="8gb"
lenovo.processor="i7"

hp.info()#calling a second funtion while the first function will be called automatically
lenovo.info()
dell.info()

#forth problem

class student:#creating a class name student
    def __init__(self):#creating 2 variables name ,registernumber while the uses of constructor
        self.name=""
        self.regno=00
    def display(self):#creating a function called display
        print("student detailes")
        print("name :",self.name)#it will be return name
        print("regNO :",self.regno)

s1=student()
s2=student()
s3=student()

s1.name="apsal"
s1.regno=181747
s2.name="yogi"
s2.regno="s181784"
s3.name="ayan"
s3.regno="s131454"

s3.display()
print()
s2.display()
print()
s1.display()

#fifth problem

class fruits:
    def __init__(self,col):
      self.color=col
    
apple=fruits("red")
print(apple.color)

#sixth program

class teacher:
   def __init__(self,name,regno):
      self.Name=name
      self.registerno=regno
   def display(self):
      print("name :",self.Name)
      print("regNo :",self.registerno)


t1=teacher("apsal","001")
t2=teacher("ayan","002")

t1.display()
t2.display()

#seventh program

class calculator:
   def __init__(self,a,b):
      self.num1=a
      self.num2=b
   def add(self):
      print("added value :",self.num1+self.num2)
   def sub(self):
      print("sub value :",self.num1-self.num2)      
   def mul(self):
      print("mul value :",self.num1*self.num2)
   def div(self):
      print("div value :",self.num1/self.num2)

value1=calculator(12,12)
value2=calculator(13,14)




value1.add()
value1.sub()
value1.mul()
value1.div()
print()
print()
value2.add()
value2.sub()
value2.mul()
value2.div()

