# Given A as a non-empty array of n integers, we define A as a "permutation" if
# A contains a sequence of n integers from 1 to n once, and only once.
# Example, given A as:
#   A[0] = 4
#   A[1] = 1
#   A[2] = 3
#   A[3] = 2
# A is a permutation. However, if A is given as:
#   A[0] = 4
#   A[1] = 1
#   A[2] = 3
# ...then A is not a permutation, because value 2 is missing.
#
# Write a function:
#
#   def solution(A)
#
# ...that, given an array A, returns 1 if A is a permutation and 0 otherwise.
#
# Write an efficient algorithm for the following assumptions:
# - n is an integer within the range [1..100,000];
# - each element of array A is an integer within the range [1..1,000,000,000].

def solution(A):
  len_a = len(A)
  sum_a = sum(A)

  s = (len_a * (len_a + 1)) // 2

  if sum_a == s:
    return 1

  return 0


A = [4, 1, 3, 2]
print(solution(A))

