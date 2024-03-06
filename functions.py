def add(x,y):
    return x+y
a = add(2,4)
print(a)


# program 2 # error
def add2(x,y):
    print(x+y)
add2(3,5)
# add2() # add2() missing 2 required positional arguments: 'x' and 'y'

# defult arguments
# program 3

def addA(v=3,w=4):
    print(v+w)
addA()
addA(5,5)


# positional arguments
#def addC(x,y):
#    print(x+y)
#e=addC(1,1)
#print(e)

def addC(x,y):
    return (x+y)
e=addC(1,1)
print(e)


# program 4
def addD(*args):
    print(args)
    total = 0
    for x in args:
        total = total + x
    return total
q = addD(1,2,3,4,5,6,7,8,9,0)
print(q)

# program 5

def addInfo(**kwargs):
    print(kwargs)
    kwargs['city'] = "pune"
    return kwargs
info = addInfo(first_name = "tavish",last_name = "anade")
print(info)

# program 6
a=1 # globle veriable
def function():
    a = 5  # local veriable
    b = 4
    a = a+1
    print(a)
    print(b)
function()
print(a)


# program 7
a = 10 # globle veriable
def function2():
    print(a) # globle is used
    print(10)
function2()
print(a)


# program 8
h = 10
def myfunction():

    global h
    h=199
    print(h)
myfunction()
print(h)