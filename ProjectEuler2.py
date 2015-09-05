sqrt5=5**(0.5)
#print sqrt5
phi=((sqrt5+1.0)/2.0)
#print phi

def f(n):
	n+=1
	return int((phi**n)/sqrt5 +(0.5))

t=input()

for i in range(int(t)):
	n=input()
	n=int(n)
	Sum=0
	k=1
	temp=0
	while(temp<=n):	
		#print temp
		if temp%2==0:
			Sum+=temp
			
		k+=1
		l=k+1
		temp=int((phi**l)/sqrt5 +(0.5))
		
	print Sum