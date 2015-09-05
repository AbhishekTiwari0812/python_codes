import pdb
def Partition(A,p,q,i):	
	A[i],A[q]=A[q],A[i]
	pivot=A[q]
	counter=p-1
	for i in range(p,q):	
		if A[i]<=pivot:
			counter+=1
			A[counter],A[i]=A[i],A[counter]
	A[q],A[counter+1]=A[counter+1],A[q]
	return counter+1
def insertionSort(Array):	
	for i in range(1,len(Array)):
		pivot=Array[i]
		j=i-1
		while j>0 and Array[j]>pivot:
			
			Array[j+1]=Array[j]
			j-=1
		Array[j+1]=pivot
	return Array[len(Array)/2]
	
def Select(A,p,q,i):
	if ()
	for i in range(p,q+1,5):
		B.append(insertionSort(A[i:i+5]))
	B.append(insertionSort(A[i:q+1])
	med=Select(B,0,len(B)-1,int(len(B)/2))
	q1=partition(A,p,q,med)
	