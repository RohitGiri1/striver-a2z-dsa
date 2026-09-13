"""
Problem - Pattern 19
Link : https://takeuforward.org/plus/dsa/problems/pattern-19
Time Complexity : O(n^2)
SpaceComplexity : O(1)
"""

def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")

        for j in range(i):
           print(" ",end="")

        for k in range(i):
           print(" ",end="")

        for l in range(n-i):
           print("*",end="")
        print()

    for x in range(n):
        for y in range(x+1):
            print("*",end="")
        for z in range(n-x-1):
            print(" ",end="")
        for a in range(n-x-1):
            print(" ",end="")
        for b in range(x+1):
            print("*",end="")
        print()

# Test
pattern(5)

# Output

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********