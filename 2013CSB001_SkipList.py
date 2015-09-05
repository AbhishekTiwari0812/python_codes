#SkipList
#2nd length=(1st length)^(1/n) if we're using n lists.
#we use n=lg(length of linked list given to us)

class SkipList:
	def __init__(self,value):	
		self.key=value
		self.prev=None
		self.next=None
		self.UP=None	#links between keys 
		self.DOWN=None	#links between keys 
def SearchNode(value,StartPoint):
	while StartPoint.key!=value:
		#print StartPoint
		if value>StartPoint.key:
			StartPoint=StartPoint.next
			continue
		elif value<StartPoint.key:
			if StartPoint.DOWN!=None:
				return SearchNode(value,StartPoint.DOWN.prev)
			else:
				return StartPoint.prev
	while StartPoint.DOWN!=None:
		StartPoint=StartPoint.DOWN
	return StartPoint
def InsertIn(MyNode,PrevNode):
	MyNode.prev=PrevNode
	#print PrevNode.key
	MyNode.next=PrevNode.next
	#print PrevNode.next
	#print 'row',PrevNode
	#print PrevNode.next
	PrevNode.next.prev=MyNode
	PrevNode.next=MyNode
def AddNode(NEW):	
		'''takes a new value creates a new node.
		re-arranges previous next pointers etc'''
		global HEAD
		NewNode=SkipList(NEW)
		PreviousNode=SearchNode(NEW,HEAD)
		if PreviousNode.key!=NEW:
			InsertIn(NewNode,PreviousNode)
			StairsForUp(NewNode)
		else:
			print "New node is already in the skipList"
		
import random		
def StairsForUp(Node):
	print 'dhioqjow'
	global HEAD
	global TAIL
	if random.random()>=0.5000000:
		print 'dhioqjow'
		k=Node.prev
		while k.UP==None:
			print 'line 2343',k.key
			k=k.prev
		if k.UP!=HEAD.UP:
			NewNode=SkipList(Node.key)
			NewNode.DOWN=Node
			Node.UP=NewNode
			InsertIn(NewNode,k.UP)
		else:
			NewHead=SkipList(-1)
			NewTail=SkipList('inf')
			NewTail.prev=NewHead
			NewHead.next=NewTail
			NewNode=SkipList(Node.key)
			NewNode.DOWN=Node
			Node.UP=NewNode
			NewHead.UP='dummy'
			NewTail.UP='dummy'
			InsertIn(NewNode,NewHead)
			NewHead.DOWN=HEAD
			HEAD.UP=NewHead
			NewTail.DOWN=TAIL
			TAIL.UP=NewTail
			HEAD=NewHead
			TAIL=NewTail
		StairsForUp(NewNode)
def DeleteNode(value):
		'''takes a value,searches for it and deletes the node from 
		the list'''
		DeleteNode=SearchNode(value,HEAD)
		if DeleteNode.key!=value:
			print value,' is Not in the list!!!'
			return None
		else:
			while DeleteNode!=None:
				DeleteNode.prev.next=DeleteNode.next
				DeleteNode.next.prev=DeleteNode.prev
				DeleteNode=DeleteNode.UP

HEAD=SkipList(-1)
TAIL=SkipList('inf')
HEAD.next=TAIL
TAIL.prev=HEAD

TAIL.UP='dummy'
HEAD.UP='dummy'
AddedList=[]
for i in range(10):
	k=int(random.random()*50)
#	if i==0:
#		new=SkipList(k)
#		new.prev=Sentinal
#		Sentinal.next=new
	AddNode(k)
	print 'adding',k 
	AddedList.append(k)
print AddedList
for i in range(10):
	k=int(random.random()*10)
	DeleteNode(AddedList[k])	
	print 'deleting',k,'th element:',AddedList[k]
for i in range(10):
	k=int(random.random()*10)
	print SearchNode(AddedList[k],HEAD)
	print 'searching for',k,'th element:',AddedList[k]	 