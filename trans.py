A=list()
countOne=0
countTwo=0
from random import randint
p=input('Enter the size of the array:')
for i in range (p):
 A.append(randint(1,1000))
print A
alpha=input('Enter the value of number of iterations')
P=A[:]
from time import *
#m=time()
def twoPick(alpha):
 for k in range(alpha):
  a=randint(0,len(A)-1)
  b=randint(0,len(A)-1)
  i=max(a,b)
  j=min(a,b)
  if A[i]<A[j]:
   A[j],A[i]=A[i],A[j]
   global countOne
  countOne+=1
twoPick(alpha)
#from pylab import *
#for i  in range(len(A)):
 #plot(i,A[i],'*')
 #show()
print A
#print countOne
def InsertionSort():
	for i in range(1,len(A)):
		current=i
		for j in range(i-1,-1,-1):
			if A[j]>A[current]:
				A[j],A[current]=A[current],A[j]
   				current=j
				global countOne
				countOne+=1
			else:
				countOne+=1
				break
InsertionSort()
#n=time()
print A
print 'Transactions taken by modified Insertion Sort:',countOne
#print 'Time taken by modified Insertion sort:%g'%(n-m)
#time1=n-m

#==================================================================================================
#Original Insertion Sort
A=P
#print A
#m=time()
def InsertionSort1():
	for i in range(1,len(A)):
		current=i
		for j in range(i-1,-1,-1):
			if A[j]>A[current]:
				A[j],A[current]=A[current],A[j]
  				current=j
				global countTwo
				countTwo+=1			
			else:
				countTwo+=1	
				break
InsertionSort1()
#n=time()
print A
print 'Transactions taken by Insertion Sort:',countTwo
#print 'Time take by actual insertion sort',n-m
#print 'Time difference:',
#print time1-(n-m)
