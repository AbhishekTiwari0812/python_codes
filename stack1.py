class stack:
	def __init__(self,Name):
		self.stack=[]
		self.top=-1
		self.name=Name
	def StackEmpty(self):
		if self.top == -1:
 			return 'TRUE'
 		else:
			return 'FALSE'
	def push(self,x):
 		self.top+=1
		self.stack.append(x)
	def pop(self):
		if self.StackEmpty()=='TRUE':
			print "Stack Under-flow"
		else:
			self.top-=1
			return self.stack[self.top+1]
	def __str__(self):
		return "stack is:"+str(self.stack)+"\nthe top element is:"+str(self.stack[self.top])
