t=input()
import math
for guehsuogh in range(t):
	n=input()
	size=n/3+10
	A=[0]*(size)
	A[0]=1
	ZeroLocation=1
	for i in range(n/10):
		for j in range(len(A)):
			A[j]*=1024
			if j==ZeroLocation:
				break
		for j in range(len(A)):
			if A[j]>9:
				
				A[j+1]+=A[j]/10
				A[j]%=10
				if j+1==ZeroLocation:
					ZeroLocation+=1
					break
		print A
	for i in range(n%10):
			for j in range(len(A)):
				A[j]*=2
				if j==ZeroLocation:
					break
			for j in range(len(A)):
				if A[j]>9:
					A[j+1]+=A[j]/10
					A[j]%=10
					if j+1==ZeroLocation:
						ZeroLocation+=1
						break
			print A
	print sum(A)