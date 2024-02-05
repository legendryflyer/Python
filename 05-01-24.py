#program 1
setA={11,22,33,44}
setA.pop()
print(setA)

# program 2
setA={11,22,33,44}
setA.update([55,66,77])
print(setA)

#program 3
setc = {11,22,33}
setd = {22,33,44}
sete = setc.intersection(setd)
print(sete)
setf = setc.union(setd)
print(setf)
setg=setc.intersection_update(setd)
print(setg)
setC = {11,22,33}
setD = {22,33,44}
setJ = setC.symmetric_difference(setD)
print(setJ)

setC.symmetric_difference_update(setD)
print(setC)

setC = {11,22}
setD = {11,22,33,44}
print(setC.issubset(setD))
print(setD.issuperset(setC))


setC = {112,222}
setD = {11,22,33,44}
print(setC.isdisjoint(setD))


setC = {112,222}
setD = {11,22,33,44}

setC.remove(112)
print(setC)

print(setC.discard(112))
setCities = {"pune","mumbai","banglore","kolkata"}
print(setCities)
for item in setCities:
     print(item)