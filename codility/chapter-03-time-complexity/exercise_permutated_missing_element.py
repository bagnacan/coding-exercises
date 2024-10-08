# An array A consists of n different integers in the range 1, ..., (n + 1)],
# i.e., exactly one element is missing.
# Write a function:
#   def solution(A)
#
# ...that, given the array A, returns the value of the missing element
#
# Example, given A = [2, 3, 1, 5]
# ...the function returns 4, as it is the missing element.
#
# Write an efficient algorithm for the following assumptions:
# - n is an integer within the range [0..100,000]
# - the elements of A are all distinct
# - each element of array A is an integer within the range [1..(n + 1)]

def solution(A):
    summa = sum(A)
    sigma = (len(A) + 1) * ((len(A) + 1) + 1) // 2

    return sigma - summa

A = [2, 3, 1, 4, 5]
print(solution(A))

