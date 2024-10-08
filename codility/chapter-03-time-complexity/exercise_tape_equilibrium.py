# A non-empty array A of n integers represents numbers on a tape.
# Any integer p, such that 0 < p < n, splits the tape in two non-empty parts:
# A[0], A[1], ..., A[p - 1]; A[p], A[p + 1], ..., A[n - 1].
# The difference between the two parts is defined as:
# |(A[0] + A[1] + ... + A[p - 1]) - (A[p] + A[p + 1] + ... + A[n - 1])|
# Example, consider array A = [3, 1, 2, 4, 3] then, we can split the tape in
# four places:
# - p = 1 ==> difference = |3 - 10| = 7
# - p = 2 ==> difference = |4 - 9| = 5
# - p = 3 ==> difference = |6 - 7| = 1
# - p = 4 ==> difference = |10 - 3| = 7
#
# Write a function:
#   def solution(A)
#
# ...that, given a non-empty array A of n integers, returns the minimal
# difference that can be achieved.
# Example, given:
# A[0] = 3
# A[1] = 1
# A[2] = 2
# A[3] = 4
# A[4] = 3
# ...the function returns 1.
#
# Write an efficient algorithm for the following assumptions:
# - N is an integer within the range [2..100,000]
# - each element of array A is an integer within the range [−1,000..1,000]


def solution(A):
    sum_a = sum(A)
    sum_b = 0

    lower_dif = sum_a
    lower_idx = 0
    count = 0

    while len(A) > 0:
        e = A.pop(0)
        count += 1  # count pop operations to infer index

        sum_a -= e
        sum_b += e

        dif = abs(sum_a - sum_b)
        if dif < lower_dif:
            lower_dif = dif
            lower_idx = count

    return lower_idx

A = [3, 1, 2, 4, 3]
print(solution(A))

