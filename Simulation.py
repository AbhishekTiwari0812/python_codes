#Hospital Simulation
def Left(i):
	return 2*i+1
def Right(i):
	return 2*i+2
def swap(p,q):
	A[p],A[q]=A[q],A[p]
def message1():
	'''prints the message when patients keep on coming to a larger extent'''
	print 'Time to close the hospital,please come tomorrow.'
def message2():
	'''prints message when all the patients are cured'''
	print 'All the patients are cured,time for doctor to take a lunch break'
def heapify(A,i):
	'''Used to maintain the property of max-heap at the i-th node'''
	l=Left(i)
	r=Right(i)
	global heapsize
	if l<=heapsize and A[l]>A[i]:
		largest=l
	else:
		largest=i
	if r<=heapsize and A[r]>A[largest]:
		largest=r
	if largest!=i:
		swap(i,largest)
		heapify(A,largest)
def BuildMaxHeap():
	'''helps making the the unordered array a max-heap'''
	for i in range(len(A)/2-1,-1,-1):
		heapify(A,i)
def ServeMostCritical():
 '''Patient with most criticality is popped out to be treated by the doctor'''
 global heapsize
 if heapsize==0:
	message2()
 else:
	 swap(0,heapsize)
	 print 'Doctor Cured patient with Criticality:',A[heapsize],'\nCheers Everyone!!\n^_^'
	 del A[heapsize]
	 heapsize-=1
	 
def AddPatient(i):
	'''Adds a new patient of criticality i to the original list'''
	global heapsize	
	print 'new patient with criticality:',i,' is added to the list'
	A.append(i)
	heapsize+=1
	BuildMaxHeap()	
def CriticalityHandler(i,change):
	'''Changes the criticality of ith patient to new variable "change" '''
	print 'Criticality of:',i,'th element changed from ',A[i],' to:',change
	A[i]=change
	BuildMaxHeap()
import random
size=input('Enter the number of patients lined up before the hospital was opened: ')
A=random.sample(range(1,100),size)			#sets up criticality to each of the patients randomly
heapsize=len(A)-1
for i in range(10):
	p=random.choice(range(100))				#Helps randomly choosing  whether to increase criticality or add  a new patient or Serve a critical case.
	if 0<=p<=40:
		crit=random.choice(range(100))
		print 'New patient coming,with criticality:',crit,'.Please clear the way'
		AddPatient(crit)
	elif 41<=p<=69:
		ServeMostCritical()
	else:
		print 'criticality changing'
		CriticalityHandler(random.choice(range(len(A))),random.choice(range(100)))
		
	print 'Total patients still remaining to be treated:',heapsize
	print 'Criticalities:',A
	if heapsize==0:             #in case when all the patients are treated and the list is empty
		     	break

if heapsize!=0:
	message1()
else:
	message2()








