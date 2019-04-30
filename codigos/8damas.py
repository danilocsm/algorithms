from array import array

count = 0
diagonal = False

def damePermutation(vector, boolVec, index):

	global diagonal
	global count
	if index>=(len(vector)):
			count += 1
			print("{0} ".format(count),end="")
			print(vector)
	else:

		for i in range(1,len(vector)+1):
			diagonal = False
			vector[index]=i
			if boolVec[i]:
				continue

			for k in range(0,index):
				if( (i == vector[k] + (k - index) ) or (i == vector[k] - (k - index)) ):
					diagonal = True
					break

			if diagonal:
				continue

			boolVec[i]=True
			damePermutation(vector,boolVec,index+1)
			boolVec[i]=False

def main():


	vector = [-1]*8
	vector = array('l',vector)
	boolVec = [False]*(8+1)
	print("hello")
	damePermutation(vector,boolVec,0)

main()
