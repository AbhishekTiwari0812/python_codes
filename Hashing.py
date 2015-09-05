WordFile=open('words.txt','r')	#file containing all the Licence plates
lines=WordFile.readlines()
String=' '.join(lines)
wordlist=String.split()
import math
def hash(n):	#hashing n
	#string=str(n)
	#string=string[::-1]
	#n=int(string)
	return (n**n)%Size
m=[]		#M keeps record of keys  already allotted
Size=len(wordlist)		#total number of keys already present
for i in range(Size):
	m.append([])
def ConvertToInt(word):				#converts each word to a corresponding Integer
	ReNum=''
	for i in word:
		ReNum+=str(ord(i)-40)
	return int(ReNum)
	
def Manage():	
	global wordlist 	#maps words to keys via hashing and creates a hash table
	for i in range(len(wordlist)):
		m[hash(ConvertToInt(wordlist[i]))].append(wordlist[i])
def search(element):
	k=hash(ConvertToInt(element))
	found='none'
	for i in range(len(m[k])):
		if m[k][i]==element:
			found=i
	return k,found		#returns bucket number and the index of the element 
def insert(new):
	m[hash(ConvertToInt(new))].append(new)
def delete(ToBeDeleted):
	bucketNo,index=search(ToBeDeleted,m[hash(ConvertToInt(ToBeDeleted))])
	if index!='none':
		del m[bucketNo][index]
	else:
		print 'Plate Number not found'

Manage()
print 'Done managing'
max=0
for i in range(Size):	
	if len(m[i])>max:
		max=len(m[i])	
print max
