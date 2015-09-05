import random
import math
global size
global DELTA
DELTA=4
size=6
def tag(p):
	global DELTA
	if DELTA==0:
		print 'Problem with DELTA'
	return int(p.x*(int(float(2/DELTA))+1)),int(p.y*(int(2/DELTA)))
class Point:
	def __init__(self,a,b):
		global DELTA
		self.x=a
		self.y=b
		
	def __str__(self):
		return "("+str(self.x)+","+str(self.y)+")"
def h(A):
	s=A[0]
	t=A[1]
	return int(((s*t*(s-t)*math.sqrt((5)-1)/2)%1)*len(HashTable))
def Insert(Point):
	HashTable[h(tag(Point))].append(Point)
def Search(Point):
	s,t=tag(Point)
	temp=h(s,t)
	for i in range(len(temp)):
		print 'oierwo',tag(temp[i])
		if (s,t)==tag(temp[i]):
			return temp[i]
def MakeDict(Seen):
	global HashTable
	HashTable=list()
	for i in range(len(P)*2):
		HashTable.append([])
	for i in range(Seen):
		HashTable[h(tag(P[i]))].append(P[i])
		

def ClosestPair(Point):
	global DELTA
	A=list()
	s,t=tag(Point)
	for i in range(s-2,s+3):
		for j in range(t-2,t+3):
			temp=HashTable[h((i,j))]
			for k in range(len(temp)):
				if 0<=i<=(2/DELTA)+1 and 0<=j<=(2/DELTA)+1:
					if tag(temp[k])==(i,j):
						A.append(temp[k])
	#for i in range(len(A)):
		#print A[i],',',
	#print '\n'
	return A
def d(a,b):
	#print 1000*math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)
	return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)
def main():
	global DELTA
	DELTA=d(P[0],P[1])
	MakeDict(2)
	for i in range(2,len(P)):
		SUBS=ClosestPair(P[i])
		MIN=DELTA
		#print 'fsdho',MIN
		for j in range(len(SUBS)):
			#print d(SUBS[j],P[i]),SUBS[j].x,SUBS[j][0].y
			if d(SUBS[j],P[i])<MIN:
				MIN=d(SUBS[j],P[i])
		if MIN!=DELTA:
			DELTA=MIN
			MakeDict(i)
		else:
			Insert(P[i])
def FaltuMethod():
	NEWMIN=321
	k=1
	global size
	for i in range(len(P)):
		for j in range(i+1,len(P)):
			#print 'd',k,': is...',d(P[i],P[j])*size
			k+=1
			if d(P[i],P[j])<NEWMIN:
				NEWMIN=d(P[i],P[j])
	global size
	print 'This is found by FaltuMethod:',NEWMIN*1000

size=100
A=random.sample(range(10000),size)
P=list()
#A=[672,31,980,287,316,232]
#A=[798,42,285,44,514,29,605,64,616,379]
#print A
for i in range(size):
	A[i]=float(A[i])/10000
for i in range(0,size,2):
	P.append(Point(A[i],A[i+1]))
main()
print 'This is DELTA:',DELTA*1000
FaltuMethod()
print 'This is DELTA:',DELTA*1000