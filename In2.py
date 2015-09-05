A=list()
from random import randint
p=input('Enter the size of the array:')
for i in range (p):
 A.append(randint(1,1000))
print A
#A=input('Enter A')
alpha=input('Enter the value of number of iterations')
P=A[:]
from time import *
m=time()
def twoPick(alpha):
 for k in range(alpha):
  a=randint(0,len(A)-1)
  b=randint(0,len(A)-1)
  i=max(a,b)
  j=min(a,b)
  if A[i]<A[j]:
   temp=A[i]
   A[i]=A[j]
   A[j]=temp
twoPick(alpha)

import matplotlib.pyplot as plt
plt.plot(range(len(A)),A)
plt.show()





print A
def InsertionSort():
	for i in range(1,len(A)):
		current=i
		for j in range(i-1,-1,-1):
			if A[j]>A[current]:
				temp=A[current]
   				A[current]=A[j]
  				A[j]=temp
				current=j
	        plt.plot(range(len(A)),A)
       		plt.show()

InsertionSort()
plt.show()
n=time()
print A
print 'Time taken by modified Insertion sort:%g'%(n-m)
time1=n-m

#==================================================================================================
#Original Insertion Sort
A=P
print A
m=time()
def InsertionSort1():
	for i in range(1,len(A)):
		current=i
		for j in range(i-1,-1,-1):
			if A[j]>A[current]:
				temp=A[current]
  				A[current]=A[j]
				A[j]=temp

				current=j
		plt.plot(range(len(A)),A)
       		plt.show()
InsertionSort1()
n=time()
print A
print 'Time take by actual insertion sort',n-m
print 'Time difference:',
print time1-(n-m)
