

def pattern(n):

    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for k in range(n-i-1):
            print(" ",end="")
        for l in range(n-i-1):
            print(" ",end="")
        for m in range(i+1):
            print("*",end="")
        print()

    for w in range(n-1):
        for x in range(n-w-1):
            print("*",end="")
        for y in range(w+1):
            print(" ",end="")
        for z in range(w+1):
            print(" ",end="")
        for a in range(n-w-1):
            print("*",end = "")
        print()

# Test
pattern(5)

# Output

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *