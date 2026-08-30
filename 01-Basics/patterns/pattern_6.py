"""
Problem : Pattern 6
Link : https://takeuforward.org/plus/dsa/problems/pattern-6
Time Complexity : O(n^2)
Space Complexity : O(1)
"""

def pattern(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j,end="")
        print()

# Test
pattern(5)

# Output
# 12345
# 1234
# 123
# 12
# 1