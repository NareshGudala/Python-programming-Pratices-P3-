# ======== PRINTING PATTERNS ============
# Print Square Pattern

# print("Square Pattern:")
# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()    

# # Print Triangle Pattern

# print("Triangle Pattern")
# for i in range(5):
#     for j in range(i+1):
#         print("#",end=" ")
#     print()    


# # Print reverse triangle pattern

# print("Reverse triangle Pattern")
# for i in range(5):
#     for j in range(5-i):
#         print("*",end=" ")
#     print()    


import sys

def pattern(i, a):
    for j in range(i, a):
        sys.stdout.write(" ")
    for j in range(1, i + 1):
        if i == j or j == 1 or (i >= 5 and (j == 3 or j == i - 2)) or (i >= 9 and (j == 5 or j == i - 4)):
            sys.stdout.write("**")
        else:
            sys.stdout.write("  ")
    sys.stdout.write("\n")

a = int(input( ))
for i in range(1, a + 1):
    pattern(i, a)
for i in range(a - 1, 0, -1):
    pattern(i, a)
