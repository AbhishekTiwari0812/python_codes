import random
class node:
	def __init__(self):
		self.key=None
		self.left=None
		self.right=None

def BinSearchInsert(element,root):
	global ROOT
	if element==ROOT.key:
		print	"The element is in the tree" 
	elif element<root.key:
		if root.left==None:	
			root.left=node()
			root.left.key=element
		else:
			BinSearchInsert(element,root.left)
	else:
		if root.right==None:
			root.right=node()	
			root.right.key=element
		else:
			BinSearchInsert(element,root.right)
def printTree(Start):
	if Start.left!=None:
		printTree(Start.left)
	print Start.key
	if Start.right!=None:
		printTree(Start.right)
Size=input('Enter the size')
A=list()
for i in range(Size):	
	A.append(random.randint(1,100))
print A
ROOT=node()
ROOT.key=A[0]
for i in range(1,len(A)):
	BinSearchInsert(A[i],ROOT)
printTree(ROOT)