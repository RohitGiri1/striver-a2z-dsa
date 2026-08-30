"""
Problem: Pattern 1 - Square Pattern
Link: https://takeuforward.org/plus/dsa/problems/pattern-1
Time Complexity: O(n^2)  -> outer loop n times, inner loop n times
Space Complexity: O(1)   -> No extra space is used
"""

def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()


# Test
pattern1(5)

# Output:
# *****
# *****
# *****
# *****
# *****