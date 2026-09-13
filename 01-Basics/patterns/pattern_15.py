
'''
Problem - Pattern 15 : Inverted Alphabet Pyramid
Link :
Time Complexity : O(n^2)
SpaceComplexity : O(1)
'''
def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(65+j),end = "")
        print()
        
# Test
pattern(5)

# Output

# ABCDE
# ABCD
# ABC
# AB
# A
