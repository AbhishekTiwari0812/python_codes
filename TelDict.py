#TelDict
global TableSize
def h(key,TableToHashIn):
	global TableSize
	while TableToHashIn[(key+(((i**2)+i)/2))%TableSize]==0:
	 i+=1
	return (key+(((i**2)+i)/2))%TableSize
	
	
def Search(TableToSearchIn,TupleToSearchFor):		#take table and tuple as input
	global TableSize
	i=0
	key=ChangeTupInKey(TupleToSearchFor)
	while TableToSearchIn[(key+(((i**2)+i)/2))%TableSize]!=0:
		if TableToSearchIn[(key+(((i**2)+i)/2))%TableSize].val==TupleToSearchFor:
			return TableToSearchIn[(key+(((i**2)+i)/2))%TableSize]
		i+=1
	return -1
def addNumber(NAME,Number):		#Takes table and Vertex as Input
	global TableSize
	i=0
	#key=ChangeTupInKey(NodeToInsert.val)
	NameIndex=StringToInt(NAME)
	while NameList[h(NameIndex+(((i**2)+i)/2))%TableSize]!=0:
		i+=1
	NameList[(NameIndex+(((i**2)+i)/2))%TableSize]=Number
	NumIndex=IntToInt(Number)
	while NumList[h(NumIndex)+(((i**2)+i)/2))%TableSize]]!=0:
		i+=1
	NumList[(NumIndex+(((i**2)+i)/2))%TableSize]=NAME
def StringToInt(Tup):
	counter=0
	MyInt=0
	#print 'This is Tup',Tup
	for i in range(len(Tup)):	
		if counter>10:	
			counter=0
		MyInt+=ord(Tup[i])*(10**counter)
		counter+=1
		#print 'In the for loop',MyInt
	#print 'MyInt',MyInt
	return MyInt
def 