dict={
    "firstname":"tavish",
    "lastname":"anade",
    "email":"tavishanade12@gmail.com",
    "rollno":64
}
dict2=dict
dict2["rollno"]=65
print(dict2)
print(dict)


#copy()
dict3=dict.copy()
dict3["firstname"]="sharayu"
print(dict3)
print(dict)


#update()
dict4={
    "plotno":"38"
}
dict.update(dict4)
print(dict)

dict4.update(dict)
print(dict4)


#popitem()
dict.popitem()
print(dict)

dict4.popitem()
print(dict4)


#setdefault()
q=dict.setdefault("firstname")
print(q)

w=dict.setdefault("middlename","suresh")
print(dict)
print(w)

#fromkeys()
props=["fn","ln","age"]
info=dict.fromkeys(props,0)
print(info)










