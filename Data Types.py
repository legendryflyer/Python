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
