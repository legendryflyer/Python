#l=int(input())
#r=int(input())
#k=int(input())
#count=0
#for number in range(l,r+1):
#	if number % k == 0:
#		count=count+1
#print(count)




#A=[85,25,65,21,84]
#last_digits = [num % 10 for num in A]
#n=int(''.join(map(str, last_digits)))
#if n % 10 == 0:
#    print("Yes")
#else:
#    print("No")



#A=[]
#N=int(input())
#i=0
#while i<N:
#   a=A.append(int(input()))
#    i=i+1
#last_digits = [num % 10 for num in A]
#n=int(''.join(map(str, last_digits)))
#if n % 10 == 0:
#    print("Yes")
#else:
#    print("No")




def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_prime_triplets(arr):
    n = len(arr)
    count = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                product = arr[i] * arr[j] * arr[k]
                if is_prime(product):
                    count += 1

    return count

# Example usage:
N = int(input("Enter the size of the array: "))
A = [int(input(f"Enter element {i + 1}: ")) for i in range(N)]

result = count_prime_triplets(A)
print(f"The number of triplets such that Ai * Aj * Ak is a prime number is: {result}")
