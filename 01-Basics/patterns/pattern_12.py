"""
Problem 12 - Half Butterfly Pattern
Link : https://takeuforward.org/plus/dsa/problems/pattern-12
Time Complexity : O(n^2)
Space Complexity : O(1)
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")

        for k in range(n-i):
            print(" ",end="")

        for k in range(n-i):
            print(" ",end="")

        for k in range(i,0,-1):
            print(k,end="")

        print()

# Test

pattern(5)

# Output

# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321