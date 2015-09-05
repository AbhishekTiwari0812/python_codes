def partition(A,p,q):
	Pivot=A[q]
	i=p-1
	for j in range(p,q):
		if A[j]<=Pivot:
			i+=1
			A[i],A[j]=A[j],A[i]
	A[i+1],A[q]=A[q],A[i+1]
	return i+1
	
A=input('Enter the list to be partitioned')
p=input('Enter the lower index from where you wanna start compare for the partitioning')
q=input('Enter the index of the pivot element')
print 'Index of pivot element in the partitioned list is',partition(A,p,q)