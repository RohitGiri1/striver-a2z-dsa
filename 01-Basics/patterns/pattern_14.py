
'''
Problem - Pattern 14 : Alphabet Pyramid
Link :
Time Complexity : O(n^2)
SpaceComplexity : O(1)
'''

def pattern(n):
    for i in range(n+1):
        for j in range(i):
            print(chr(65+j),end = "")
        print()

#Test
pattern(5)

#Output
# A
# AB
# ABC
# ABCD
# ABCDE
