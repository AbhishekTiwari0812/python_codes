#hackerRankGraph2


class Set:
	def __init__(self,x):
		self.parent=None
		self.Head=False
		self.count=1
		self.value=x
		
def GetHead(a):
	k=a.parent
	while k.Head!=True:
		k=k.parent
	return k
def Union(a,b):
	if a.parent==None and b.parent==None:
		a.parent=a
		b.parent=a
		a.Head=True
		a.count+=1
	elif a.parent!=None and b.parent==None:
		k=a.parent
		while k.Head!=True:
			k=k.parent
		b.parent=k
		k.count+=1
	elif b.parent!=None and a.parent==None:
		k=b.parent
		while k.Head!=True:
			k=k.parent
		a.parent=k
		k.count+=1	
	else:
		k1=a.parent
		while k1.Head!=True:
			k1=k1.parent
		k2=b.parent
		while k2.Head!=True:
			k2=k2.parent
		if k1.count>k2.count:
			k2.Head=False
			k2.parent=k1
			k1.cout+=k2.count
def Fact(n):
	fact=1
	while n>0:
		fact*=n
		n-=1
	return fact
NodeList=[]
N,l = map(int,raw_input().split())
for i in range(N):
	NodeList.append(Set(i))
for i in xrange(l):
	a,b = map(int,raw_input().split())
	Union(NodeList[a],NodeList[b])
for i in NodeList:
	if i.parent==None:
		i.parent=i
		i.Head=True
SetHeadList={}
for i in range(len(NodeList)):
	k=GetHead(NodeList[i])
	if k in SetHeadList:
		continue
	else:
		SetHeadList[k]=k
NodeList=[]	
Sum=0
for i in SetHeadList:
	NodeList.append(i.count)
TotalSum=sum(NodeList)
for i in range(len(NodeList)):
	TotalSum-=NodeList[i]
	Sum+=NodeList[i]*TotalSum
print Sum