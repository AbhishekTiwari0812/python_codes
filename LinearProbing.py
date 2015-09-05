#linear probling
def h(n,i):
	global TablSize
	return (n+i)%TableSize
def ConvertToInteger(word):	
	NumString=""
	for i in word:
		NumString+=str(ord(i))
	return int(NumString)
def HashDict(wordlist):
	for i in range(len(wordlist)):
		NumEqu=ConvertToInteger(wordlist[i])
		j=0
		while HashTable[h(NumEqu,j)]!=None:			#probing for an empty slot
			j+=1
		HashTable[h(NumEqu,j)]=wordlist[i]
		
import time
m=time.clock()		
WordFile=open('words.txt','r')	#file containing all the Licence plates
lines=WordFile.readlines()
String=' '.join(lines)
wordlist=String.split()
TableSize= 237683	
HashTable=[]	
for i in range(TableSize):
	HashTable.append(None)
HashDict(wordlist)
n=time.clock()
print n-m
#print HashTable