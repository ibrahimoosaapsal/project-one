"""#first problem:-
i=10

while(i<=200):
    print(i,end=",")
    i=i+10

#second problem:-
i=10

while(i>=0):
    print(i)
    i=i-1"""

#third problem

i=int(input("ehter the number :"))
fact=1

while(i>0):
    fact=fact*i
    i=i-1

print(fact)

#forth program

a=[]
sum=0

for i in range(10):
    c=int(input("enter value no"+str(i+1)+":"))
    a.append(c)

for i in a:
    sum=sum+i

print(sum)
print(sum/10)