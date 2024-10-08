# The ﬁrst two numbers in the Fibonacci sequence are 0 and 1, with each
# subsequent number being the sum of the previous two. Example, fib(5) = 0, 1,
# 1, 2, 3.
# Write a program that prints all the Fibonacci numbers, not exceeding a given
# integer n.

n = 10
a = 0
b = 1
while a <= n:
    print(a)
    c = a + b
    a = b
    b = c
    

# OUT: 0
# OUT: 1
# OUT: 1
# OUT: 2
# OUT: 3
# OUT: 5
# OUT: 8
### 
