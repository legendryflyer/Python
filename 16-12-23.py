listA=["tavish","anade",20,64]
print(listA[0])
listA[1]="ande"
print(listA)


info={
    "first_name":"tavish",
    "middle_name":"anade",
    "last_names":"suresh",
    "age":20


}

print(info)
for item in info:
    print(item)

for item in  info.keys():
    print(item)

for item in info.values():
    print(item)

for k,v in info.items():
    print(k,v)


q1=info.get("first_name")
print(q1)



