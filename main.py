# variables
x  = 10
print(x)
x = 100
print(x)

# Arithmetic operation

q = 10
r = 5

print(q+r)
print(q-r)
print(q*r)
print(q/r)
print(q%r)

s = 8
t = 4

print(s+t)
print(s-t)
print(s*t)
print(s/t)
print(s%t)

# function
# def
# Calculator - funtion name
# x,y        - parameters
# 12,4       - arguments
def Calculator(x,y):
    # statements
    print(x + y)
    print(x - y)
    print(x * y)
    print(x /y)
    print(x % y)

# calling the function
Calculator(12,4)
Calculator(6,3)
Calculator(4,2)


# function without parameter and without return type
def addA():
    print(7+3)
addA()
addA()
addA()
addA()
addA()

# function with parmeter and without return type
def addB(x,y):
    print(x+y)
addB(3,4)
addB(13,4)
addB(11,4)

# function with parameter and with return type
# 100 -- display
# 100 -- given ---> 100 + 100 , 100 - 50 , 100 / 5 , 100 * 0.10

def addC(x,y):
    return x + y
q1 = addC(11,3)
print(q1)
print(q1 + q1)
print(q1 - 4)
print(q1 * 4)

# comparison operator
# < , > , <= , >= , != , ==
print(3 > 2)
print(3 < 2)
print(3 != 2)
print(3 == 2)
print(3 == 3)
print(3 >= 3)
print(3 <= 3)
print(3 >= 2)
print(3 <= 2)


# Logical operator

# and
# True    and    True   ----> True
# False   and    True   ----> False
# True    and    False  -----> False
# False   and    False  ----> False

print(7 == 7 and 8 == 8)
print(7 != 7 and 8 == 8)
print(7 == 7 and 8 != 8)
print(7 != 7 and 8 != 8)
# or


# True    or   True   ----> True
# False   or    True   ----> True
# True    or    False  -----> True
# False   or    False  ----> False
print(7 == 7 or 8 == 8)
print(7 != 7 or 8 == 8)
print(7 == 7 or 8 != 8)
print(7 != 7 or 8 != 8)

# not
# not True  ----> False
# not False ----> True
print(not (6 == 6))
print(not ( 6 != 6))



# condition statements
numT = 5
if numT > 0 and numT <= 5:
    print("10 discount")
if numT > 5 and numT <= 10:
    print("20 discount")
if numT > 10:
    print("30 discount")



numT = 5
if numT > 0 and numT <= 5:
    print("10 discount")
elif numT > 5 and numT <= 10:
    print("20 discount")
elif numT > 10:
    print("30 discount")
else:
    print("incorrect input")

marks = 33
if(marks > 90):
    print("Grade A")
if(marks > 65):
    print("Grade B")
if(marks > 55):
    print("Grade C")

if(marks > 90):
    print("Grade A")
elif(marks > 65):
    print("Grade B")
elif(marks > 55):
    print("Grade C")
else:
    print("Try again")