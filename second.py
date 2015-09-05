t=input()
for iter in range(t):	
	p = raw_input()
	p = raw_input()
	mouse = p.split()
	for i in range(len(mouse)):
    		mouse[i] = int(mouse[i])
	q = raw_input()
	holes = q.split()
	for j in range(len(holes)):
    		holes[j] = int(holes[j])
	#print mouse
	#print holes
	dis=[]
	for j in range(len(mouse)):
		for i in range(len(holes)):
			MINI=10**4
			#dis[j].append(abs(mouse[j]-holes[i]))
			if MINI>abs(mouse[j]-holes[i]):
				MINI=abs(mouse[j]-holes[i])
		dis.append(MINI)
	print max(dis)