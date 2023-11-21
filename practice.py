"""a=int(input("enter your number :-"))
if (a>=1):
 b=[]
 sum=0
 for i in range(1,a+1):
    c=int(input("enter value no"+ str(i)+":"))
    b.append(c)
    
 for i in b:
    sum=sum+i

 avg=int(sum/a)
 print(b)
 print(sum)
 print(avg)     

else:
 print("enter valid number" )"""

a=1
b=2
number=int(input("enter input :"))
if(number==1):
    print(a)
elif(number==2):
    print(a)
    print(b)
else:
    for i in number:
        print(a)
        print(b)
        c=a+b
        print()