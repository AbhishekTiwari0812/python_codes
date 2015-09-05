import math
def h(n,i,TableSize):
	return (n+(((i**2)+i)/2))%TableSize
def ConvertToInteger(word):	
	NumString=""
	for i in word:
		NumString+=str(i)
	NumString=int(NumString)
def HashDictInsert(i,HashTable,TableSize):
	#for i in range(len(wordlist)):
	NumEqu=ConvertToInteger(i)
	j=0
	while HashTable[h(NumEqu,j,TableSize)]!=None:			#probing for an empty slot
		j+=1
	HashTable[h(NumEqu,j,TableSize)]=(i,
def Search(key,HashTable):
	
		
WordFile=open('Words.txt','r')	#file containing all the Licence plates
lines=WordFile.readlines()
String=' '.join(lines)
wordlist=String.split()
TableSize= 2**(int(math.log(len(wordlist),2))+1)		
HashTable=[]	
for i in range(TableSize):
	HashTable.append(None)
HashDict(wordlist)
print HashTable