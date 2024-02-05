# program 1
def add(x,y):
    return x+y
q1=add(1,2)
print(q1)


# program 2
add=lambda a,b:a+b
print(add(2,3))



#program 3
s=lambda x:x*x
print(s(4))


#program 4
def addAll(*args):
    print(args)
    total=0
    for item in args:
        total=total+item
        return total

g=addAll(12,13,14,15,16,2,3,4,56,78,6,543,456,54,3,2,3,4,5,6,7,6,54,3,4)



# program 5
def updateCity(**kwargs):
    print(kwargs)
    kwargs['city'] = "nagpur"
    return kwargs
f2 = updateCity(fullName = "chinmay",city = "pune", age= 34)
print(f2)


# program 6
def addition(x = 4,y= 6):
    print(x+y)
addition()
addition(1,2)


# program 7

def addition(x3,x2,x1):
    print(x3+x2+x1)
    print(x3)
addition(x1 = 3,x2 = 4,x3 = 10)


