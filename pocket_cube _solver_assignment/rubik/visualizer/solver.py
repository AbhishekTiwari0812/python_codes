#from test_solver import *
from rubik import *
class Vertex:
	def __init__(self):
		self.val=-1		#tuple value of the state
		self.childList=[]		#set of vertices to go to
		self.parent=None
	def NeighborList(self):			#returns the possible states 'this' can go to,list of tuples
		return [perm_apply(F,self.val),perm_apply(Fi,self.val),perm_apply(L,self.val),perm_apply(Li,self.val),perm_apply(U,self.val),perm_apply(Ui,self.val)]
	def __str__(self):
		tup=""
		for i in range(len(self.val)):
			tup+=str(self.val[i])
		return tup
#def GetKey(Vert):	#creates the int format of tuple value(takes tuple as input)
#	key=""
#	for i in Vert:
#		key+=str(i)
#	return int(key)
def Search(WhichTable,key):#takes input a tuple,searches in the table
	#(to check whether it's already been visited or not.
	global SeenStart
	global SeenEnd
	if WhichTable=='s':
		if key not in SeenStart:
			return -1
		else:
			return 'Visited already'
	else:
		if key not in SeenEnd:
			return -1
		else:
			return 'Visited already'
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
def GetNext(Initial,vert):			#creates a list of unvisited childList returns the unvisited child List,a list of vertices which are to be visited.
	children=vert.NeighborList()	#children are all(tuple value of vertices of) possible vertices vert can go to.
	for  i in range(6):
		if Search(Initial,children[i])==-1:
			NewVert=Vertex()
			if Initial=='s':
				SeenStart[children[i]]=(children[i],NewVert)
			else:
				SeenEnd[children[i]]=(children[i],NewVert)
			NewVert.parent=vert
			NewVert.val=children[i]
			vert.childList.append(NewVert)
	return	vert.childList 
def shortest_path(start,end):
	"""
	Using 2-way BFS, finds the shortest path from start_position to
	end_position. Returns a list of moves. 
	You can use the rubik.quarter_twists move set.
	Each move can be applied using rubik.perm_apply
	"""
	#raise NotImplementedError
	Qone=[]		#Enqueues the vertices to be visited  from start
	Qtwo=[]		#Enqueues the vertices to be visited from end
	global SeenStart
	global SeenEnd
	SeenStart={}
	SeenEnd={}
	current_state=Vertex()
	current_state.val=start
	Final_state=Vertex()
	Final_state.val=end
	Qone.append(current_state)
	Qtwo.append(Final_state)
	SeenStart[current_state.val]=(current_state.val,current_state)
	SeenEnd[Final_state.val]=(Final_state.val,Final_state)
	if current_state.val==Final_state.val:
		return []
	counter=0
	lastStart=0		#To check if there exists a solution or not
	lastEnd=0		#To check if there exists a solution or not
	while (Qone!=[] or Qtwo!=[]):
		current_state=Qone[0]
		Final_state=Qtwo[0]
		ls=GetNext('s',current_state)			#puts the ls list in the  SeenStart list too.
		le=GetNext('e',Final_state)			#puts the le list in the SeenEnd list too.
		#for  i in range(len(ls)):
			#Qone.append(ls[i])
		#for  i in range(len(le)):
		#	Qtwo.append(le[i])
		Qone.extend(ls)
		Qtwo.extend(le)
		flag=0
		for i in ls:
			if i.val in SeenEnd:		#
				flag=1
				MeetingPointLs=i
				MeetingPointLe=SeenEnd[i.val][1]
				break
		for j in le:		#List of vertices in SeenEnd
			if j.val in SeenStart:
				flag=1
				MeetingPointLe=j
				MeetingPointLs=SeenStart[j.val][1]
				break
		counter+=1
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
		elif len(SeenStart)-lastStart ==0 and len(SeenEnd)-lastEnd==0:	#If there doesn't exist any solution
			return None
		else:
			del Qone[0]
			del Qtwo[0]
		lastStart=len(SeenStart)
		lastEnd=len(SeenEnd)
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