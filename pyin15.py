# Write a python function to sum all the numbers in a list.

def sum(num):   # function defination
    total=0     # local variable
    for x in num:
        total+=x # total=total+x
    return total
print(sum([12,19,17,5,10,15]))    

# li = [12,15,14,24,65]
#print(sum(li))