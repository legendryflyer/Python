# string
str = "tavish"
print(str[1])
print(type(str))
# string stores value by index

strA = "anade"

# for loop without range
for x in strA:
    print(x)

# for loop with range
for x in range(len(str)):
    #print(x) # index
    print(str[x])


# list

listA = [1,2,3,4,5,6]
print(type(list))
print(listA[0])

listA[2] = 44
print(list)

# for loop without using range
for x in listA:
    print(x)


# for loop with using range
for x in range(len(listA)):
    print(listA[x])

# tuple
# tuple also stores value by index
# can't update single value
# tuple has fixed value
# cannot add a new value
# length of tuple is fixed


tupleA = ("A","B","C")
print(type(tupleA))


print(tupleA[0])
print(tupleA[1])
print(tupleA[2])

# for loop without using range
for x in tupleA:
    print(x)

#for loop using range
for x in range(len(tupleA)):
    print(tupleA[x])


# while loop
i=0
while(i < len(tupleA)):
    print(tupleA[i])
    i = i+1

#tuple[1] = "d"  cannot update single value of tuple

# to add value in tuple convert tuple into list

my_tuple = ("apple", "banana", "cherry")
my_list = list(my_tuple)
print(my_list)


my_list[0] = "mango"
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)


# set 

setA = {11,22,33,4,55,667,7777,7,7,7}
print(type(setA))

# set do not store duplicate values 
print(len(setA))

# set do not stores the value by index 

# print(setA[0])

for item in setA:
    print(item)
    
# add() 
setA = {11,22,33,4,55,667,7777,7,7,7}
setA.add(6666)
print(setA)

# pop() remove the element of set randomly

setA.pop()
print(setA)

# remove() we have to pass the element  which we want to remove from the set

setA.remove(55)
print(setA)

# methord on set 

setA={11,22,33,44,55}
setB={44,55,66,77,88}

# newSet=setA.intersection(setB)
# print(newSet)


# intersection()
# newSet=setA.intersection(setB)
# print(newSet)

# intersection_update()

# setA={11,22,33,44,55}
# setB={44,55,66,77,88}
# nnnSet = setA.intersection_update(setB)
# print(nnnSet)
# print(setA)


# union
# setC=setA.union(setB)
# print(setC)

# there is no such thing like union_update in python 

# difference()


setA={11,22,33,44,55}
setB={44,55,66,77,88}

# setD = setA.difference(setB)
# print(setD)

# difference_update ()


# setE=setA.difference_update(setB)
# print(setA)

# setB.difference_update(setA)
# print(setB)

#  symmetric_difference()


# setW = setA.symmetric_difference(setB)
# print(setW)

# setV=setB.symmetric_difference(setA)
# print(setV)


setA={11,22,33,44,55}
setB={44,55,66,77,88}



