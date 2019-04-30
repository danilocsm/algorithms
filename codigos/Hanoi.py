

def hanoi(n,start,to,other):

	if n<1:
		return
	else:
		hanoi(n-1,start,other,to)
		print("Move {0} from {1} to {2}".format(n,start,to))
		hanoi(n-1,other,to,start)

def main():

	n = int(input("Número de discos: "))

	hanoi(n,1,3,2)

main()