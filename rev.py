# variables
x=10
y=20

print("x")
print("y")
print(x+y)

# aritmatic oprations

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x % y)

a = 40
b = 30

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a % b)

#functions
def calculator(x,y):
    print(x + y)
    print(x-y)
    print(x*y)
    print(x/y)
    print(x % y)
calculator(45,67)

calculator(10,20)


#function without parameter nad without return

def add():
    print(8+7)
    print(6-2)
    print(6 % 5)
add()
add()
add()
add()


#function with para meters without return
def add(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
add(4,7)

#function with parameter and return

def add(x,y):
    return [x-y , x+y]

c=add(5,6)
print(c[0])
print(c[1])

#camparision oprators

print(10>20)
print(10<20)
print(10>=20)
print(10<=20)
print(10==20)
print(10!=10)

#logical oprators

print(10!=20 and 10<=20)
print(10==20 and 10<=20)
print(10!=20 and 10>=20)
print(10==20 and 10>=20)




print(10!=20 or 10<=20)
print(10==20 or 10<=20)
print(10!=20 or  10>=20)
print(10==20 or 10>=20)



#condition statement
marks=100
if(marks>90):
    print("GREAD A")
elif(marks>80):
    print("GRADE B")
elif(marks>70):
    print("GRADE c")
else:
    print("fail")

#list
list=["1","2","3","4","5"]
print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])



print(type(list[0]))
print(type(list))



def add(x,y):
    return [x-y , x+y, x*y, x/y ,x%y]


c=add(7,8)
print(c)
print(c[0]+c[4])

