"""
Problem: Pattern 2 - Right Trianlge Pattern
Link: https://takeuforward.org/plus/dsa/problems/pattern-2

Time Complexity: O(n^2)  -> outer loop n times, inner loop n times
Space Complexity: O(1)   -> No extra space is used
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(0,i):
            print("*",end = "")

        print()

# Test
pattern(5)

# Output:
# *
# **
# ***
# ****
# *****