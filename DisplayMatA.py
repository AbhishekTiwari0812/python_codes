counter=list()
def createZeroMatrix(p):                #creates a matrix of size p*p
	for i in range(p):
	 sub=[]
	 for j in range(p):
	  sub.append(0)
	 counter.append(sub)
def increase(x,y):                      #increases respective indices in the matrix if elements x and y are compared in Partition function
	for index in range(len(C)):
		if x==C[index]:
			index1=index
		if y==C[index]:
			index2=index
	counter[index1][index2]+=1
	counter[index2][index1]+=1
	
def partition(A,p,q):
	Pivot=A[q]
	i=p-1
	for j in range(p,q):
		increase(Pivot,A[j])
		if A[j]<=Pivot:
			i+=1
			A[i],A[j]=A[j],A[i]
	A[i+1],A[q]=A[q],A[i+1]
	return i+1
def QuickSort(A,p,q):
	if p<q:
		pivpos=partition(A,p,q)
		QuickSort(A,p,pivpos-1)
		QuickSort(A,pivpos+1,q)
Size=input('Enter the size of the random list:')
A=list()
from random import randint
for i in range(Size):
	A.append(randint(1,1000))
B=A[:]		#to keep a history of original unsorted list
C=A[:]       	#to make a sorted list for checking the indices 
C.sort()		
createZeroMatrix(Size) 
import random
for i in range(1000):
 random.shuffle(A)
 QuickSort(A,0,len(A)-1)

 
for i in range(Size):
 for j in range(Size):
 
  print counter[i][j],
 print ' '