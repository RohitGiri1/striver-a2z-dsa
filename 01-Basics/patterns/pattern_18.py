"""
Problem - Pattern 18 : reverse alphabet triangle pattern
Link : https://takeuforward.org/plus/dsa/problems/pattern-18
Time Complexity : O(n^2)
SpaceComplexity : O(1)
"""
def pattern(n):
    for i in range(n-1,-1,-1):
        for j in range(i,n):
          print(chr(65+j),end = "")
        print()
#Task
pattern(5)
#Output
# E                 69                      4    4
# D E               68 69                   3    3  4
# C D E       -->   67 68 69        -->     2    2  3 4
# B C D E           66 67 68 69             1    1  2 3 4
# A B C D E         65 66 67 68 69          0    0  1 2 3 4
