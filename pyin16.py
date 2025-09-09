# python program to access index of a list using for loop
# Start the indexing with non zero value

my_list = [21,33,15,29]

for index,val in enumerate(my_list,start=1):
    print(index,val)

'''
>>output/Runtime Test cases:

1 21
2 33
3 15 
4 29

'''

