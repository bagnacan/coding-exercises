def count_values(A, m):
  n = len(A)
  count = [0 for i in range(m+1)]
  for i in range(n):
    count[A[i]] += 1

  return count


def can_swap_values(A, B, m):
  n = len(A)  # assuming A and B share the same lenth
  sum_a = sum(A)
  sum_b = sum(B)
  count_a = count_values(A, m)

  d = abs(sum_a - sum_b)

  if d % 2 == 1:
    return False

  d //= 2

  for i in range(n):
    if count_a[abs(B[i] - d)] > 0:
      return True

A = [4, 20, 4, 2, 18, 0]  # sum is 48
B = [20, 0, 2, 22, 0, 0]  # sum is 44
m = max(max(A, B))
print(can_swap_values(A, B, 22))

