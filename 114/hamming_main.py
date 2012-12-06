from hamming_distance import hamming_distance
import sys

file = open('./words.txt', 'r')
list = file.readlines()
file.close()
testword = sys.argv[1]

for word in list:
	word = str.rstrip(word)
	if(len(word) == len(testword)):
		if(hamming_distance(testword, word) == 1):
			 print word + '\n'
