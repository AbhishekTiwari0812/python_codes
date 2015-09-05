MY_ROOT=None
import time
import random
def LLR(x):
	x.left.LR()
	x.RR()
def RRR(x):
	x.right.RR()
	x.LR()
class Node:
	def __init__(self):
		self.key=None
		self.height=1
		self.left=None
		self.right=None
		self.parent=None
		self.weight=0
		self.level=0
	def UpdateHeight(self):
		if self.left!=None and self.right!=None:		#x has both the children
			self.height=max(self.left.height,self.right.height)+1
		elif self.left!=None and self.right==None:	#x has only left child
			self.height=self.left.height+1	
		elif self.left==None and self.right!=None:	#x has only right child
			self.height=self.right.height+1
		else:									#x has no child 
			self.height=1
#		print 'Height of node:',self.key,' has become:',self.height
		self.UpdateWeight()
	def UpdateWeight(self):
		if self.left!=None and self.right!=None:		#x has both the children
			self.weight=self.right.height-self.left.height
		elif self.left!=None and self.right==None:	#x has only left child
			self.weight=0-self.left.height
		elif self.left==None and self.right!=None:	#x has only right child
			self.weight=self.right.height-0
		else:								#x has no child 
			self.weight=0
	def CheckWeightBalance(self):		#should return where to go next
		'''checks if the height of left sub-tree and right sub tree differ by more than 100
		if yes,then balances them using rotation'''
		#self.UpdateWeight()
		#print abs(self.weight),'and key',self.key
		if abs(self.weight)<=1:
			#print 'Did nothing'
			k=2+3		#do nothing
			return self.parent
		elif self.weight==-2:
			if self.left.weight==1:
				LLR(self)
				return self.parent
			else:
				self.RR()
				return self.parent
		else:#self.weight==2
			if self.right.weight==1:
			#	print 'line:55'
				self.LR()
				
				return self.parent
			else:
			#	print 'line:60'
				RRR(self)
				return self.parent
	def UpdateLevel(self):
		if self.parent==None:
			self.level=0
		else:
			self.level=self.parent.level+1
	def LR(self):
		#print 'In LR'
		global MY_ROOT
		y=self.right
		self.right=y.left
		if y.left!=None:
			y.left.parent=self
		y.parent=self.parent
		#print 'This is self.parent',self.parent
		if self.parent==None:
			MY_ROOT=y	
		#	print 'ROOT changed'
		elif self.parent.left==self:
			self.parent.left=y
		else:
			self.parent.right=y
		y.left=self
		self.parent=y
		self.UpdateHeight()
		y.UpdateHeight()
		y.UpdateLevel()
		self.UpdateLevel()
		#y.UpdateLevel()
		#self.UpdateWeight()
		#y.UpdateWeight()
		#self.UpdateWeight()
		#return self
	def RR(self):
		global MY_ROOT
		y=self.left
		self.left=y.right
		if y.right!=None:
			y.right.parent=self
		y.parent=self.parent
		if self.parent==None:
			MY_ROOT=y
		elif self.parent.left==self:
			self.parent.left=y
		else:
			self.parent.right=y
		y.right=self
		self.parent=y
		self.UpdateHeight()
		y.UpdateHeight()
		y.UpdateLevel()
		self.UpdateLevel()
		#y.UpdateLevel()
		#self.UpdateWeight()
		#y.UpdateWeight()
		#self.UpdateWeight()
		#return self
#def FindROOT(k):
#	global MY_ROOT
#	'''Finds out the ROOT of the tree'''
#	if k.parent!=None:

#		return FindROOT(k.parent)
#	else:
#		print 'This is the root of the tree:',k.key,'and this is MY ROOT:',MY_ROOT
#		return k
def BST_Search(root,x):			#returns the pointer where to insert		
	if root.key==x:
		return root
	elif x<root.key:
		if root.left==None:
			root.left=Node()
			root.left.parent=root
			root.left.level=root.level+1
			return root.left
		else:
			return BST_Search(root.left,x)
	else:
		if root.right==None:
			root.right=Node()
			#root.right.height=1
			root.right.parent=root
			#root.UpdateHeight()
			root.right.level=root.level+1
			return root.right
		else:
			return BST_Search(root.right,x)
class AVL:
	def __init__(self):	
		self.h=0		#height of the tree
		self.t=0		#time taken to insert "input.txt"
		
def AVL_Insert(x):
	global MY_ROOT
	'''Inserts x in the tree,
	updates the heights parents recursively,
	checking for imbalance and fixing it.'''
	if MY_ROOT==None:
		#print 'going in'
		MY_ROOT=Node()
		MY_ROOT.key=x
	else:
		ToBePlaced=BST_Search(MY_ROOT,x)
		ToBePlaced.key=x
		k=ToBePlaced.parent
		#print 'Inserting',x
		
		while k!=None:
			k.UpdateHeight()
			#print 'Parent is:',k.key
			k=k.CheckWeightBalance()		
def printTree(Start):
	if Start.left!=None:
		printTree(Start.left)
	#Start.UpdateHeight()
	#print 'Start.key===========>>>',Start.key,' and height:::::::::::',Start.height
	if Start.right!=None:
		printTree(Start.right)


Size=input('Enter the size')
A=range(10**6)

random.shuffle(A)
p=time.clock()
#A=[1,2,3]
for i in range(0,len(A)):
	print i
	AVL_Insert(A[i])
#print 'Ultimate:',ULTIMATE_ROOT.key

print 'This is the ROOT:',MY_ROOT.key
#printTree(MY_ROOT)
print time.clock()-p