t=input()
def Power(n,a):
	SUM=0
	while n%a==0:
		SUM+=1
		n/=a
	
	return SUM

for i in range(t):
	n=input()
	B=[]
	A=[2,3,5,7,11,13,17,19,23,29,31,37]
	for i in range(len(A)):
		B.append(0)
	for i in range(1,n+1):
		for j in range(len(A)):
			Max=Power(i,A[j])
			if B[j]<Max:
				B[j]=Max
	product=1
	for k in range(len(A)):
		product*=A[k]**B[k]
	print product