"""
Problem - Pattern 17 : Palindromic Alphabet Pyramid
Link : https://takeuforward.org/plus/dsa/problems/pattern-17
Time Complexity : O(n^2)
SpaceComplexity : O(1)
"""

def pattern(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        for j in list(range(i)) + list(range(i-2,-1,-1)):
            print(chr(65+j),end="")
        print()

# Task
pattern(5)

# Output
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA
