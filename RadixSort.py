def digg(p,i):
	return int ((p%(10**i))-(p%(10**(i-1))))/10**(i-1)
def CountingSort(A,d):
	size=len(A)
	C=list()
	for i in range(10):
		C.append(0)
	for i in range(len(A)):
		C[digg(A[i],d)]+=1
	for i in range(1,len(C)):
	 C[i]+=C[i-1]
	B=list()
	for i in range(size):
		B.append(0)
	for j in range(len(A)-1,-1,-1):
		B[C[digg(A[j],d)]-1]=A[j]
		C[digg(A[j],d)]-=1
	return B

def RadixSort(A):
	for i in range(1,int(math.log(max(A)))):
		A=CountingSort(A,i)
	return A

import random
import math
A=random.sample(range(1000),100)
print A
A=RadixSort(A)		
print A