names=["a","b","c","d","e"]
print(names)
names1=names
print(names1)


# remove()
names=["a","b","c","d","e"]
names.remove("a")
print(names)

# pop()
names.pop()
print(names)

# clear()
names.clear()
print(names)

# index()
fruits = ["apple","mango","banana","papaya","apple","mango","grapes","apple"]
q1=fruits.index("apple")
print(q1)
q2=fruits.index("apple",1,5)
print(q2)
q3=fruits.index("apple",5)
print(q3)


# reverse()
cities = ["goa","nagpur","wardha","chennai","pune"]
cities.reverse()
print(cities)
fruits.reverse()
print(fruits)


# append()
cities.append("mumbai")
print(cities)
fruits.append("grapes")
print(fruits)



# insert()
cities.insert(3,"nagpur")
print(cities)
fruits.insert(5,"papaya")
print(fruits)



# extand()
n1=[1,2,3,4,5]
n2=[6,7,8,9,0]
n1.extend(n2)
print(n1)


n2.extend(n1)
print(n2)




h=[11,22,33]
j=h.copy()
j[0]=111
print(j)
print(h)





