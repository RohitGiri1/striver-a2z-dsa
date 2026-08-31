"""
Problem 7 - pyramid
Link : https://takeuforward.org/plus/dsa/problems/pattern-7
Time Complexity : O(n^2)
Space Complexity : o(1)
"""

def pattern(n):
    for i in range(n):
        for j in range(n-1-i):
            print(" ",end="")
        for k in range(i*2+1):
            print("*",end="")
        print()

# Test
pattern(4)

# Output
#    *
#   ***
#  *****
# *******