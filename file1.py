a= 0
b= 1
number=int(input("enter the number :"))

print(a)
print(b)

for i in range(2,number):
    c = a + b
    print(c)
    a = b
    b = c
