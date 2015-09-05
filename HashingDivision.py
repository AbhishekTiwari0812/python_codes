import math
global TableSize
def h(key):
	global TableSize
	#check whether it's returning correctly or not
	print int(((key*(math.sqrt(5)-1)/2)%1.0)*TableSize)
	return int(((key*(math.sqrt(5)-1)/2)%1.0)*TableSize)
def ChangeTupInKey(Tup):
	Str=""
	for i in Tup:
		Str+=str(i)
	return int(Str)
def Search(Key,Table):
	Key1=ChangeTupInKey(Key)
	MyLinkedList=Table[h(Key1)]
	for i in range(len(MyLinkedList)):
		if MyLinkedList[i][0]==Key:
			return 'Visited Already'
	return -1
def Insert(Node,Table):
	key=ChangeTupInKey(Node.key)
	Table[h(key)].append(Node.key,Node)
	