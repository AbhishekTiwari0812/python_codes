#HAckerRank


class Node:
	def __init__(self):
		self.counter=0
		self.EdgeList=[]
		self.Parent=None
		self.value=None
		self.leaf=True
def Connect(child,parent):
	child.Parent=parent
	parent.leaf=False
	parent.EdgeList.append(child)
def UpdateCounter(LeafNode):
	x=1
	while LeafNode.Parent!=None:
		A[LeafNode.value-1].Parent.counter+=1
		print LeafNode.value,LeafNode.counter
		print LeafNode.Parent.value,LeafNode.Parent.counter

		LeafNode=LeafNode.Parent
		
		

Inp=raw_input()
InputValues=Inp.split()
n=int(InputValues[0])
m=int(InputValues[1])
A=[]
for i in range(n):
	A.append(Node())
	A[i].value=i+1


for i in range(m):
	Inp=raw_input()
	InputValues=Inp.split()
	From=int(InputValues[0])
	To=int(InputValues[1])
	Connect(A[From-1],A[To-1])
for i in A:
	UpdateCounter(i)
TotalCount=1
for i in A:
	for j in i.EdgeList:
		if j.counter%2!=0:
			TotalCount+=1
print TotalCount