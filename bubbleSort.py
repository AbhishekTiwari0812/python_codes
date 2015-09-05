A=input('Enter the array to be sorted')
for j in range((len(A))-1):
	for i in range((len(A))-1):
		if(A[i]>A[i+1]):
			temp=A[i]
			A.insert(i,A[i+1])
			A(i+1,temp)
		
print(A)