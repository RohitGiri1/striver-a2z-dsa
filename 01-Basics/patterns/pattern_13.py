"""
Problem 13 - Floyd's Triangle
Link : https://takeuforward.org/plus/dsa/problems/pattern-13
Time Complexity : O(n^2)
Space Complexity : O(1)
"""

def pattern(n):
    count = 1
    for i in range(n):
        for j in range(i+1):
            print(count,end="")
            count+=1
        print()
# Test
pattern(5)

# Output
# 1
# 23
# 456
# 78910
# 1112131415
