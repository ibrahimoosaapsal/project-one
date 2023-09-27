"""i=10
while(i<=200):
    print(i)
    i=i+10
#list and their functions
a=[1,2,3,4,5,6]#sample list
print(a)
a.append(7)#add the data to the list
print(a)
a.insert(1,1.5)#insert the data into their desired position 
print(a)
a.pop(1)#delete the data and number is help to find the  position
print(a)
b=[8,9,10,11,12,13]#new list
print(b)
a.extend(b)#extend() is use to concordinate the two list 
print(a)
b.extend(a)
print(b)

#tuples tuples can allow duplicate values but it can,t modify but we can casting

a=(1,2,3,4,5,6,7)#this tis tuple it classify with circle braket 
print(a)
b=list(a)
print(b)#see the diffrence between the previous print 
b.pop()#if pop does not have any value then he will remove the last element defaultly

#sets sets cant allow duplicate value but we can add or remove data and its un-ordered

a={1,2,3,4,51,1}#sets can be declared as calibraces
print(a)#see the diffrence beetween the numbers and we cannot assign the value
a.add(23) #we can add the element
print(a)
a.remove(4)#we can remove with this 
print(a)
b={"apsal","ayan","deva"}# set are always un ordered
print(b)"""

#dictionary dictionary is same as js object but sintax willl be diffrent

a={
    "key" : "value"#this is the syntax of dictionay
}

b={
    "name":"apsal",
    "age":23,
    "height":6.8
}

print(b)
print(b["age"])# this is the syntax used to select the selected  value
b["height"]="hello" #this is the method to update the dictionary
print(b)
b.update({"height":6.8})# this is the another method to update
print(b)
b.pop("age") #this is the way to delete
print(b)
del b["height"]# 2nd way to delete
print(b)
del a #delete whole dictionay
print(a)
b.clear()#this is the type to clear all the data in the dictionay
print(b)
