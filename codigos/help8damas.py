import numpy as np


table = np.zeros(64).reshape(8,8)


table[0][0] = 1
table[1][2] = 1
table[2][1] = 1
table[3][5] = 1
table[6][0] = 1
table[2][3] = 1
print(table)