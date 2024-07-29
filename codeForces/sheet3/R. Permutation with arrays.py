def isPermutation(A,B):
    if(len(A)!=len(B)):
        return False
    A = sorted(A)
    print(A)
    B = sorted(B)
    print(B)
    if A != B:
        return False
    return True


N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
isPermutation(A,B)
print(isPermutation(A,B))

from collections import Counter

def are_permutations_counter(A, B):
    return Counter(A) == Counter(B)

# Read input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Check and print result
if are_permutations_counter(A, B):
    print("yes")
else:
    print("no")
