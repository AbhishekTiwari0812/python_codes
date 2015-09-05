def l(k):
	aliasl=SFC(k)[:]
	for i in range(len(aliasl)):
		aliasl[i][0],aliasl[i][1]=aliasl[i][1],aliasl[i][0]
	print 'length:',len(aliasl),'aliasl:',aliasl
	return aliasl
def u1(k):
	aliasu1=SFC(k)[:]
	for i in range(len(aliasu1)):
		aliasu1[i][0]+=2**k
	print 'length:',len(aliasu1),'aliasu1:',aliasu1
	return aliasu1
def u2(k):
	alaisu2=SFC(k)[:]	
	for i in range(len(alaisu2)):
		alaisu2[i][0]+=2**k
		alaisu2[i][1]+=2**k
	print 'length:',len(alaisu2),'aliasu2:',alaisu2
	return alaisu2
def r(k):

	aliasr=SFC(k)[:]
	for i in range(len(aliasr)):
		aliasr[i],aliasr[len(aliasr)-i-1]=aliasr[len(aliasr)-i-1],aliasr[i]
	for i in range(len(aliasr)):
			aliasr[i][1]+=2**k
	return aliasr

def SFC(n):
	if n==1:
		return [[1,1],[2,1],[2,2],[1,2]]
	else:
		p=list()
		p=l(n-1)+u1(n-1)+u2(n-1)+r(n-1)
		return p
		
print SFC(2)
