# program 1
#f1 = open('Screenshot 2023-03-25 220642.png','rb')
#f2 = open('image.png','wb')
#bytes = f1.read()
#f2.write(bytes)
#f1.close()
#f2.close()
import pickle


# program 2
#with open('sample.txt','w') as f:
#    f.write("I am learning js \n")
#    f.write("I am learning python \n")

#with open('sample.txt','r') as f:
 #   for line in f:
   #     print(line)


class emp:
    def __init__(self,fn,ln,age,rollno):
        self.firstname = fn
        self.lastName = ln
        self.age = age
        self.rollNo = rollno

#tavish = emp("tavish","anade",20,632)


#import pickle
#f =open('emp.dat','wb')
#n = int(input("how many emp: "))

#for i in range(n):
 #   fn = input("enter firstname")
  #  ln = input("enter lastname")
   # ag = input("enter age")
    #rn = input("enter rollno")
    #e = emp(fn,ln,ag,rn)
    #pickle.dump(e,f)
#f.close()

import pickle
f = open('emp.dat','rb')
while True:
    try:
        e = pickle.load(f)
        print(e.firstName)
        print(e.lastName)
        print(e.lastName)
        print(e.lastName)

    except EOFError:
        print("end of file reached")
        break
