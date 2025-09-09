# python to add two matrices using nested loop

x = [[12,2,3],
     [14,7,9],
     [1,23,16]]

y = [[5,9,7,],
     [11,9,7],
     [3,9,8]]

result = [[0,0,0],
          [0,0,0,],
          [0,0,0,]]

# print(len(x))

# print(len(y))

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j]+y[i][j]
        # print(result[i][j])

for r in result:
    print(r)



