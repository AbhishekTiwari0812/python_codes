A=input('Enter the Array to be sorted')
l=len(A)      #Length of the array
def InsertionSort(A):
 for i in range(1,l):
	for j in range(i-1,-1,-1):
		if A[i]<A[j]:           #Compares to all previous elements
			temp=A[i]
			A[i]=A[j]
			A[j]=temp
			continue
		else:
			break
InsertionSort(A)
print A