import random

def Partition(A,p,q):	
	pivot=A[q]
	counter=p-1
	for i in range(p,q):	
		if A[i]<=pivot:
			counter+=1
			A[counter],A[i]=A[i],A[counter]
	A[q],A[counter+1]=A[counter+1],A[q]
	if len(A)/3 <=counter+1<=(2*len(A))/3:
		#print counter+1,A[counter+1]
		return counter+1
	else:
		return randomizedPartition(A,p,q)
def randomizedPartition(A,p,q):
	i=random.choice(range(q-p+1))
	A[i],A[q]=A[q],A[i]
	r=Partition(A,p,q)
	return r
def RandSelect(A,p,r,i):
	if p==r:
		return A[p]
	else:
		q=randomizedPartition(A,p,r)
		k=q-p
	if i==k:
		return A[q]
	elif i<k:
		return RandSelect(A,p,q-1,i)
	else:
		return RandSelect(A,q+1,r,i)

A=random.sample(range(100),20)
print RandSelect(A,0,len(A)-1,10)
A.sort()
print A[10]