"""
Problem 9 - Diamond
Link : https://takeuforward.org/plus/dsa/problems/pattern-9
Time Complexity : O(n^2)
Space Complexity : O(1)
"""
def pattern(n):
    for i in range(n):
        for j in range(n-1-i):
            print(" ",end="")
        for k in range(i*2+1):
            print("*",end="")
        print()
    for i in range(n):
        for j in range (i):
            print(" ",end="")
        for k in range((n-i)*2-1):
            print("*",end = "")
        print()
        
# Test
pattern(4)

# Output
#    *
#   **
#  *****
# *******
# *******
#  *****
#   ***
#    *