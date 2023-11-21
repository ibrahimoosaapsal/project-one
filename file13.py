#types of errors/exception handelling 
#typing error
print("hi")
#printt("hi")#this will be the typing error

#logical error
a=10
b=15
print(a+a)#this is the example for logical error
#runtime error it will be the mistake of user
a=int(input("enter a :"))#if user gives a integer means its program throwing error 
b=int(input("enter b :"))
c=a+b

print(c)

#lts see how to fix this
try:
    a=int(input("enter a :"))#if user gives a integer means its program throwing error 
    b=int(input("enter b :"))
    c=a+b
    print(c)
except Exception:
    print("invalid input")#give your msg here 

#if your willing to find the ivalid reason defaultly
# try this
try:
    a=int(input("enter a :"))
    b=int(input("enter b :"))
    print(a+b)
except Exception as e:#this exception will be work for all type of error
    print ("here is your reason :-",e) 

#another method
try:
    a=input()
    b=input()
    print(a/b)
except TypeError as e:
    print("reason :",e)  
finally:#finally will be work as defaultly when the error is throeing or not
    print("final statement")