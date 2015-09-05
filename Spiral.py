def R(i):

	global Size
	if i==Size:
		return
	else:
		global row
	        global column
	        for p in range(i):
		 print A[row][column],
		 column+=1
def U(i):
	global row
	global column
	for p in range(i):
		print A[row][column],
		row-=1
def L(i):
	
		global row
		global column
		for p in range(i):
			print A[row][column],
			column-=1
def D(i):
	global row
	global column
	for p in range(i):
		print A[row][column],
		row+=1
A=[]
Size=input('Size=')
from random import randint
for i in range(Size):
	q=[]
	A.append(q)
	for j in range(Size):
		q.append(randint(1,100))
	print q

row=Size/2
column=Size/2
for i in range(len(A)+1):
	if i%2==1:
		U(i)
		R(i)
	else:
		D(i)
		L(i)








