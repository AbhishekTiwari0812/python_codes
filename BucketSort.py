import pdb
def InsertionSort(bucket):
	for i in range(len(bucket)):
		pivot=bucket[i]
		j=i-1
		while j>=0 and bucket[j]>pivot:
			A[j+1]=A[j]
			j-=1
		A[j+1]=pivot
def BucketSort(A):
	#pdb.set_trace()
	B=[[]]*len(A)
	#make all the elements ranging from 0 to 1
	MAX=max(A)
	MAX+=1
	for i in range(len(A)):
		A[i]/=MAX
	for i in range(len(A)):
		B[(int(A[i]*len(B)))].append(A[i])
	C=[]
	for i in range(len(B)):
		InsertionSort(B[i])
	#C+=B[i]
	print B







import random
A=[]
for i in range(10):
	A.append(random.random()*100)

#print A
BucketSort(A)
#print A		
