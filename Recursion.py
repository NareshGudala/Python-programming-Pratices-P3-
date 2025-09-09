# Write a python program of recursion list sum.

def recursion(data_list):
    total=0
    for ele in data_list:
        if type(ele)==type([]):
            total=total+recursion(ele)
        else:
            total=total+ele   # 0+1=1+2=3+3=6+4=10+5=15+6=21
    return total
print(recursion([1,2,[3,4],[5,6]]))            