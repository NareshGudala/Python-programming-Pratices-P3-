# check if the number is an Armstrong number or not
# without using power function
# eg: 153 = 1^3+5^3+3^3

n = int(input("Enter the number:"))
s= n
b=len(str(n))
sum1=0
while n!=0:           # 153
    r=n%10            # 153%10=3
    sum1=sum1+(r**b)  # 3**3=27  5**3=125   1**3=1
    n=n//10

    # 125+27+1 = 153
if s==sum1:
    print("armstrong number")
else:    
    print("Not a armstrong")