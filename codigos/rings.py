
#import heapq
import numpy as np
'''
def countGroups(heap):

	heapq.heapify(heap)
	count = 0
	group = []
	auxList = []
	i = 0
	while heap:		
		item = heappop(heap)
		if auxList == []:
			auxList.append(item)
		else:
			if(auxList[len(auxList)-1]<=item):
				group.append(auxList)
'''

def main():

	N = int(input())
	counter = np.zeros(21)

	for i in range(0,N):
		number = (int(input()))
		counter[number-10]+=1

	number = np.amax(counter)

	print(number)


main()