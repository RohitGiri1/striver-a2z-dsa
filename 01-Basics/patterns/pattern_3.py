"""
Problem : Pattern 3 - Half Pyramid with Numbers
Link : https://takeuforward.org/plus/dsa/problems/pattern-3
Time Complexity : O(n^2)
Space Complexity : O(1)
"""

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()

#Test
pattern(4)

#Output
# 1
# 12
# 123
# 1234