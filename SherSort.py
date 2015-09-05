from time import time
m=time()
reader=open("sherlock.txt",'r')
a=reader.readlines()
#print a				#a is list containing one line in one element
a=' '.join(a)			# a is the whole text 
#print a
A=a.split()		
#print A
B=[]
for i in range(len(A)):
	if A[i].isalpha():
		B.append(A[i].lower())			#B is the list which contains all the words of the  text file
def Sort(P):
 	for i in range(1,len(P)):
		pivot=P[i]
		j=i-1
		while j>=0 and P[j]>pivot:
			P[j+1]=P[j]
			j-=1
		P[j+1]=pivot 

def insertionSort():
	for i in range(1,len(B)):
		Pivot=B[i]
		j=i-1
		while j>=0 and B[j]>Pivot:
			B[j+1]=B[j]
			j-=1
		B[j+1]=Pivot
def BucketSort():
	#global Bucket
	Bucket=list()
	for i in range(26):
		Bucket.append([])
	for i in range(len(B)):
				Bucket[ord(B[i][0])-97].append(B[i])
	for i in range(len(Bucket)):
		Sort(Bucket[i])
	C=[]
	for i in range(len(Bucket)):
		C+=Bucket[i]
	print 'the sorted list:',C

def merge(A,p,q,r):
	left=A[p:q+1]
	right=A[q+1:r+1]
	i=0
	j=0
	for k in range(p,r+1):
		if i<len(left) and j<len(right):
			if left[i]<right[j]:
				A[k]=left[i]
				i+=1
			else:
				A[k]=right[j]
				j+=1
		else :
			break
	if i>=len(left):
		while k<r+1:
			A[k]=right[j]
			j+=1
			k+=1
	else:
		while k<r+1:
			print 'len(Left)',len(left)
			print k
			print i
			A[k]=left[i]
			i+=1
			k+=1
def mergesort(A,p,q):
	if p<q:
		mergesort(A,p,(p+q)/2)
		mergesort(A,(p+q)/2+1,q)
		merge(A,p,(p+q)/2,q)
#BucketSort()
#import random
#B=random.sample(range(100),20)
#print B
#insertionSort()
n=time()
B.sort()
print B
print n-m
