class Stack:
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
		print 'pushing:',x
		self.stack.append(x)
	def pop(self):
		if self.StackEmpty()=='TRUE':
			print "Stack Under-flow"
		else:
			self.top-=1
			print 'popping:',self.stack[self.top+1]
			return self.stack[self.top+1]
	def Top(self):
		return self.stack[self.top]


def Hanoi4(Rings,first,second,third,fourth):
	if Rings == 1:
		fourth.push(first.pop())
		print first.name," --> ",fourth.name
	elif Rings==2:
		print first.name," --> ",second.name
		second.push(first.pop())
		print first.name," --> ",fourth.name
		fourth.push(first.pop())	
		print second.name," --> ",fourth.name
		fourth.push(second.pop())
	else:
		Hanoi4(Rings-2,first,third,fourth, second)		
		print first.name," --> ",third.name
		third.push(first.pop())
		print first.name," --> ",fourth.name
		fourth.push(first.pop())
		print third.name," --> ",fourth.name
		print 'third.top:',third.Top()
		fourth.push(third.pop())
		Hanoi4(Rings - 2, second, first, third,fourth)
n=input('number of rings:\n')
First=Stack('First')
Second=Stack('Second')
Third=Stack('Third')
Fourth=Stack('Fourth')
for i in range(n):
	print n-i
	First.push(n-i)

Hanoi4(n,First,Second,Third,Fourth)
for i in range(n):
	print Fourth.pop()