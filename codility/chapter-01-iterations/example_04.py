# Given a positive number n, count the number of digits in its decimal
# representation. Do not convert the number to a string representation. Use
# instead arithmetical operations. Example: 48.90 produces 2

n = 48.90
result = 0
while n > 0:
    n = n // 10
    result += 1
    

print(result)
# OUT: 2
### 
