list_a=[1,2,3]
list_b=[1,2,3]
while list_a and list_b:
    a=int(input())
    b=int(input())


    if(a>b):
        print("a wins the round")
        list_b.remove(b)
        print(list_a)
        print(list_b)
        continue
    elif(a<b):
        print("b wins the round")
        list_a.remove(a)
        print(list_a)
        print(list_b)
        continue



    elif(a==b):
        list_a.remove(a)
        list_b.remove(b)
        print(list_a)
        print(list_b)
        continue


print(f"List A: {list_a}")
print(f"List B: {list_b}")
print("\n")
if not list_a:
    print("Game over! B wins.")
else:
    print("Game over! A wins.")



