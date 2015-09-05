def PartialInsertionSort(i,k):
	j=(len(A)-i-1)/k
	for p in range(i+k,i+(j+1)*k,k):
		current=p
		for q in range(p-k,i-k,-k):
			if A[q]>A[current]:
				A[current],A[q]=A[q],A[current]
   				current=q

				
				
				
				
#from random import randint
#size=50
#A=list()
#for i in range(size):
# A.append(randint(1,100))
def ShellSort(A,k):
 shell=2
 while(k>0):
    k=k/shell
	for i in range(k):
		PartialInsertionSort(i,k)
	shell+=1
A=input('Enter the array to be sorted ')
ShellSort(A,len(A))
print A