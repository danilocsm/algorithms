import math as m
import numpy as np

def isJolly(array):

	auxArray = np.zeros(array[0]-1)

	for i in range(1,len(array)-1):
		diff = int(m.fabs(array[i]-array[i+1]))
		try:
			auxArray[diff-1]+=1
		except IndexError:
			pass

	jolly = True

	for i in range(0,len(auxArray)):

		if auxArray[i]!=1:
			jolly = False
			break

	if jolly:
		print("Jolly")
	else:
		print("Not Jolly")


def main():
	while True:
		try:
			entry = input()
		except EOFError:
			break

		aux = entry.split(" ")
		aux = [int(i) for i in aux]

		isJolly(aux)

main()
