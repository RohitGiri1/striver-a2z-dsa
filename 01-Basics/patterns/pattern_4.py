"""
Problem : Pattern 4 - Repeated Number Triangle
Link : https://takeuforward.org/plus/dsa/problems/pattern-4
Time Complexity : O(n^2)
Space Complexity : O(1)
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end="")
        print()

# Test
pattern(5)

# Output
# 1
# 22
# 333
# 4444
# 55555


