counter=[]
def partition(A,p,q):
	Pivot=A[q]
	i=p-1
	for j in range(p,q):
		if A[j]<=Pivot:
			i+=1
			A[i],A[j]=A[j],A[i]
		increase(q-1,j-1)
	A[i+1],A[q]=A[q],A[i+1]
	return i+1
def increase(i,j):
	global counter
	counter[i][j]+=1

		
def QuickSort(A,p,q):
	if p<q:
		pivpos=partition(A,p,q)
		QuickSort(A,p,pivpos-1)
		QuickSort(A,pivpos+1,q)
def createZeroMatrix(p):
	for i in range(p):
	 sub=[]
	 for j in range(p):
	  sub.append(0)
	 counter.append(sub)
		
		
		
		
		
		
		
		
Size=input('Enter the size of the random list:')
A=list()
from random import randint
for i in range(size):			#creates a random list of elements of length Size
	A.append(randint(1,100))
createZeroMAtrix(Size)                  #creates a matrix of dimension Size*Size
B=A[:]									#to keep a history of 
for i in range(1000):
 A=B[:]
 QuickSort(A,0,len(A)-1)


print 'Sorted list:':A
print 'The matrix corresponding to comparisons done:'
print counter
