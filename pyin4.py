# check if the first and last number of a list the same
number_x = [10,20,30,40,10]
def first_last(numbers_x):
    first=numbers_x[0]
    second=numbers_x[-1]
    # print(first,second)
    if first==second:
         return True
    else:
        return False
print(first_last(number_x))  