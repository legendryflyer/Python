# string as a parameter and string as a return type
def greet(name):
    return "hellow" + name
q1=greet("  tavish")

print(q1)


# list as a parameter and list as a return type
city=["pune","mumbai","banglore","kolkata"]
def addcity(lst):
    lst.append("nagpur")
    return lst
q2=addcity(city)
print(q2)




#dictnary as a parameter and dictnary as a return type
info={
    "firstname":"tavish",
    "lastname":"anade"
}

def addlanguage(information):
    information.update({"language":"marathi"})
    return information
q3=addlanguage(info)
print(q3)


#touple as a parameter and tuple as a return type
names=("tavish","ankit","amit","aman","harshita")


def addElementToTouple(nmT):
    nmT=list(nmT)
    nmT.append("tavish")
    nnmt=tuple(nmT)
    return nmT

q4=addElementToTouple(names)
print(q4)


# set as a parameter and set as a return type
seta={11,22,33,44,55}
def addSetCValue(setToAdd):
    setToAdd.add(34)
    return setToAdd
q5=addSetCValue(seta)
print(seta)


