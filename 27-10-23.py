# operators -

# Arithmetic operation
a = 10
b = 5
print(a+b)
firstName = "chinmay"
lastName = "deshpande"
print(firstName + lastName)

q1  = 10
q2 = 5

print(q1+q2)
print(q1-q2)
print(q1*q2)
print(q1/q2)
print(q1%q2)

# comparison operators
# entity < entity  ---- boolean  True or False
# < , >, <= , >= ,== ,!=

print(12 < 4)
print(12 > 4)
print(12 !=  4)
print(12 ==  4)
print(12 ==  12)
print(12 >=  12)
print(12 <=  12)
print(12 <=  13)
print(12 >=  13)
# logical operators

# and
# True    and   True  ----->  True
# # False   and   True  ----->  False
# # True    and   False  ---->  False
# # False   and   False  -----> False

print(3 == 3 and 4 == 4)
print(3 != 3 and 4 == 4)
print(3 == 3 and 4 != 4)
print(3 != 3 and 4 != 4)


# or

# True    or   True  ----->  True
# False   or   True  ----->  True
# True    or   False  ---->  True
# False   or   False  -----> False

print(3 == 3 or 4 == 4)
print(3 != 3 or 4 == 4)
print(3 == 3 or 4 != 4)
print(3 != 3 or 4 != 4)

# not
#not True --- False
#not False --- True

print(not(6 == 3))
print(not (6 == 6))