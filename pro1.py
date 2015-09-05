 B=list()
#bink=list()
 from random import *
#for i in range(10): 
 size=10
 for i in range(size):
 	B.append(randint(1,10))
 A=B[:]
 alpha=0
 C=B[:]
 AlphaKeep=list()
 B.sort()
 for i in range(100):
  global alpha
  alpha=0
  while(1==1):
   a=randint(0,len(A)-1)
   b=randint(0,len(A)-1)
   i=max(a,b)
   j=min(a,b)
   if A[i]<A[j]:
    temp=A[i]
    A[i]=A[j]
    A[j]=temp
   if(A!=B):
    B==C
    global alpha
    alpha+=1
    continue
   else:
    AlphaKeep.append(alpha)
    A=C[:]
    break
 print AlphaKeep
# bink.append(sum(AlphaKeep)/len(AlphaKeep))
#print bink 