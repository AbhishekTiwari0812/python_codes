#union
MyDict={}
def f(n):
	if n not in MyDict:
		pro=1
		for i in range(n):
			pro*=i+1
		MyDict[n]=pro
		return pro
	else:
		return MyDict[n]


class Union :
	def __init__(self,x):
		self.parent=None
		self.head=False
		self.value=x
		self.cardinality=1
def MakeUnion(a,b):
	if a.parent==None and b.parent==None:
		a.parent=a
		b.parent=a
		a.head=True
		a.cardinality+=1
	elif a.parent!=None and b.parent==None:
		k=a.parent
		
		while k.head!=True:
			
			k=k.parent
		b.parent=k
		k.cardinality+=1
	elif b.parent!=None and a.parent==None:
		k=b.parent
		while k.head!=True:
			k=k.parent
		a.parent=k
		k.cardinality+=1
	else:
		k1=a.parent
		k2=b.parent
		while k1.head!=True:
			k1=k1.parent
		while k2.head!=True:
			k2=k2.parent
		if k1.cardinality>k2.cardinality:
			k2.head=False
			k2.parent=k1
			k1.head=True
			k1.cardinality+=k2.cardinality
		else:
			k1.head=False
			k2.head=True
			k1.parent=k2
			k2.cardinality+=k1.cardinality
	
A=raw_input()
A=A.split()
Indices=[]
for i in range(int(A[0])):
	Indices.append(Union(i))
for j in range(int (A[1])):
	p=(raw_input())
	p=p.split()
	
	m=int(p[0])
	n=int(p[1])
	MakeUnion(Indices[m],Indices[n])
Product=1
for i in range(len(Indices)):
	if Indices[i].head==True:
		Product*=f(Indices[i].cardinality)
	if Product>=(10**9)+7:
		Product%=(10**9)+7
		
print Product%((10**9)+7)
