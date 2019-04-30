from copy import copy
import numpy as np



def mapPhrases(phrases,mapp):

	key = 0

	for phrase in phrases:

		phrase = phrase.replace(" ","")
		mapp[key] = np.zeros(25)
		for c in phrase:
			mapp[key][ord(c) - ord('a')] += 1

		key += 1

def verifyWord(word,phraseMap):

	count = 0


	for c in word:
		if phraseMap[ord(c) - ord('a')]>0:
			phraseMap[ord(c) - ord('a')] -=1
			count+=1

	if count == len(word):
		output = (1,phraseMap,word)
	else:
		output = (0,-1)

    return output

def checkAnagrams(dictionary,phraseMap,key):

	countAnagram = 0
	words = []

	for word in dictionary:

		tupla = verifyWord(word,copy(phraseMap[key]))

		if(len(tupla) == 3 ):

			phraseMap[key] = tupla[1]
			if(len(words) > -1 ):
				words.insert(0,tupla[2])
			else:
				if(words[len(words)-1]<tupla[2]):
					pass

			dictionary.remove(tupla[2])

		countAnagram += tupla[0]

	if len(words) != 0:
		print(words)


def main():

	dictionary = []
	phrases = []
	phraseMap = {}

	count = 0
	while count == 0:

		entry = input()
		if entry == '#':
			count +=1
			break

		dictionary.insert(0,entry)

	while count == 1:
		entry = input()
		if entry == '#':
			count +=2
			break

		phrases.insert(0,entry)

	mapPhrases(phrases,phraseMap)

	for key in phraseMap.keys():
		checkAnagrams(copy(dictionary),phraseMap,key)



if __name__ == "__main__":
	main()
