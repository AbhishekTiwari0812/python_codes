#from test_solver import *
from rubik import *
class Vertex:
	def __init__(self):
		self.val=-1		#tuple value of the state
		#self.state='NotVisited'	# other states visited and finished
		#self.PlacesToGO=[]
		self.childList=[]
		self.parent=None
	def NeighborList(self):			#returns the possible states 'this' can go to,list of tuples
		flu =self.val[0] # (0-th cubie; front face)
		luf = self.val[1] # (0-th cubie; left face)
		ufl = self.val[2] # (0-th cubie; up face)
		fur = self.val[3] # (1-st cubie; front face)
		urf = self.val[4] # (1-st cubie; up face)
		rfu = self.val[5]# (1-st cubie; right face)
		fdl = self.val[6] # (2-nd cubie; front face)
		dlf = self.val[7] # (2-nd cubie; down face)
		lfd = self.val[8] # (2-nd cubie; left face)
		frd = self.val[9] #  (3-rd cubie; front face)
		rdf = self.val[10] # (3-rd cubie; right face)
		dfr = self.val[11] # (3-rd cubie; down face)
		bul = self.val[12] # (4-th cubie; back face)
		ulb = self.val[13] # (4-th cubie; up face)
		lbu = self.val[14] # (4-th cubie; left face)
		bru = self.val[15] # (5-th cubie; back face)
		rub = self.val[16] # (5-th cubie; right face)
		ubr = self.val[17] # (5-th cubie; up face)
		bld = self.val[18] # (6-th cubie; back face)
		ldb = self.val[19] # (6-th cubie; left face)
		dbl = self.val[20] # (6-th cubie; down face)
		bdr = self.val[21] # (7-th cubie; back face)
		drb = self.val[22]# (7-th cubie; down face)
		rbd = self.val[23] # (7-th cubie; right face)
		F = (fdl, dlf, lfd, flu, luf, ufl, frd, rdf, dfr, fur, urf, rfu,bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)
		Fi = perm_inverse(F)
			# Left face rotated clockwise.
		L = (ulb, lbu, bul, fur, urf, rfu, ufl, flu, luf, frd, rdf, dfr,dbl, bld, ldb, bru, rub, ubr, dlf, lfd, fdl, bdr, drb, rbd)
		# Left face rotated counter-clockwise.
		Li = perm_inverse(L)
		# Upper face rotated clockwise.
		U = (rfu, fur, urf, rub, ubr, bru, fdl, dlf, lfd, frd, rdf, dfr,luf, ufl, flu, lbu, bul, ulb, bld, ldb, dbl, bdr, drb, rbd)
		# Upper face rotated counter-clockwise.
		Ui = perm_inverse(U)
		#self.PlaceToGo=[F,Fi,L,Li,U,Ui]
		return [F,Fi,L,Li,U,Ui]
def GetKey(Vert):	#creates the int format of tuple value(takes tuple as input)
	key=""
	for i in Vert:
		key+=str(i)
	return int(key)
def Search(WhichTable,key):#takes input a tuple,searches in the table
	#(to check whether it's already been visited or not.if not,inserts it in the table)
	global SeenStart
	global SeenEnd
	if WhichTable=='s':
		if key not in SeenStart:
			#print 'inserting in seenStart'
			SeenStart[key]=key
			return -1
		else:
			return 'Visited already'
	else:
		
		if key not in SeenEnd:
			#print 'inserting in seenEnd'
			#print SeenEnd
			SeenEnd[key]=key
			return -1
		else:
			return 'Visited already'
def GetNext(Initial,vert):			#creates a list of unvisited childList returns the unvisited child List,a list of vertices which are to be visited.
	children=vert.NeighborList()	#children are all(tuple value of vertices of) possible vertices vert can go to.
	for  i in range(6):
		if Search(Initial,children[i])==-1:
			NewVert=Vertex()
			NewVert.parent=vert
			NewVert.val=children[i]
			vert.childList.append(NewVert)
	return	vert.childList 
		#seen points from end
		#Seen points from start
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
	Search('s',current_state.val)
	Search('e',Final_state.val)
	while Qone!=[] or Qtwo!=[]:
		current_state=Qone[0]
		Final_state=Qtwo[0]
		ls=GetNext('s',current_state)			#puts the ls list in the  SeenStart list too.
		le=GetNext('e',Final_state)			#puts the le list in the SeenEnd list too.
		for  i in range(len(ls)):
			Qone.append(ls[i])
		for  i in range(len(le)):
			Qtwo.append(le[i])
		flag=0
		#for i in ls:
		#	if i.val in SeenEnd:		#List of vertices in SeenStart
		#		flag=1
		#		MeetingPoint=i
		#		print 'flag changed here in ls'
		#		break
		for i in le:		#List of vertices in SeenEnd
			if i.val in SeenStart:
				flag=1
				MeetingPoint=i
				print 'flag changed here in le'
				for j in ls:
					if j.val==i.val:
						otherDirection=j
				break
		#print SeenStart
		#print SeenEnd
		if flag==1:
			MyPath=[]
			while MeetingPoint.parent!=None:
				MyPath.append(MeetingPoint.parent)
				MeetingPoint=MeetingPoint.parent
			while OtherDirection.parent!=None:
				MyPath.append(OtherDirection.parent)
				OtherDirection=OtherDirection.parent
			print 'Path found'
			break
		else:
			del Qone[0]
			del Qtwo[0]
	return MyPath
	
	#print 'In while loop'	
	

start =I
middle1=perm_apply(F, start)
middle2=perm_apply(F, middle1)
end =perm_apply(Li, middle2)	
	
shortest_path(start,end)
	
from time import clock
m=clock()
start = (6, 7, 8, 20, 18, 19, 3, 4, 5, 16, 17, 15, 0, 1, 2, 14, 12, 13, 10, 11, 9, 21, 22, 23)
end =I
shortest_path(start,end)
#print 'time taken:',clock()-m
start=I
middle1 =perm_apply(F, start)
middle2 =perm_apply(L, middle1)
middle3 =perm_apply(F, middle2)
end =perm_apply(L, middle3)
shortest_path(start, end)
start=I
middle1=perm_apply(F, start)
middle2=perm_apply(F, middle1)
perm_apply(Li, middle2)
shortest_path(start, end)