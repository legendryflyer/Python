#list
fruits=["apple","mango","banana","coconut","chikoo"]
print(len(fruits))
a=len(fruits)
print(a)


#without range
for x in fruits:
    print(x)

#range
for x in range(10):
    print(x)

for x in range(len(fruits)):
    print(fruits[x])



for x in range(2,10):
    print(x)

for x in range(2,22,2):
    print(x)


for x in range(5,51,5):
    print(x)

#program 2

cities=["mumbai","delhi","kolkata","chennai","nagpur","indore","bhopal"]
b=len(cities)
print(b)
cities[0]="banglore"
print(cities)
cities[6]="mumbai"
print(cities)

for x in cities:
    print(x)


for x in range(len(cities)):
    print(cities[x])


#program 3
numbers=["00","11","22","33","44","55","66","77"]
print(len((numbers)))

for x in range(len(numbers)):
    print(numbers[x])

print("00" in numbers)
print("87" in numbers)


for x in numbers:
    print(x)


numbers.append('88')
print(numbers)

numbers.append('99')
print(numbers)
print(numbers)



def add(x,y):
    return [x-y , x+y, x*y, x/y ,x%y]


c=add(7,8)
print(c)
print(c[0]+c[4])
d=len(c)
print(d)

for x in c:
    print(x)


for x in range(len(c)):
    print(c[x])



