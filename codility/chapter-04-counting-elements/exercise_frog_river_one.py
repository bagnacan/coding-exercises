# A frog is initially located on one river bank, i.e., position 0, and wants to
# jump to the opposite bank, i.e., position X+1. To do so, the frog relies on
# the leaves that fall from a tree to the surface of the water.
#
# We list the positions of the fallen leaves as integer values of an array A. In
# particular:
# - the value "A[k]" represents the position where one leaf has fallen
# - the index "k" represents the time (seconds) when the leaf has fallen
# - the length "n" of the array A represents the number of seconds so far
#
# Find the earliest time when the frog can jump to the other side of the river.
# That is, the time (in seconds) when each position is covered by a leaf.
# (Assume that the speed of the river's current is negligible and that leaves
# don't move:)
#
# Example: X=5 and A is defined as:
#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# Here, at second k=7 a leaf fell into position A[k]=4. However, there exists
# another moment in time where all positions were already covered by at least
# one leaf. This is true at second k=6 where, for the X=5 positions:
# - position 1 has been covered by a leaf at second(s) 0 and 2
# - position 2 has been covered by a leaf at second(s) 4
# - position 3 has been covered by a leaf at second(s) 1 and 5
# - position 4 has been covered by a leaf at second(s) 3
# - position 5 has been covered by a leaf at second(s) 6
#
# Write a function:
#
#   def solution(X, A)
#
# ...that, given a non-empty array A consisting of n integers and integer X,
# returns the earliest time (seconds) when the frog can jump to the other bank.
# If the frog is never able to jump to the other side of the river, the function
# should return −1.
#
# Write an efficient algorithm for the following assumptions:
# - n and X are integers within the range [1..100,000];
#  each element of A is an integer within the range [1..X].

def solution(X, A):
  count = [0 for i in range(X+1)]
  cover = 0
  n = len(A)

  for j in range(n):
    if count[A[j]] == 0:
      count[A[j]] += 1
      cover +=1

      if cover == X:
        return j

  return -1


X = 5
A = [1, 3, 1, 4, 2, 3, 5, 4]
print(solution(X, A))

