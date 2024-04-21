# rb = open('image.png','rb')
# rb2 = open('image2.png','wb')
# bytes = rb.read()
# rb.close()
# rb2.close()


# # program 2
# with  open('file2.txt','w') as  f:
#     f.write("learning python\n")
#     f.write("learning js")
    
    
# program 3

# user defined  function to check the file extension 

import pickle

class emp:
    def __init__(self,fn,ln,age):
        self.firstName = fn,
        self.lastName = ln,
        self.age = age

    def displayData(self):
        print(self.firstName)
        print(self.lastName)
        print(self.age)
        
f = open('employee.dat', 'ab+')  
noOfObjects = int(input('enter the number of objects'))

for x in  range(noOfObjects):
    fn = input('Enter first name : ')
    ln = input('Enter last name : ')
    age = int(input('Enter Age : '))
    obj = emp(fn,ln,age)
    pickle.dump(obj,f)
f.close()


# with open(r'employee.dat','rb') as f:
#     f.seek(0,0)
#     content = f.read()
#     # content = content.decode()
#     print(content)


# # three modes 
# # read , write , append

# # creation a object
# # f  = open('myfile.txt','w')
# # # taking user input
# # str = input('Enter the name')
# # # writing to the file
# # f.write(str)
# # # closing the filec
# # f.close()

# # program 2
# #
# f = None
# try:
#     fileName = input('enter the filename')
#     f = open(fileName,'r')
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print("File not found")
# finally:
#     if f is not None:
#         f.close()
# print("bye")

# program 1 
# read , write and append

# opening the file 
# f = open("myfile2.txt",'w')
# # taking input from the user
# name = input('Enter the name')
# # writing to file
# f.write(name)
# # closing
# f.close()

# program 2
# fileName = input('please enter the fileName')
# f = open(fileName,'r')
# str = f.read()
# print(str)
# f.close()

# program3
# f = None
# try:
#     fileName = input('please enter the fileName')
#     f = open(fileName,'r')
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print("file not found")
# finally:
#     if f is not None:
#         f.close()

# program4
# f = open('myfile3.txt',"w")
# while str != "@":
#     str = input('Enter the name'+'\n')
#     if str != '@':
#         f.write(str + '\n')
# f.close()

# program 5
# r w
# f = open('myfile2.txt','a+')
# while str != "@":
#     str = input("Enter the names")
#     if str != '@':
#         f.write(str + "\n")
# f.seek(0,0)
# str2 = f.read()
# print(str2)
# f.close()

# program 2

import os , sys
# fname = input('Enter the filename: ')
# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     sys.exit()
# print('The file contents are: ')
# str = f.read()
# print(str)
# f.close()


#count word character and lines

fname = input('Enter the filename: ')
if os.path.isfile(fname):
    f = open(fname,'r')
else:
    print("file does not exist")
    sys.exit()

cc = 0
cw = 0
cl = 0

for line in f:
    cl = cl + 1
    list = line.split() #["chinmay","learning" ,"js"] 
    cw = cw + len(list)
    cc = cc + len(line)
print(cl)
print(cw)
print(cc)

f.close()


f.close()
    
    
    