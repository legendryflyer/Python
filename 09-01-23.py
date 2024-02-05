seta={11,22,33,44}
seta.pop()
print(seta)

#program 2
setA={11,22,33,44}
setA.update([55,66,77,88])
setA.update((99,100))
setA.update({110,220,330})
print(setA)


#program 3
setC={11,22,33}
setD={44,22,66}
setE=setC.intersection(setD)
print(setE)

#program 4
setC={11,22,33}
setD={44,55,66}
setF=setC.union(setD)
print(setF)

# program 4
setC={11,22,33}
setD={22,33,44}
setC.intersection_update(setD)
print(setC)

# program 5
setC={11,22,33}
setD={22,33,44}
print(setC.difference(setD))
print(setD.difference(setC))

# program 6
setC = {11,22,33}
setD = {22,33,44}
setC.difference_update(setD)
print(setC)
setC = {11,22,33}
setD = {22,33,44}


# program 7
setC={11,22,33}
setD={22,33,44}
setJ=setC.symmetric_difference(setD)
print(setJ)

# program 8
setC={11,22}
setD={11,22,33,44}
print(setC.issubset(setD))
print(setD.issuperset(setC))

# program 9
setC={112,222}
setD={11,22,33,44}

print(setC.isdisjoint(setD))

# program 10
setC = {112,222}
setD = {11,22,33,44}

setC.remove(112)
print(setC)

print(setC.discard(112))
setCities = {"pune","mumbai","banglore","kolkata"}
print(setCities)
for item in setCities:
    print(item)