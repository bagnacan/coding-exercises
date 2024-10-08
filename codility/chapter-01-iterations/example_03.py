# Print a symmetric triangle made of space-separated asterisks. The triangle
# consists of n rows, where n is a given positive integer, and consecutive rows
# contain 1, 2, ..., n*2 - 1 space-separated asterisks. Example, for n = 4, the
# triangle appears as:
#       *
#     * * *
#   * * * * *
# * * * * * * *

for i in range(1, n+1, 1):
    for t in range((2*n) - (i*2)):
        print(" ", end="")
    for a in range(i + (1*(i-1))):
        print("* ", end="")
    print("")
    

# OUT:       * 
# OUT:     * * * 
# OUT:   * * * * * 
# OUT: * * * * * * * 
### 
