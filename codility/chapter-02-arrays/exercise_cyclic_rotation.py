# Given an array A of n integers, a rotation of A is defined as a shift of each
# element to the right by one index (with the last element moved to the first
# place). Example, the rotation of A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7].
#
# Write a function:
#  def solution(A, k)
#
# ...that, given an array A of n integers and an integer k, returns the array A
# rotated k times, i.e., each element of A is shifted k times to the right.
# Examples:
# - with A = [3, 8, 9, 7, 6], k = 3
#     the function returns [9, 7, 6, 3, 8].
# - with A = [0, 0, 0], k = 1
#     the function returns [0, 0, 0]
# - with A = [1, 2, 3, 4], k = 4
#     the function returns [1, 2, 3, 4]
#
# Assume that:
# - n and k are integers within the range [0..100]
# - each element of array A is an integer within the range [−1,000..1,000]

def solution(A, k):

    n = len(A)

    if k >= n:  # avoid performing complete rotations
        k %= n

    while k > 0:

        tail = A[n-1]

        for i in range(n-1, 0, -1):
            A[i] = A[i-1]
        A[0] = tail

        k -= 1

    return A


A = [3, 8, 9, 7, 6]
k = 3
print(f'A: {A} before {k} rotation(s)')

cyclic_rotation = solution(A, k)

print(f'A: {cyclic_rotation} after {k} rotation(s)')

