
class Queue:
	def __init__(self):
		self.size=100		#Queue memory size
		for i in range(self.size):	
			self.queue.append(None)
		self.head=0
		self.tail=0
	def enqueue(self,x):
		self.queue[self.tail]=x
		if tail!=(self.size-1):
			self.tail+=1
		else:
			self.tail=0
	def dequeue(self):
		x=self.queue[self.head]
		if self.head==self.size-1:
			self.head=0
		else:
			self.head+=1
		return x
	