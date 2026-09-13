"""
Problem - Pattern 16 :
Link : https://takeuforward.org/plus/dsa/problems/pattern-16
Time Complexity : O(n^2)
SpaceComplexity : O(1)
"""
def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i),end="")
        print()

# Test
pattern(5)

# Output
# A
# BB
# CCC
# DDDD
# EEEEE
