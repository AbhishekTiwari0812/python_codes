global time
global Tracker
global TraversedNodes
time=0
class DFS:
	def __init__(self):
		self.G=None
	def dfsTraversal(self,G):
		G=ConvertInSuitableFormat(G)
		dfs(G)
		return TraversedNodes
	def getConnectedComponent(self,G):
		G=ConvertInSuitableFormat(G)
		dfs(G)
		Tran=Transpose(G)
		CompList=[]
		QuickSort(Tran,0,len(Tran)-1)
		Tran1=Tran[::-1]
		MyConectedComponents=dfs(Tran1)
		for i in MyConectedComponents:
			if i=='\n':
				CompList.append([])
		del CompList[-1]
		j=-1
		for i in MyConectedComponents:
			if i=='\n':
				j+=1
			else:
				CompList[j].append(i)
		return CompList
	def TopoSort(self,B):
		B=ConvertInSuitableFormat(B)
		global CycleDetection
		CycleDetection=False
		dfs(B)
		if CycleDetection==True:
			print 'There\' a cycle in the graph.Topological Sorting not Possible'
		else:
			return TopoSortArray[::-1]


def dfs(G):
		global Tracker
		global TraversedNodes
		global TopoSortArray
		ConectedComponents=[]
		TraversedNodes=[]
		TopoSortArray=list()
		for i in G:
			i.state='NotVisited'
			i.StartTime=0
			i.FinishTime=0
		for i in G:
			if i.value==-1:
				continue
			if i.state=='NotVisited':
				Tracker=[]
				DFSvisit(G,i)
				ConectedComponents.append('\n')
				ConectedComponents.extend(Tracker)
		del ConectedComponents[-1]
		return ConectedComponents

class Node:
	def __init__(self,x):	
		self.value=x
		self.Previous=[]
		self.parent=None
		self.next=[]
		self.StartTime=0
		self.FinishTime=0
		self.state='NotVisited'
	def __str__(self):
		return str(self.value+1)
def Transpose(A):
	TransG=list()
	for i in range(len(A)):
		TransG.append(Node(i))
		TransG[i].FinishTime=A[i].FinishTime
	for i in range(len(A)):
		for j in A[i].next:
			TransG[j.value].next.append(TransG[i])
	return TransG
			
def DFSvisit(G,i):
	global time
	global TopoSortArray
	global Tracker
	global TraversedNodes
	global CycleDetection
	TraversedNodes.append(i.value)
	Tracker.append(i.value)
	i.StartTime=time
	time+=1
	i.state='started'
	for j in i.next:
		if j.state=='NotVisited':
			DFSvisit(G,j)
		if j.state=='started':
			CycleDetection=True
	i.FinishTime=time
	time+=1
	i.state='Finished'
	TopoSortArray.append(i.value)


	
def partition(newA,p,q):
	Pivot=newA[q].FinishTime
	i=p-1
	for j in range(p,q):
		if newA[j].FinishTime<=Pivot:
			i+=1
			newA[i],newA[j]=newA[j],newA[i]
	newA[i+1],newA[q]=newA[q],newA[i+1]
	return i+1
		
def QuickSort(A,p,q):
	if p<q:
		pivpos=partition(A,p,q)
		QuickSort(A,p,pivpos-1)
		QuickSort(A,pivpos+1,q)



#EdgeList=[[1,2],[2,3],[3,4],[4,1],[2,5],[5,6],[6,7],[7,8],[8,5]]
#EdgeList=[[1,2],[2,3],[3,4],[2,5],[5,6],[6,7],[7,8]]

def ConvertInSuitableFormat(EdgeList):
	G=list()
	MAX=0
	for i in EdgeList:
		for j in i:
			if j>MAX:
				MAX=j
	for i in range(MAX+1):
		if i==0:
			G.append(Node(-1))
		else:   
			G.append(Node(i))
	for i in range(len(EdgeList)):
		G[EdgeList[i][0]].next.append(G[EdgeList[i][1]])
	return G 
#A=DFS()
#print A.dfsTraversal(EdgeList)
#print A.getConnectedComponent(EdgeList)
#print A.TopoSort(EdgeList)