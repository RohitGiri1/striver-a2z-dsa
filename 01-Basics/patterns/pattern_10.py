"""
Problem 10 - Diamond
Link : https://takeuforward.org/plus/dsa/problems/pattern-10
Time Complexity : O(n^2)
Space Complexity : O(1)
"""

def pattern(n):
    for i in list(range(n)) + list(range(n-1,-1)):
        for j in range(i+1):
            print("*",end="")
        print()
    for k in range(n-1):
        for l in range(n-k-1):
            print("*",end="")
        print()

# Test
pattern(5)

# Output
# *          
# **         
# ***       
# ****       
# *****      
# ****       
# ***        
# **         
# *          
