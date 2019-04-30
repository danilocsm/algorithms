import numpy as np
import math as m



#Código para calcular a distancia entre valores em dois vetores de mesmo tamanho e com o mesmo elementos.

def mapFirstArr(arr):

	output = np.zeros(len(arr))

	for i in range(0,len(arr)):

		pos = arr[i]
		output[pos] = i
	return output


def calculateDistances(arr1,arr2):

	aux = mapFirstArr(arr1)	

	for i in range(0,len(arr2)):

		val = arr2[i]
		pos1 = aux[val]
		dist = m.fabs(pos1 - i)

		print("Distancia de {0} : {1}".format(arr2[i],dist))



def main():

	size = int(input())

	arr1 = np.arange(size)
	arr2 = np.arange(size)

	np.random.shuffle(arr1)
	np.random.shuffle(arr2)

	print(arr1)
	print(arr2)

	calculateDistances(arr1,arr2)


if __name__ == "__main__":
	main()