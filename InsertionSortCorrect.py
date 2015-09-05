from time import time
A=[4,5,754,5,329,8,37,6,4,45,3,6,4,3,6,43,5,2,4,3,5,6,53,43,1,24,1,432,453,2543,45,4,2,2,32,4,35,4,7,64,645,53,56,656,32,2]
m=time()

def InsertionSort():
	for i in range(1,len(A)):
		pivot=A[i]
		j=i-1
		while j>=0 and  pivot<A[j]:
			A[j+1]=A[j]
			j-=1
		A[j+1]=pivot
InsertionSort()
print A
n=time()
print n-m
