import os, sys
# count no of words, characters, line
filename = input("enter file name: ")
if os.path.isfile(filename):
    f = open(filename,'+a')
else:
    sys.exit()

cc=0
cw=0 
cl=0
f.seek(0,0)
for line in f:
    cl = cl + 1
    words = line.split(" ")
    cw = cw + len(words)
    cc = cc +len(line)  
f.read()
print(f"No of Characters: {cc}")
print(f"No of Words: {cw}")
print(f"No of Lines: {cl}\n")   
f.close()