#from test_solver import *
from rubik import *
import math
global TableSize
def h(key,TableToHashIn):
	global TableSize
	while TableToHashIn[(key+(((i**2)+i)/2))%TableSize]==0:
	 i+=1
	return (key+(((i**2)+i)/2))%TableSize
	
	
def Search(TableToSearchIn,TupleToSearchFor):		#take table and tuple as input
	global TableSize
	i=0
	key=ChangeTupInKey(TupleToSearchFor)
	while TableToSearchIn[(key+(((i**2)+i)/2))%TableSize]!=0:
		if TableToSearchIn[(key+(((i**2)+i)/2))%TableSize].val==TupleToSearchFor:
			return TableToSearchIn[(key+(((i**2)+i)/2))%TableSize]
		i+=1
	return -1
def Insert(TableToHashIn,NodeToInsert):		#Takes table and Vertex as Input
	global TableSize
	i=0
	key=ChangeTupInKey(NodeToInsert.val)
	while TableToHashIn[(key+(((i**2)+i)/2))%TableSize]!=0:
		i+=1
	TableToHashIn[(key+(((i**2)+i)/2))%TableSize]=NodeToInsert
def ChangeTupInKey(Tup):
	counter=0
	MyInt=0
	#print 'This is Tup',Tup
	for i in range(len(Tup)):	
		if counter>10:	
			counter=0
		if Tup[i]==0:
			continue
		MyInt+=Tup[i]*(10**counter)
		counter+=1
		#print 'In the for loop',MyInt
	#print 'MyInt',MyInt
	return MyInt
class Vertex:
	def __init__(self):
		self.val=-1		#tuple value of the state
		self.childList=[]		#set of vertices to go to
		self.parent=None
	def NeighborList(self):			#returns the possible states 'this' can go to,list of tuples
		return [perm_apply(F,self.val),perm_apply(Fi,self.val),perm_apply(L,self.val),perm_apply(Li,self.val),perm_apply(U,self.val),perm_apply(Ui,self.val)]
def getPath(Vertices,startlen):
	PathList=[]
	for i in range(1,startlen):
		N=Vertices[i].parent.NeighborList()
		for j in range(len(N)):
			if N[j]==Vertices[i].val:
				PathList.append(j)
	for i in range(startlen,len(Vertices)):
		N=Vertices[i].NeighborList()
		for j in range(6):			
			if N[j]==Vertices[i-1].val:
				if j%2==0:
					PathList.append(j+1)
				else:
					PathList.append(j-1)
	return PathList

	
def GetValidChildren(MyTable,Vert):		#takes Table and Vertex as input
	PosChildList=Vert.NeighborList()
	ValidChildList=[]
	for i in PosChildList:
		Pos=Search(MyTable,i)
		if Pos==-1:
			NewVert=Vertex()
			NewVert.val=i
			NewVert.parent=Vert
			Insert(MyTable,NewVert)
			ValidChildList.append(NewVert)
	return ValidChildList	
			


def shortest_path(start,end):	
	import time
	m=time.clock()
	"""
	Using 2-way BFS, finds the shortest path from start_position to
	end_position. Returns a list of moves. 
	You can use the rubik.quarter_twists move set.
	Each move can be applied using rubik.perm_apply
	"""
	#raise NotImplementedError
	Qone=[]		#Enqueues the vertices to be visited  from start
	Qtwo=[]		#Enqueues the vertices to be visited from end
	Size=2356789
	global TableSize
	TableSize= 2**((int(math.log(Size,2)))+1)
	SeenStart=[0]*TableSize
	SeenEnd=[0]*TableSize
	
	
	current_state=Vertex()
	current_state.val=start
	Final_state=Vertex()
	Final_state.val=end
	Qone.append(current_state)
	Qtwo.append(Final_state)
	Insert(SeenStart,current_state)
	Insert(SeenEnd,Final_state)
	if current_state.val==Final_state.val:
		return []
	counter=0
	LCounts=0
	LCounte=0
	Counts=0
	Counte=0
	while (Qone!=[] or Qtwo!=[]):
			counter+=1
			current_state=Qone[0]
			Final_state=Qtwo[0]
			ls=GetValidChildren(SeenStart,current_state)			#puts the ls list in the  SeenStart list too.
			le=GetValidChildren(SeenEnd,Final_state)			#puts the le list in the SeenEnd list too.
			Qone.extend(ls)
			Counts+=len(ls)
			Qtwo.extend(le)
			Counte+=len(le)
			flag=0
			for i in ls:
				k=Search(SeenEnd,i.val)
				if k!=-1:
					flag=1
					MeetingPointLs=i
					MeetingPointLe=k
					break
			for j in le:		#List of vertices in SeenEnd
				k=Search(SeenStart,j.val)
				if k!=-1:
					flag=1
					MeetingPointLe=j
					MeetingPointLs=k
					break
			if flag==1:
				Path=[]
				Path.append(MeetingPointLs)
				while MeetingPointLs.parent!=None:
					Path.append(MeetingPointLs.parent)
					MeetingPointLs=MeetingPointLs.parent
				Path=Path[::-1]
				startlen=len(Path)
				while MeetingPointLe.parent!=None:
					Path.append(MeetingPointLe.parent)
					MeetingPointLe=MeetingPointLe.parent	
				break
			else:
				del Qone[0]
				del Qtwo[0]
			if Counts==LCounts and Counte==LCounte:
				return None
			else:
				LCounts=Counts
				LCounte=Counte
	FinalPath=getPath(Path,startlen)
	PATH_STRING=[F,Fi,L,Li,U,Ui]
	x=[0]*len(FinalPath)
	for i in range(len(x)):
		x[i]=PATH_STRING[FinalPath[i]]
	return x

def Check():		
	start =I
	end=perm_apply(F, start)
	shortest_path(start, end) #path length 1
	start=I
	middle1 =perm_apply(F, start)
	middle2 =perm_apply(L, middle1)
	middle3 =perm_apply(F, middle2)
	end =perm_apply(L, middle3)
	shortest_path(start, end)		#path length 4
	start =I
	middle1=perm_apply(F, start)
	middle2=perm_apply(F, middle1)
	end =perm_apply(Li, middle2)	
	shortest_path(start,end)#path length 3
	from time import clock
	m=clock()
	start = (6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23)
	end =I
	shortest_path(start,end)		#path length 14
	print 'time taken:',clock()-m
	start=I
	middle1 =perm_apply(F, start)
	middle2 =perm_apply(Li, middle1)
	middle4=perm_apply(Fi, middle2)
	middle3=perm_apply(U, middle4)
	end =perm_apply(U, middle3)
	shortest_path(start, end)		#path length 5
	start=I
	middle1=perm_apply(F, start)
	middle2=perm_apply(F, middle1)
	shortest_path(start,middle2)		#path length 2

#Check()
#input_configuration()