next=0
class node:
	def __init__(self):
		self.key=None
		self.left=None
		self.right=None
		self.height=0				#this attribute keeps track of the distance of the node to the root
														#node(considering distance between 2 connected nodes as unity)
def BinSearchInsert(element,root):
	''' this function searches for the appropriate position to store element in the BST''' 
	global next
	if element==root.key:
		return 				#If element already exists in the tree,do nothing
	elif element<root.key:	
		if root.left==None:	
			root.left=node()
			root.left.key=element
			root.left.height=root.height+1		
			HeightList.append(root.left.height)
			keyNheight[next].append(element)
			keyNheight[next].append(root.left.height)
			next+=1
		else:
			BinSearchInsert(element,root.left)
	else:
		if root.right==None:
			root.right=node()	
			root.right.key=element
			root.right.height=root.height+1
			HeightList.append(root.right.height)
			keyNheight[next].append(element)
			keyNheight[next].append(root.right.height)
			next+=1
		else:
			BinSearchInsert(element,root.right)

FileReader=open('Input.txt','r')
NUMS=FileReader.readlines()
Anish=' '.join(NUMS)		#changing NUMS to string
A=Anish.split()				#changing A to list
Size=len(A)
import random
random.shuffle(A)
keyNheight=[]			#This list stores the height of the key 
for i in range(Size):	
	keyNheight.append([])
HeightList=list()		#this list just stores the heights :P 
ROOT=node()
ROOT.key=A[0]
ROOT.height=0
HeightList.append(0)
keyNheight[next].append(ROOT.key)
keyNheight[next].append(ROOT.height)
next+=1
import time
n=time.time()
for i in range(1,len(A)):
	BinSearchInsert(int(A[i]),ROOT)			#checking where to insert A[i] and inserting
print 'Maximum height:',max(HeightList)
# Maximum height of the BST for given Input list is coming out to be 52 
print 'Average height of the nodes is:',float(sum(HeightList))/float(len(HeightList))
# Average heights of the nodes is coming out to be 25 (round-off of 25.0356744448)

#print keyNheight #prints each element height of it
print time.time()-n