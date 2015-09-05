import random 
#order n^2 algo---->
import time 
m=time.clock()
A = random.sample(xrange(-100000,100000),5000)
start=0
end=0
BIG=0
for i in range(len(A)):
	s=0
	for j in range(i,len(A)):
		#print 'This is BIG:',BIG
		s+=A[j]
		if s>BIG:
			BIG=s
			#print 'This is sum greater than BIG:',sum(A[i:j+1])
			start=i
			end=j
print 'Starting point:',start,'and ending point:',end
print 'And the time taken:',time.clock()-m
#Order(n) time algo
START=0
END=0
SUM=0
start=0
end=0
biggest=0
m=time.clock()
for i in range(len(A)):
	SUM+=A[i]
	if SUM<=0:
		SUM=0
		start=i+1
		end=i
	else:
		if SUM>biggest:
			biggest=SUM
			START=start
			END=end
	end+=1
print 'Second Algo results:','START: ',START,'and END',END
print 'And the time taken:',time.clock()-m