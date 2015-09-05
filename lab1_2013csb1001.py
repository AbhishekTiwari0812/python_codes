MY_ROOT=None
import time
import random
def LLR(x):
	x.left.LR()
	x.RR()
def RRR(x):
	x.right.RR()
	x.LR()
class Node1:
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
				self.LR()
				return self.parent
			else:
				RRR(self)
				return self.parent
	def LR(self):
		global MY_ROOT
		y=self.right
		self.right=y.left
		if y.left!=None:
			y.left.parent=self
		y.parent=self.parent
		if self.parent==None:
			MY_ROOT=y	
		elif self.parent.left==self:
			self.parent.left=y
		else:
			self.parent.right=y
		y.left=self
		self.parent=y
		self.UpdateHeight()
		y.UpdateHeight()
		
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
def AVL_Search(root,x):			#returns the pointer where to insert		
	if root.key==x:
		return root
	elif x<root.key:
		if root.left==None:
			root.left=Node1()
			root.left.parent=root
			root.left.level=root.level+1
			return root.left
		else:
			return AVL_Search(root.left,x)
	else:
		if root.right==None:
			root.right=Node1()
			root.right.parent=root
			root.right.level=root.level+1
			return root.right
		else:
			return AVL_Search(root.right,x)
class AVL:

	def __init__(self):	
		self.h=0		
		self.t=0		
		self.tree=None
	def insert(self,FileName):
		global MY_ROOT
		MY_ROOT=None
		FileReader=open(FileName,'r')
		NUMS=FileReader.readlines()
		Anish=' '.join(NUMS)		#changing NUMS to string
		A=Anish.split()				#changing A to list
		self.tree=[]
		for i in range(len(A)):
			
			self.tree.append(int(A[i]))
		n=time.clock()
		for i in range(len(A)):
			#print i
			AVL_Insert(self.tree[i])
		self.t=time.clock()
	def height(self,element='NothingPassed'):
		global MY_ROOT
		fixingLevel(MY_ROOT,0)
		if element=='NothingPassed':
			return MY_ROOT.height-1
		return AVL_Search(MY_ROOT,element).level
	def avg_height(self):
		global MY_ROOT
		heights=[]
		fixingLevel(MY_ROOT,0)
		heightCal(MY_ROOT,heights)
		return float(sum(heights))/len(heights)
def heightCal(Start,LeafHeight):
	if Start.left!=None:
		heightCal(Start.left,LeafHeight)
	if Start.left==None and Start.right==None:
		LeafHeight.append(Start.level)
	if Start.right!=None:
		heightCal(Start.right,LeafHeight)
def AVL_Insert(x):
	global MY_ROOT
	'''Inserts x in the tree,
	updates the heights parents recursively,
	checking for imbalance and fixing it.'''
	if MY_ROOT==None:
		#print 'going in'
		MY_ROOT=Node1()
		MY_ROOT.key=x
	else:
		ToBePlaced=AVL_Search(MY_ROOT,x)
		ToBePlaced.key=x
		k=ToBePlaced.parent		
		while k!=None:
			k.UpdateHeight()
			k=k.CheckWeightBalance()	
def printTreeAVL(Start):
	if Start.left!=None:
		printTreeAVL(Start.left)
	#print 'Start.key===========>>>',Start.key,' and height:::::::::::',Start.level
	if Start.right!=None:
		printTreeAVL(Start.right)
def fixingLevel(Start,i):
	if Start!=None:
		Start.level=i
		fixingLevel(Start.left,i+1)
		fixingLevel(Start.right,i+1)
class node:
	def __init__(self):
		self.h=-1
		self.t=0
		self.leaf=1
		self.key=None
		self.left=None
		self.right=None
		self.parent=None
class BST:
	def __init__(self):
		self.k=None
		self.HeightSum=[]
		self.ROOT=None
		self.t=None
	def insert(self,NewFile):
		'''takes input a'''
		FileReader=open(NewFile,'r')
		NUMS=FileReader.readlines()
		Anish=' '.join(NUMS)		#changing NUMS to string
		A=Anish.split()				#changing A to list
		self.ROOT=node()
		self.ROOT.key=A[0]
		self.k=[]
		self.HeightSum=[]	
		n=time.clock()
		for i in range(len(A)):
			self.k.append(int(A[i]))
		for i in range(len(self.k)):
			#print i
			BST_Insert(self.ROOT,self.k[i])
		self.t=time.clock()-n		
	def avg_height(self):
		HeightSum=[]
		for i in range(len(self.k)):
			CheckForThis=BST_Search(self.ROOT,self.k[i])
			if CheckForThis.leaf==1:
				self.HeightSum.append(CheckForThis.h)	
				#print 'it\'s a leaf',CheckForThis.key
		return float(sum(self.HeightSum))/len(self.HeightSum)
	def height(self,k=0):
		if k==0:	
			if self.HeightSum==[]:
				self.avg_height()
			return max(self.HeightSum)
		else:
			Search=BST_Search(self.ROOT,k)
			return Search.h
	def PRINT(self):	
		InOrderWalk(self.ROOT)
def BST_Search(root,x):
	if root.key==x:
		return root
	elif x<root.key:
		if root.left==None:
			root.left=node()
			root.leaf=0
			root.left.h=root.h+1
			root.left.parent=root
			return root.left
		else:
			return BST_Search(root.left,x)
	else:
		if root.right==None:
			root.right=node()
			root.leaf=0
			root.right.parent=root
			root.right.h=root.h+1
			return root.right
		else:
			return BST_Search(root.right,x)
def BST_Insert(root,x):	
	ToBePlaced=BST_Search(root,x)
	ToBePlaced.key=x
def InOrderWalk(root):
	if root!=None:	
		InOrderWalk(root.left)
	#	print root.key,'and it\'s height:',root.h
		InOrderWalk(root.right)
