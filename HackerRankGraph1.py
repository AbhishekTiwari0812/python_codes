class Node:
	def __init__(self,x):
		self.neighbours=[]
		self.name=x
		self.complist=[]
s = raw_input()
numbers = map(int, s.split())
n=numbers[0]
m=numbers[1]
A=[]
for i in range(n):
	A.append(Node(i))

for i in range(m):
	s = raw_input()
	numbers = map(int, s.split())	
	A[numbers[0]].neighbours.append(A[numbers[1]])
	A[numbers[1]].neighbours.append(A[numbers[0]])