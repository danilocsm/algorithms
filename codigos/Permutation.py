def itPermutation(vector, boolVec, index):

	if index>=(len(vector)):

			print(vector)
	else:

		for i in range(1,len(vector)+1):
			
			vector[index]=i
			if boolVec[i]:
				continue
			boolVec[i]=True
			itPermutation(vector,boolVec,index+1)
			boolVec[i]=False

def permutation(vector, boolVec):

	print("Permutando")
	itPermutation(vector,boolVec,0)

def main():

	n = int(input("Digite o número para n!: "))

	vector = np.empty(n)

	boolVec = [False]*(n+1)

	permutation(vector,boolVec)

main()