# python program to check if a string is palindrome or not
# eg :
# input : MOM   => output : MOM
# input : MADAM   => output : MADAM

def ispalindrome(s): # Function defination and palindrome
    return s==s[::-1]
s = "mom"            # string
ans=ispalindrome(s)  # Function call 
if ans:
    print("This is palindrome")
else:
    print("Not a palindrome")


