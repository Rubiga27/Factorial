def factorial(A):
    if A==0:
        return 1
    else:
        return factorial(A-1)*A
A=int(input())
print(factorial(A))

"""
Input 1:
A = 4

Input 2:
A = 1



Output 1:
24

Output 2:
1
"""

