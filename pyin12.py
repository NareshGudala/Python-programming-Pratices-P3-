# python program to remove punctuation from a string
# eg: this is pen

punctuation = "!@#$%^&*(),."
mystr = input("Enter a string:")

new_str=""
for c  in mystr:
    if c not in punctuation:    
        new_str+=c
print(new_str)        
    

