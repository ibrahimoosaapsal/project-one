"""#ifelse excercise
mark=int(input("enter your mark :"))

if (mark >= 35):
   print("you are pass")
else:
    print("you are fail")

# second excercise

income=int(input("enter your income :"))

if(income<=7000):
    print("you are eligible for scholarship")

else:
    print("you are not eligible for scholarship")

#third excercise

number=int(input("enter your number :"))

if(number%3==0 and number%5==0):
    print("its divisible by 3 and 5")

else:
    print("its not divisible by 3 and 5")

    #forth program

number=int(input("enter your number :"))

if(number%2==1):
    print("this is odd number")

else:
    print("this is even number")

score=int(input("enter your score"))

if(score<=35):
    print("poor student")
elif(score>=35 and score<=70):
    print("average student")
elif(score>100):
    print("invalid input")
    
else:
    print("good student")

#fifth program

print("welcome to the mini calcukator")

a=int(input("enter a value :"))
b=int(input("enter b value :"))

print("plz type your program : add/sub/mul/div")
answer=input("enter your choice :")

if(answer=="add"):
    print(a+b)

elif(answer=="sub"):
    print(a-b)

elif(answer=="mul"):
    print(a*b)
  
elif(answer=="div"):
    print(a/b)

else:
    print("invalid input")

#sixth program
percentage=int(input("enter you percentage :"))

if(percentage>=70 and percentage<100):
    print("plzz write down this field")
    name=input("enter your name :")
    age=int(input("enter youe age :"))
    department=input("enter your department :")
    print("thank you for your response!!")
    print("you are eligible")
elif(percentage>100):
    print("invalid input")

else:
    print("you are not eligible")

#seventh program
salary=int(input("enter your salary :"))
age=int(input("enter your age :"))

if(salary>=20000 or age <= 25):
    print("you are eligible for loan")
    amount=int(input("plzz enter your required amount :"))
    if(amount<=50000):
         print("ok we will contact you soon")
    else:
          print("sorry the maximum amount is 50,000!")
else:
    print("you are not eligible")"""

#eighth program
a=int(input("enter your  tamil mark :"))
b=int(input("enter your english mark :"))
c=int(input("enter your maths mark :"))
d=int(input("enter your science mark :"))
e=int(input("enter your social mark :"))
total=a+b+c+d+e
avg=total/5

if(avg>=35 and avg<=100):
        print("you are good to go")
elif(avg>100):
        print("invalid input")
else:
        print("you need attent more classes")



