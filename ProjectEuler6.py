t=1
for guehsuogh in range(t):
	n=input()
	A=[]
	for k in range(n):
		inp=raw_input()
		A.append(inp)
	Result=[0]*100
	something=1
	for i in range(49,-1,-1):
		Sum=0
		for j in range(n):
			Sum+=int(A[j][i])
		Result[-1*something]=Sum
		something+=1
	for iter in range(len(Result)-1,-1,-1):
		if Result[iter]>9:
			Result[iter-1]+=Result[iter]/10
			Result[iter]%=10
	MyString=""
	i=0
	while Result[i]==0:
		i+=1
		continue
	for k in range(10):
		MyString+=str(Result[i])
		i+=1
	print MyString