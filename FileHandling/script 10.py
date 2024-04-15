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

# class emp:
#     def __init__(self,fn,ln,age):
#         self.firstName = fn,
#         self.lastName = ln,
#         self.age = age

#     def displayData(self):
#         print(self.firstName)
#         print(self.lastName)
#         print(self.age)
        
# f = open('employee.dat', 'ab+')  
# noOfObjects = int(input('enter the number of objects'))

# for x in  range(noOfObjects):
#     fn = input('Enter first name : ')
#     ln = input('Enter last name : ')
#     age = int(input('Enter Age : '))
#     obj = emp(fn,ln,age)
#     pickle.dump(obj,f)
# f.close()


with open(r'employee.dat','rb') as f:
    f.seek(0,0)
    content = f.read()
    content = content.decode()
    print(content)

    
    
    