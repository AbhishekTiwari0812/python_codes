#DFS
class Node:
        def __init__(self):
                self.val=None           #Stores the val at the node,if any
                self.Adj=[]             #addresses to the neighbors
                self.TimeStart=0        #Time at which Node is being pushed into the stack
                Self.TimeFinish=0       #Time at which Node is being popped off the stack
                self.parent=None        #Parent of the given node
def DFS(StartingNode):          #only for Undirected Graph
        global Time
        StartingNode.TimeStart=Time
        Time+=1
        MyStack.append(StartingNode)
        for i in StartingNode.Adj:
                if i.TimeStart==0:
                        i.parent=StartingNode
                        DFS(i)
	MyStack.pop()
	StartingNode.TimeFinish=Time
	SortedList.append(StartingNode)         # this list contains inverse of topologically sorted vertices
	Time+=1
	if len(MyStack)==0:
                return SortedList[::-1]                 #returns the topologically sorted list of nodes

	
	
def main():
        
MyStack=[]      #since we're using recursion,there's no need of a stack here :P
Time=0
if __name__=='__main__':
	main()
