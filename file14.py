#filehandling
#all are default function
f=open("text.txt","w")#open funtion is used to open the file amd set mode "w"-stands for write "r"-stands for read 
#content=f.read() this willbe used to read the file
#print(content)
#print(f) it will used to see the mode of the file
f.write("GOVA")#write method will be used to add the new record into a file but it will delete all existing record
f.write("gova")#adding another iteam
f.write("apple \n")#\n is used to declared this iteam if over and you should start a new iteam into  next line
f.write("apple \n")#same us above
f.close()#close function is used to close the file
#f=open("text.txt","r+")#change the file mode, r+ stands for readable and writeable
f=open("text.txt","a")#a stands for append it wont delete any data but adding a new data to it
f.write("apple\n")
f.write("apple\n")
f.write("apple\n")
f.write("apple\n")
f.close()#close the program
a=open("text.txt","r+") #we  can use the diffrent variable to open the file 

read=a.readline()#readline() used to read the first line only.
print(read)
