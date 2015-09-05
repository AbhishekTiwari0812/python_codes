def partition(A,p,q):
	Pivot=A[q]
	i=p-1
	for j in range(p,q):
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

		
		
#A=list()
#from random import randint
#for i in range(10):
#	A.append(randint(1,100))
#print A
A=input('Enter the list to be sorted')
QuickSort(A,0,len(A)-1)
print A
