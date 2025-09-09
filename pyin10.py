# python program to computer all the permutation of the string.
# run unr rnu nur


def get_permutation(string,i=0):   # ('run',0)
    if i==len(string):  # 3==3  #['r','u','n']
        print("".join(string))   
    for j in range(i,len(string)):  #0,3
        words=[c for c in string]   #['r','u','n']
        # print(words)  

        words[i],words[j]=words[j],words[i]  
        get_permutation(words,i+1)
get_permutation('run')        


