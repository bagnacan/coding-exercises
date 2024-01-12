# Given an array A consisting of n integers, return the reversed array without
# relying on Python's reverse function.

A = [1, 2, 3, 4, 5, 6, 7]
print(f'Array before reversal: {A}')

n = len(A)

for i in range(n // 2):
    x = A[i]
    rev_index = n - i - 1
    A[i] = A[rev_index]
    A[rev_index] = x

print(f'Array after reversal:  {A}')
