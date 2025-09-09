# Accept a hyphen-separated sequence of words as input and
# prints the sorted words

'''

put : green-red-black-white
tput : black-green-red-white

'''

items = [n for n in input("Enter the string:").split("-")]
items.sort()
print("-".join(items))