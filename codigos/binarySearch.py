
import numpy as np
import math as m
import random

def binarySearch(arr,val):
	
	beg = 0
	end = len(arr)-1
	meio = m.floor(end+beg/2)
	while(meio>=beg and meio<=end):
			
		if val>arr[meio]:
			beg = meio + 1
			meio = m.floor((beg+end)/2)
		elif val<arr[meio]:
			end = meio - 1 
			meio = m.floor((beg+end)/2)
		else:
			return arr[meio]

	return -1

def InsertionSort(vet):

	print(len(vet))
	for i in range(1,len(vet)):
		key = vet[i]
		j = i-1
		while (j>=0) and (vet[j]>key):
			vet[j+1] = vet[j]
			j -= 1

		vet[j+1] = key

	return vet		

arr = np.arange(1000)
random.shuffle(arr)
print(arr)
arr = InsertionSort(arr)
print(arr)
print(binarySearch(arr,34))
