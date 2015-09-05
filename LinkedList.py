class linkedlist:
	def __init__(self):
		self.next=linkedlist()
		self.previous=linkedlist()
		self.value=None
	def getValue(self,x):	
		self.value=x
	def GetPrevious(self,prev):
		self.previous=prev
	def GetNext(self,nexT):	
		self.next=nexT
