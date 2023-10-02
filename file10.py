#types of class variables


class phone():
    def __init__(self,brand,price,ram,storage):
        self.brand=brand
        self.price=price
        self.ram=ram
        self.storage=storage

    def display(self):
        print("brand :",self.brand)
        print("price :",self.price)
        print("ram :",self.ram)
        print("storage :",self.storage)

samsung=phone("samsung",20000,"6gb","128gb")
nokia=phone("nokia",12000,"6gb","256gb")

samsung.display()
print()
nokia.display()

#type of instance variable

class language():#creating a class 
    mothertough="tamil"#default variable foe all object
    def __init__(self,name,lan1,lan2):#function1
        self.lan1=lan1#asigning first value
        self.lan2=lan2#asigning second value
        self.name=name#asigning third value
    def display(self):#function 2
        print("name :",self.name)#print all values one by one
        print("mothertough :",self.mothertough)
        print("second language :",self.lan1)
        print("third language :",self.lan2)

language.mothertough="german"#changind default variables value
ayan=language("ayan","english","french")#creating object 1
apsal=language("apsal","english","spanish")#creating object 2

apsal.display()#call the object with class funtion
print()
ayan.display()

#types of funtional methods
#instance method is used self
class laptop():
    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)

hp=laptop()
hp.setprice(20000)
hp.getprice()

#class method
class laptop():
    chargertype="c-type"
    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)
    @classmethod#it will be used to run this charger function without giving: (laptop)
    def chargertype(cls):
        cls.chargertype="b-type"
        print("charger type changed")

hp=laptop()
hp.setprice(20000)
hp.getprice()
laptop.chargertype()

#static method 

class laptop():
    chargertype="c-type"
    def __init__(self):
        self.brand=""
        self.price=34
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)
    @classmethod#it will be used to run this charger function without giving: (laptop)
    def chargertype(cls):
        cls.chargertype="b-type"
        print("charger type changed")

    @staticmethod#this method will be help to work the function without self and class
    def info():
        print("this is sample static method")


hp=laptop()
hp.setprice(20000)
hp.getprice()
laptop.chargertype()
hp.info()

