import random
import math
global DELTA
def h(s,t):
	#print 'ewqfwe',int(((s*t*(s-t)*((math.sqrt(5)-1)/2))%1)*len(P))
	
	return int(((s*t*(s-t)*((math.sqrt(5)-1)/2))%1.0)*len(HashTable))
class Point():
	def __init__(self,a,b):
		self.x=a
		self.y=b
		self.s=None
		self.t=None
def tag(p):
	#print 'fhwaufhsh',2/DELTA
	global DELTA
	if DELTA==0:
		print 'Problem with DELTA'
	#print '1.....',int(p.x*(int(float(2/DELTA))+1)),int(p.y*(int(2/DELTA)+1))
	return int(p.x*(int(float(2/DELTA))+1)),int(p.y*(int(2/DELTA)+1))
def MakeDict(Seen):
	global HashTable
	HashTable=list()
	for i in range(len(P)**len(P)):
		HashTable.append([])
	for i in range(Seen):
		#print 'FDSAga'
		s,t=tag(P[i])
		HashTable[h(s,t)].append(P[i])
		HashTable[h(s,t)].append(s)
		HashTable[h(s,t)].append(t)
	#print 'fsahdoi',HashTable
def Insert(Point):
	global HashTable
	s,t=tag(Point)
	HashTable[h(s,t)].append(Point,s,t)
def CloseSubSquares(Point):
	global HashTable
	A=list()
	s,t=tag(Point)
	
	for i in range(s-2,s+3):	
		for j in range(t-2,t+3):
			if 0<=i<=(2/DELTA) and 0<=j<=(2/DELTA):
				A.append(HashTable[h(i,j)])
	#print len(A)
	return A
def d(a,b):
	global size
	#print size
	#print (a.x-b.x)**2
	#print (a.y-b.y)**2
	#print 1000*math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)
	return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)
def main():
	global DELTA
	DELTA=d(P[0],P[1])
	#print '1',DELTA
	MakeDict(2)
	for i in range(2,len(P)):
		SUBS=CloseSubSquares(P[i])
		MIN=DELTA
		#print 'fsdho',MIN
		for j in range(len(SUBS)):
			print 'Goes in for'
			if len(SUBS[j])!=0:
				print 'this is being compared:',j
				print d(SUBS[j][0],P[i]),SUBS[j][0].x,SUBS[j][0].y
				if d(SUBS[j][0],P[i])<MIN:
					MIN=d(SUBS[j][0],P[i])
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

size=6
A=random.sample(range(1000),size)
P=list()
A=[586,291,239,990,96,752]
print A
for i in range(size):
	A[i]=float(A[i])/1000
for i in range(0,size,2):
	P.append(Point(A[i],A[i+1]))
main()
print 'This is DELTA:',DELTA*1000
FaltuMethod()