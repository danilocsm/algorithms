import numpy as np


matrix = []
for i in range(0,16):
	matrix.append(int(input()))

matrix = np.asarray(matrix).reshape(4,4)
print(matrix)


print(matrix[1:3,1:3])

myArr = np.arange(9)
aux = np.where(myArr == 10)
print(len(aux[0]))
aux1 = np.where(matrix>=6)
aux2 = np.where(matrix<=20)
index = []


for i in range(0,len(aux1[0])):
	if(matrix[aux1[0][i]][aux1[1][i]]>20):
		index.append(i)

minimum = (np.delete(aux1[0],index,axis=0),np.delete(aux1[1],index,axis=0))

index.clear()

for i in range(0,len(aux2[0])):
	if(matrix[aux2[0][i]][aux2[1][i]]<6):
		index.append(i)

maximum = (np.delete(aux2[0],index,axis=0),np.delete(aux2[1],index,axis=0))


print(minimum)
print(maximum)
