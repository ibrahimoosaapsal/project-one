#funtions
def driver():
    print("Driving")

driver()

#first problem

def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
def div():
    print(a/b)
a=int(input("enter a value :"))
b=int(input("enter b value :"))
add()
sub()
mul()
div()

#second problem

def er(ayan):
    print("hello"+ayan)

er() 

#third problem

def findevenorodd(num=int(input("enter your number :"))):
    if(num==1):
        print("odd number")
    else:
        print("even number")

findevenorodd()

#forth problem

def result(num=int(input("enter your mark :"))):
    if(num>35):
        print("pass")
    else:
        print("fail")
result()

#fifth problem

def findrange(
     num=int(input("enter first num :")),
     num2=int(input("enter your num 2 :"))):
     for i in range(num,num2):
      print(i)

findrange()

#sixth program
u_name="apsal"
password=123

a=input("enter your name :")
b=int(input("enter your password :"))

def validate():
    if(a==u_name and b==password):
        return 'corect'
    else:
        return 'wrong' 

c=validate()
print(c)

#seventh program
a=int(input("enter a value :")) 
b=int(input("enter b value :"))
c=int(input("enter c value :"))

def add():
    return a+b

d=add()
print(d*c)

#eighth program

def add(n1,n2):
    return n1+n2

a=int(input("enter a :"))
b=int(input("enter b :"))
c=int(input("enter c :"))

added=add(a,b)
output=added*c
print(output)

