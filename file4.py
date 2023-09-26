#print the table:-

j=int(input("enter the number"))

for i in range(1,11):
    print(j,"x",i,"=",i*j)

    #second problem
a=int(input("enter a value :"))
b=int(input("enter b value :"))

for i in range(a+1,b):
    print(i)

#third problem

for i in range(1,11):
    if(i%2==0):
        print(i)

#forth problem
count=0

for i in range(1,11):
    if(i%2==0):
      count=count+1
print(count)#this space is matter

count=0
n=int(input("find the odd number enter your value :"))

for i in range(1,n+1):
  if(i%2==1):
    count=count+1
print("odd number :",count)

#fifth problem
count1=0
count2=0
n=int(input("enter the number :"))

for i in range(1,n+1):
    if(i%2==1):
     count1=count1+1
    else:
       count2=count2+1
         
print("number of odd numbers :",count1)
print("number of even numbers :",count2)

#sixth program

a=int(input("enter the no :"))
count=0
for i in range(1,a+1):
    if(i%3==0 and i%5==0):
         count=count+1
         
print(count)
count=0
for i in range(1,6):
   count=count+i

print(count)

#seventh program 

a=[]
print("enter 10 values :")

for i in range(10):
    b=int(input("enter value "+str(i+1)+":- "))
    a.append(b)
    
print(a)

sum=0

for i in a:
    sum=sum+i

print("total=",sum)
print("average=",sum/10)

#eight program

a=int(input("enter the number"))
b=[]

for i in range(1,a+1):
    c=int(input("enter value no "+str(i),":-"))
    b.append(c)
print(b)
sum=0

for i in b:
     sum=sum+i

print(sum)
print(sum/a*100)

#ninth program

a=int(input("enter your number"))
b=[]
c=0
for i in range(1,a+1):
  c=c+1
  b.append(c)

print(b)

a=int(input("enter your value :"))

for i in range(1,a+1):
    print("Number is :",i,"cube is :",i*i*i)

a=int(input("enter number"))

for i in range(1,a+1):
   print("*"*i)
