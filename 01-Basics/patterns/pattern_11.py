"""
Problem 11 - Binary Triangle Pattern
Link : https://takeuforward.org/plus/dsa/problems/pattern-11
Time Complexity : O(n^2)
Space Complexity : O(1)
"""

def pattern(n):
    token = 1;
    for i in range(1,n+1):
        token = i%2
        for j in range(i):
            print(int(token),end="")
            token = not token
        print()

# Test
pattern(5)


# Output

# 1          
# 01        
# 101      
# 0101      
# 10101     