# A binary gap within a positive integer n is any maximal sequence of
# consecutive zeros that is surrounded by ones at both ends in the binary
# representation of n.
# Examples:
# - 9 has binary representation 1001 and contains a binary gap of length 2
# - 529 has binary representation 1000010001 and contains two binary gaps, one
#   of length 4 and one of length 3
# - 20 has binary representation 10100 and contains one binary gap of length 1
# - 15 has binary representation 1111 and has no binary gaps
# - 32 has binary representation 100000 and has no binary gaps
#
# Write a function:
#   def solution(n)
# ...that, given a positive integer n, returns the length of its longest binary
# gap. The function should return 0 if n doesn't contain a binary gap.
# Examples:
# - for n = 1041, the function returns 5, because n has binary representation
#   10000010001 and its longest binary gap is of length 5
# - for n = 32, the function returns 0, because n has binary representation
#   100000 and thus no binary gaps
#
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..2,147,483,647]

def solution(n):
    bin_gap = 0
    bin_rep = f'{n:b}'

    if len(bin_rep) < 3:
        return bin_gap

    else:
        # bin_rep always starts with 1, so we can always assume that a window
        # starts at index position zero, and evaluate the successive numbers
        idx_open = 0

        for i in range(1, len(bin_rep)):

            print(f'window opens at {idx_open} and closes at {i}')
            print(f'bin repr at idx_open : {int(bin_rep[idx_open])}')
            print(f'bin repr at idx_close: {int(bin_rep[i])}')

            if int(bin_rep[idx_open]) + int(bin_rep[i]) == 2:

                print('\tdecimal sum is = 2')

                # check distance between the indexes of starting and ending 1s
                distance = i - idx_open

                print(f'\tdistance between indices is {distance}')

                if distance == 1:  # consecutive 1s ==> move window forward
                    idx_open = i
                    print(f'\t\tdistance is 1 ==> move window forward')
                else:  # non-consecutive 1s ==> check if bin_gap is smaller
                    print(f'\t\tdistance is > 1')
                    gap = distance - 1  # remove trailing 1
                    if bin_gap < gap:
                        print(f'\t\tassign gap = {gap}')
                        bin_gap = gap
                        idx_open = i  # move window forward

            else:
                print('\tdecimal sum is still 1')

    return bin_gap


# n = 1   # binary representation:    1
# n = 2   # binary representation:   10
# n = 3   # binary representation:   11
# n = 4   # binary representation:  100
# n = 5   # binary representation:  101
# n = 25  # binary representation: 1101
n = 49  # binary representation: 110001
# n = 529  # binary representation: 1000010001

gap = solution(n)

print(gap)

