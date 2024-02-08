# number of lines , number of characters , number of words
import os, sys
fname = input("enter the file name: ")
if os.path.isfile(fname):
    f = open(fname,"+a")
else:
    print("file not found. ")
    sys.exit()
f.seek(0,0)
cl = 0
cw = 0
cc = 0

for line in f:
    words = line.split(" ")
    cl = cl + 1
    cw = cw + len(words)
    cc = cc +len(line)
print(cl)
print(cw)
print(cc)
f.close()