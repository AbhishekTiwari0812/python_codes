#
testCases=raw_input()
for i in range(int(testCases)):
	n=input()
	n=int(n)
	n-=1
	s1=n/3
	s2=n/5
	s3=n/15
	SUM=3*s1*(s1+1)/2+5*s2*(s2+1)/2-15*s3*(s3+1)/2
	print SUM