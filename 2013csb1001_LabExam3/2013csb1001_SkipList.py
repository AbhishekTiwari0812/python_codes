global HEAD
def InsertIn(MyNode,PrevNode):
	MyNode.prev=PrevNode
	MyNode.next=PrevNode.next
	PrevNode.next.prev=MyNode
	PrevNode.next=MyNode
class Vertex:
	def __init__(self):	
		self.key=None
		self.prev=None
		self.next=None
		self.UP=None	#links between keys 
		self.DOWN=None	#links between keys 
	def __str__(self):
		return str(self.key)
import random		
def StairsForUp(Node):
	global HEAD
	global TAIL
	if random.random()>=0.5000000:
		k=Node.prev
		while k.UP==None:
			k=k.prev
		if k.UP!=HEAD.UP:
			NewNode=Vertex()
			NewNode.key=Node.key
			NewNode.DOWN=Node
			Node.UP=NewNode
			InsertIn(NewNode,k.UP)
		else:
			NewHead=Vertex()
			NewHead.key=-1
			NewTail=Vertex()
			NewTail.key='inf'
			NewTail.prev=NewHead
			NewHead.next=NewTail
			NewNode=Vertex()
			NewNode.key=Node.key
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
	


class SkipList:
	def __init__(self):	 
		global HEAD
		HEAD=0
		Initialize()
	def SearchNode(self,value):
		global HEAD
		k=self.SearchNode1(value,HEAD)
		if k.key==value:
			return k
		print value,' is not in the list.'
	def SearchNode2(self,value):	
		global HEAD		
		return self.SearchNode1(value,HEAD)		
	def SearchNode1(self,value,StartPoint):
		while StartPoint.key!=value:
			if value>StartPoint.key:
				StartPoint=StartPoint.next
				continue
			elif value<StartPoint.key:
				if StartPoint.DOWN!=None:
					return self.SearchNode1(value,StartPoint.DOWN.prev)
				else:
					return StartPoint.prev
		while StartPoint.DOWN!=None:
			StartPoint=StartPoint.DOWN
		return StartPoint
	def AddNode(self,NEW):	
			'''takes a new value creates a new node.
			re-arranges previous next pointers etc'''
			#Initialize()
			global HEAD
			NewNode=Vertex()
			NewNode.key=NEW
			PreviousNode=self.SearchNode2(NEW)
			if PreviousNode.key!=NEW:
				InsertIn(NewNode,PreviousNode)
				StairsForUp(NewNode)
			else:
				print "New node is already in the skipList"
			
	def DeleteNode(self,value):
			'''takes a value,searches for it and deletes the node from 
			the list'''
			#Initialize()
			DeleteNode=self.SearchNode2(value)
			if DeleteNode.key!=value:
				print value,' is Not in the list!!!'
				return None
			else:
				while DeleteNode!=None:
					DeleteNode.prev.next=DeleteNode.next
					DeleteNode.next.prev=DeleteNode.prev
					DeleteNode=DeleteNode.UP	
def Initialize():
	global HEAD
	global TAIL
	if HEAD==0:
		HEAD=Vertex()
		HEAD.key=-1
		TAIL=Vertex()
		TAIL.key='inf'
		HEAD.next=TAIL
		TAIL.prev=HEAD
		TAIL.UP='dummy'
		HEAD.UP='dummy'
#A=SkipList()
#for i in range(10000):
#	A.AddNode(int(random.random()*100))
#A.AddNode(432789)
#for i in range(10000):
#	print 'searching........',A.SearchNode(int(random.random()*100))
#	print 'deleting......',A.DeleteNode(int(random.random()*100))
#print A.SearchNode(432789)
#A.DeleteNode(432789)
#A.SearchNode(432789)
#A.AddNode(4563)
#A.SearchNode(432789)
#print A.SearchNode(4563)