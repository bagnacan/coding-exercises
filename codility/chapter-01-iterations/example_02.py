# Print a triangle made of space-separated asterisks. The triangle consists of n
# rows, where n is a given positive integer, and consecutive rows contain 1, 2,
# ..., n space-separated asterisks. Example, for n = 4, the triangle appears as:
# *
# * *
# * * *
# * * * *

for i in range(1, n+1):  # Python3's range is Python2's xrange, which returns
    for j in range(i):   # values on-the-fly instead of building a list first
        print("* ", end="")
    print("")
    

# OUT: * 
# OUT: * * 
# OUT: * * * 
# OUT: * * * * 
### 
