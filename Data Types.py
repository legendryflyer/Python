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

list = [1,2,3,4,5,6]
print(type(list))
print(list[0])

list[2] = 44
print(list)

# for loop without using range
for x in list:
    print(x)


# for loop with using range
for x in range(len(list)):
    print(list[x])

# tuple
# tuple also stores value by index
# can't update single value
# tuple has fixed value
# cannot add a new value
# length of tuple is fixed


tuple = ("A","B","C")
print(type(tuple))


print(tuple[0])
print(tuple[1])
print(tuple[2])

# for loop without using range
for x in tuple:
    print(x)

#for loop using range
for x in range(len(tuple)):
    print(tuple[x])


# while loop
i=0
while(i < len(tuple)):
    print(tuple[i])
    i = i+1

#tuple[1] = "d"  cannot update single value of tuple

# to add value in tuple convert tuple into list

my_tuple = ("apple", "banana", "cherry")
my_list = list(my_tuple)
print(my_list)

