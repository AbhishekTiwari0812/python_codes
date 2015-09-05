import math
def h(n,sizeOfTable):
	while n>10**10:
		n/=1.7932
	
	gamma=(math.sqrt(5)-1.0)/2.0
	c=n*gamma
	#print 'c=',c
	a=(c%1.0)
	#print 'a=',a
	b=a*sizeOfTable
	#print 'b=',b
	return int(b)
	return int((n*gamma%1.0)*sizeOfTable)
def convertToNum(word):
	num=0
	for i in word:
		num+=ord(i)
		num*=7
	return num
def hash(TheList):
	for i in range(len(TheList)):
		M[h(convertToNum(TheList[i]),len(TheList))].append(TheList[i])
reader=open("words.txt",'r')
a=reader.readlines()
#print a				#a is list containing one line in one element
a=' '.join(a)			# a is the whole text 
#print a
A=a.split()
M=[]
for i in range(len(A)):	
	M.append([])
hash(A)
#print M

mAx=0
for i in range(len(M)):
	if mAx<len(M[i]):
	 mAx=len(M[i])
print mAx
print len(M)