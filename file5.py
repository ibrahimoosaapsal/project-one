#first problem:-
for i in range(1,6):
    for j in range(1,3):
        print(j,"apple")
#second problem

a=int(input("enter no of week:"))
b=int(input("enter no of days :"))
if(b<=7):
 for i in range(1,a+1):
    print("Week No :",i)
    for j in range(1,b+1):
      print("day :",j)
else:
   print("invalid input")

#third problem

a=int(input("enter the value :"))

for i in range(1,a+1):
    print(i,end=",")

for i in range(1,10):
    print()
    for j in range(1,i+1):
        print(j,end="")

a=int(input("enter number :"))

for i in range(1,a+1):
    print(i * "$")
  
