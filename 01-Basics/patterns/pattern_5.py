"""
Problem : Pattern 5 - Inverted Right Triangle
Link : https://takeuforward.org/plus/dsa/problems/pattern-5
Time Complexity : O(n^2)
Space Complexity : O(1)
"""

def pattern(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end="")
        print()

# Test
pattern(5)

# Output
# *****
# ****
# ***
# **
# *