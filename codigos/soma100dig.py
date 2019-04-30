

def soma(numA,numB):

	numA = numA.lstrip("0")
	numB = numB.lstrip("0")
	
	return int(numA)+int(numB)

def main():

	numA = input("Numero a: ")

	numB = input("Numero b :")

	print("{0}".format(soma(numA,numB)))

if __name__ == "__main__":
	main()