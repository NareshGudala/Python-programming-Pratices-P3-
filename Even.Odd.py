# check if the input number is odd and even.
# A number is even if division by 2 gives a remain
# If the remainder is 1, it is an odd number.

num = int(input("Enter the Number:"))
if num%2==0:
    # print("Even number")
    print("{0} is Even".format(num))
else:
    # print("odd number") 
    print("{0} is Odd".format(num))    