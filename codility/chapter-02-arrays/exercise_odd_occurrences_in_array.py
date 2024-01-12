# A non-empty array A contains an odd number n of integers.
# Each element in the array can be paired with another element that has the
# same value. Since the array has an odd number of elements, one element is
# left unpaired. Example:
# with A[0] = 9; A[1] = 3; A[2] = 9; A[3] = 3; A[4] = 9; A[5] = 7; A[6] = 9
# ...follows that:
# - the elements at indexes 0 and 2 have value 9
# - the elements at indexes 1 and 3 have value 3
# - the elements at indexes 4 and 6 have value 9
# - the element at index 5 has value 7 and is unpaired
#
# Write a function:
#   def solution(A)
#
# ...that, given an array A with an odd number n of integers fulfilling the
# above conditions, returns the value of the unpaired element.
#
# Example: A = [9, 3, 9, 3, 9, 7, 9]
#   the function returns 7
#
# Assume that:
# - n is an odd integer within the range [1..1,000,000]
# - each element of array A is an integer within the range [1..1,000,000,000]
# - all but one of the values in A occur an even number of times

def solution(A):
    if n > 1:
        s = set()

        for i in range(n):
            k = A[i]

            if k not in s:  # track a new element
                s.add(k)
            else:  # or remove it since the new element pairs the old element
                s.remove(k)

        # pop an arbitrary element, i.e., the only element we are looking for :)
        return s.pop()

    else:
        return A[0]

A = [9, 3, 9, 3, 9, 7, 9]
n = len(A)
print(solution(A))

