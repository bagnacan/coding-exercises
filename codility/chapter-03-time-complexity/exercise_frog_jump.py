

# A frog, currently located at position X, wants to jump to a position that is
# greater than or equal to Y. The frog always jumps a fixed distance D.
# Count the minimal number of jumps that the frog must take to reach the target.
#
# Write a function:
#   def solution(X, Y, D)
#
# ...that, given the three integers X, Y and D, returns the minimal number of
# jumps from position X to a position equal to or greater than Y
#
# Example, given:
# - X = 10
# - Y = 85
# - D = 30
# the function returns 3, because the frog will be positioned as follows:
# - after the first jump, at position 10 + 30 = 40
# - after the second jump, at position 10 + 30 + 30 = 70
# - after the third jump, at position 10 + 30 + 30 + 30 = 100
#
# Write an efficient algorithm for the following assumptions:
# - X, Y and D are integers within the range [1..1,000,000,000]
# - X ≤ Y


def solution(X, Y, D):
    offset = Y - X

    d = offset // D

    if (offset % D) > 0:
        d += 1

    return d


X = 10
Y = 85
D = 30

print(solution(X, Y, D))

