# transpose a matrix using a nested loop

x = [[12,3],
     [6,5],
     [12,16]]

result = [[0,0,0],
          [0,0,0]]

import numpy as np
c = np.transpose(x)
print(c)

# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[j][i] = x[i][j]
# for r in result:       
#     print(r)    

