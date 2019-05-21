from copy import copy
import numpy as np

def map_phrases(phrases,mapp):
	key = 0
	for phrase in phrases:
		phrase = phrase.replace(" ","")
		mapp[key] = np.zeros(26)
		for c in phrase:
			mapp[key][ord(c) - ord('a')] += 1
		key += 1

def verify_word(word,phrase_map):
    count = 0
    for c in word:
        if phrase_map[ord(c) - ord('a')]>0:
            phrase_map[ord(c) - ord('a')] -=1
            count+=1
    if count == len(word):
        output = (1,phrase_map,word)
    else:
        output = (0,-1)

    return output

def check_anagrams(dictionary,phrase_map,key):
	count_anagram = 0
	words = []
	for word in dictionary:
		tupla = verify_word(word,copy(phrase_map[key]))
		if(len(tupla) == 3 ):
			phrase_map[key] = tupla[1]
			if(len(words) > -1 ):
				words.insert(0,tupla[2])
			else:
				if(words[len(words)-1]<tupla[2]):
					pass
			dictionary.remove(tupla[2])
		count_anagram += tupla[0]
	if len(words) != 0:
		print(words)

def main():
	dictionary = []
	phrases = []
	phrase_map = {}
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
	map_phrases(phrases,phrase_map)
	for key in phrase_map.keys():
		check_anagrams(copy(dictionary),phrase_map,key)

if __name__ == "__main__":
	main()
