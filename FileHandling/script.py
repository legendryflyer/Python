# program 1
# open the file for writting data

f=open("file.txt","w")
#enter the characters from keyword
e=input("enter the name")
#write the string into the file
f.write(e)
f.close()


# program 2
#g=open("file2.txt","w")
#str = g.read()
#print(str)
#g.close()

# program 3
#g=open("file2.txt","w")
#print("enter '@' to exit")
#while str != '@':
#    str = input("enter multiple names")
#    if str != '@':
#        g.write(str + "\n")
#g.close()


# program 4
h=open("file3.txt","+a")
print("enter '@' to exit")
while str != '@':
    str = input("enter multiple names")
    if str != '@':
        h.write(str + "\n")
h.seek(0,0)
str=h.read()
print(str)
h.close()

