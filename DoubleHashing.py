#double hashing
def h2(n):				#auxiliary hash functions 
	global TableSize
	return (n%(TableSize-1))+1		#Return value must be relatively prime with TableSize
def h1(n):
	global TableSize
	return n%TableSize
def h(n,i):		# n is to be hashed in a table of size m
	global TableSize
	return (h1(n)+i*(h2(n)))%TableSize
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
		
		
WordFile=open('WordsDel.txt','r')	#file containing all the Licence plates
lines=WordFile.readlines()
String=' '.join(lines)
wordlist=String.split()
TableSize= len(wordlist)		
HashTable=[]	
for i in range(len(wordlist)):
	HashTable.append(None)
HashDict(wordlist)
print HashTable