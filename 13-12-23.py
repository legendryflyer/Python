listA = ["tavish ","anade",20,64]
#retrive
print(listA[0])
# update
listA[1] = "ande"
# add
listA.append("pune")
#delete
#del listA
# total number of element
print(len(listA))

listA = ["tavish ","anade",20,64]
for item in listA:
    print(item)

for item in range(len(listA)):
    print(listA[item])

# dict
info = {
        "firstName":"tavish",
        "lastName":"anade",
        "age":20,
        "rollNo":64
}
# dict does not stores the value by index
q2 = info['firstName']
print(q2)
# update
info['lastName'] = "ande"
# add
info['city'] = "pune"
print(info)
# delete
#del info
print(len(info))

# Check whether  element is present
# looping through list
cities = ["wardha","pune","nagpur"]
for item in cities:
    print(item)
print("wardha" in  cities)

info2 = {
    "firstName":"tavish",
    "lastName":"anade",
    "age":20
}
print("age" in info2)
for item in info2:
    #print(item)
    print(item ,info2[item])


car = {
    "color":"blue",
    "model":"Q4",
    "company":"Audi"
}

for item in car:
    print(item,car[item])

#get()
q3 = car.get("model")