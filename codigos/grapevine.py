import numpy as np


matriXes = []

ranges = []
'''
def binary_search_b(vec,size,lb,rb):
	left = 0 
	right = size - 1

	while left<=right:
		middle = (left+right)/2

		if middle == 0 and vec[middle] >= lb and vec[middle] <= rb:
			return middle
		elif middle == 0:
			left = 1

		if vec[middle]>= lb and vec[middle-1]<lb and vec[middle]<=rb:
			return middle

		if vec[middle] >= lb:
			right = middle-1
		else:
			left = middle+1

	return -1
'''	
def constroySquare(mini,maxi,matrix):

	maxSize = 0

	N = matrix.shape[0]
	M = matrix.shape[1]
	#print("{0} {1}".format(N,M))
	for i in range(0,N):

		mini_pos = np.where(matrix[i] >= mini)
		if(len(mini_pos[0]) == 0):
			continue
		else:
			mini_pos = mini_pos[0][0]

		for j in range(maxSize,N):

			if (i+j >= N) or  (mini_pos + j >= M) or (matrix[i+j][mini_pos+j]>maxi):
				break
			if(j+1 > maxSize):
				maxSize = j+1

		
	print(maxSize)


def getSquares():

	global matriXes
	global ranges

	i=0
	for rang in ranges:
		for key in rang.keys():
			constroySquare(rang[key][0],rang[key][1],matriXes[i])
		print("-")	
		i += 1

def main():

	global matriXes
	global ranges

	
	while(True):
		
		N, M = map(int, input().split())

		if N == 0 or M == 0:
			break

		matrix = []
		for i in range(0,N):
			matrix.extend(map(int,input().split()))

		matrix = np.asarray(matrix).reshape(N,M)
		matriXes.append(matrix)
		Q = int(input())
		aux = {}
		for i in range(0,Q):
			end, beg = map(int, input().split())
			tupla = (end,beg)
			aux[i] = tupla

		ranges.append(aux)

	getSquares()

print("Sou foda")
		
main()
