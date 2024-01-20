# Write a function:
#
#   def solution(A)
#
# ...that, given an array A of n integers, returns the smallest positive integer
# (greater than 0) that does not occur in A.
#
# Examples:
# - given A = [1, 3, 6, 4, 1, 2], the function return 5
# - given A = [1, 2, 3], the function returns 4
# - given A = [1, 2, 4], the function returns 3
# - given A = [3, 4], the function returns 1
# - given A = [−1, −3], the function returns 1
#
# Write an efficient algorithm for the following assumptions:
# - n is an integer within the range [1..100,000]
# - each element of A is an integer within the range [−1,000,000..1,000,000]

def first_missing(A, m):
  n = len(A)
  count = [0 for i in range(m+1)]

  for j in range(n):
    count[A[j]] += 1

  for k in range(1, m+1):
    if count[k] == 0:
      return k

def solution(A):
  m = max(A)

  # case no number in A is >0
  if m < 0:
    return 1

  # case A contains all numbers
  s = sum(A)
  sigma = (m * (m+1)) // 2
  if s == sigma:
    return m + 1

  # case A misses one or more numbers
  return first_missing(A, m)


A = [1, 3, 6, 4, 1, 2]  # 5
# A = [1, 2, 3]  # 4
# A = [1, 2, 4]  # 3
# A = [3, 4]  # 1
# A = [-1, -3]  # 1
print(solution(A))
