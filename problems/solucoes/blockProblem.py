
import numpy as np

blockWorld = {}

blockLocation = []

def initializeBlockWorld(n):

	global blockWorld
	global blockLocation

	blockLocation = [i for i in range(0,n)]
	blockLocation = np.asarray(blockLocation)

	keys = [i for i in range(0,n)]
	values = [[] for i in range(0,n)]
	blockWorld = dict(zip(keys,values))

	i=0
	for key in blockWorld.keys():
		blockWorld[key].append(i)
		i+=1


def find(B):

	global blockLocation

	return blockLocation[B]

def updatePos(bA,posB):

	global blockLocation

	blockLocation[bA] = posB

def detect(pos,B):

	global blockWorld

	aux = blockWorld[pos]
	last = len(aux)-1

	if aux.index(B) != last:
		return True
	else:
		return False

def returnToPos(pos,B):

	global blockWorld

	locate = blockWorld[pos].index(B)
	aux = blockWorld[pos][locate:]
	try:
		for i in range(1,len(aux)):
			move(aux[i],pos,aux[i])
			updatePos(aux[i],aux[i])
	except IndexError:
		pass
	#del aux


def move(bA,posA,posB):

	global blockWorld

	blockWorld[posA].remove(bA)
	blockWorld[posB].append(bA)


def pile(posA,bA,posB):

	global blockWorld

	locate = blockWorld[posA].index(bA)
	aux = blockWorld[posA]
	blockWorld[posB].extend(aux[locate:])

	for i in blockWorld[posB]:
		updatePos(i,posB)

	del	blockWorld[posA][locate:]

def doAction(bA,bB,act):

	global blockLocation
	posA=find(bA)
	posB=find(bB)

	if posA==posB or bA==bB:
		return "Illegal Command\n"

	if act == 'moveonto':
		if detect(posA,bA) or detect(posB,bB):
			returnToPos(posA,bA)
			returnToPos(posB,bB)
		move(bA,posA,posB)
		updatePos(bA,posB)
	elif act == 'moveover':
		if detect(posA,bA):
			returnToPos(posA,bA)
		move(bA,posA,posB)
		updatePos(bA,posB)
	elif act == 'pileonto':
		if detect(posB,bB):
			returnToPos(posB,bB)
		pile(posA,bA,posB)
		updatePos(bA,posB)
	elif act == 'pileover':
		pile(posA,bA,posB)
		updatePos(bA,posB)

	#showWorld()
	#print(blockLocation)

def showWorld():

	global blockWorld
	for key,values in blockWorld.items():
		print("{0}: ".format(key),end="")
		for value in values:
			print(value,end=" ")
		print("")

def main():

	global blockWorld
	command = ""

	n = int(input())

	initializeBlockWorld(n)

	while command != "quit":

		command = input()
		aux = command.split(" ")

		if command == "quit":
			continue

		blockA,blockB,action = int(aux[1]),int(aux[3]),aux[0]+aux[2]
		doAction(blockA,blockB,action)

	showWorld()


main()
