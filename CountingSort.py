#counting Sort
A=[]
size=input('Size:')
from random import randint
for i in range(size):
	A.append(randint(1,100))
print A
C=list()
for i in range(101):
	C.append(0)
for i in range(len(A)):
	C[A[i]]+=1
for i in range(1,len(C)):
 C[i]+=C[i-1]
B=list()
for i in range(size):
	B.append(0)
for j in range(len(A)-1,-1,-1):
	B[C[A[j]]-1]=A[j]
	C[A[j]]-=1
print B