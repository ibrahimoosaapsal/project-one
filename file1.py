a= 0
b= 1
number=int(input("enter the number :"))

if number == 1:
  print(a)

elif number == 2:
  print(a)
  print(b)
  
elif number <= 0:
   print("invalid input")

else:
     for i in range(2,number):
        c = a + b
        print(c)
        a = b
        b = c
    