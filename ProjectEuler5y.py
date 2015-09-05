t=input()
for i in range(t):
	inp=raw_input()
	dummy=inp.split()
	cons=int(dummy[1])
	n=raw_input()
	A=[]
	for i in n:
		A.append(int(i))
	Pro=1
	for i in range(cons):
		Pro*=A[i]
	Max=Pro
	for i in range(1,len(A)-cons+1):
		if A[i-1]!=0:
			Pro=Pro*A[i+cons-1]/A[i-1]	
		else:
			Pro=1
			for contr in range(cons):
				Pro*=A[i+contr]
		if Pro>Max:
			Max=Pro
	print Max
	