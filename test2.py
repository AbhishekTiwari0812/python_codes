
In='1234 anish ''fw32 123 Abhishek'
a=In.split()			#changes string to list
p=len(a)
todel=list()
def trim():
	for i in range(p):
		if  not a[i].isalpha():			#checks if the word is constructed of alphabets
			todel.append(i)
		
trim()
B=list()
for i in range(len(a)):
	if i not in todel:	
		B.append(a[i])
print B
for i in range(len(B)):			#changes to lower case
	B[i]=B[i].lower()

print B

def partition(A,p,r):
	counter=p-1
	Pivot=A[r]
	for i in range(p,r):
		if A[i]<Pivot:
			counter+=1
			A[i],A[counter]=A[counter],A[i]
	A[counter+1],A[r]=A[r],A[counter+1]
	return counter+1
A=['ahf','bsdfjk','ahf','ab','eo','abcdef','abce','aq']
def quicksort(A,p,r):
	if p<r:
		q=partition(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q+1,r)

def Search(element,B):
	for i in range(len(B)):
		if element ==B[i]:
			print i,element

#print partition(A,0,len(A)-1)
quicksort(A,0,len(A)-1)
print B
print Search('gsdfjpa',A)
print Search('whatthehell',A)
















