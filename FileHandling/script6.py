#program 1
f = open('myFile.txt','w')
str = input("enter the name: ")
f.write(str)
f.close()
print ("file created")


# program 2

f = open('myFile.txt','r')
print(f.read())
f.close()


#  program 3

# f = open(input("enter the file name: "))
f = None
try:
    f = open(input("enter the file name: "))
    print(f.read())
except  FileNotFoundError:
    if f is  not None:
        f.close()
    print("the file does not exist")
        
finally:
    f.close()