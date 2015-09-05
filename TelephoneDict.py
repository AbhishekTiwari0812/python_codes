global TableSize


def StringToInt(Name):
	counter=0
	MyInt=0
	for i in range(len(Name)):	
		if counter>10:	
			counter=0
		MyInt+=ord(Name[i])*(10**counter)
		counter+=1
	return MyInt
def IntToInt(Number):
	global TableSize
	Number=int(Number)
	Number=(float(Number)*((5**(1/2)-1)/2)%1)*TableSize
	return int(Number)
def h(key,TableToHashIn,k=0):	#if you want to insert pass k='del'
	global TableSize
	i=0
	while TableToHashIn[int(key+(((i**2)+i)/2))%TableSize]!=k and TableToHashIn[(key+(((i**2)+i)/2))%TableSize]!=0:
		print 'stuck here'
		i+=1
	return (key+(((i**2)+i)/2))%TableSize
class TelephoneDirectory:
	def __init__(self):
		global TableSize
		TableSize=6000
		NameList=[]
		NumberList=[]
		NameList=[0]*TableSize
		NumberList=[0]*TableSize
		
	def GetNumber(self,Name):
		key=StringToInt(Name)
		global TableSize
		i=0
		while NameList[(key+(((i**2)+i)/2))%TableSize]!=0:
			if NameList[(key+(((i**2)+i)/2))%TableSize][0]==key:
				return NameList[(key+(((i**2)+i)/2))%TableSize]
			i+=1
		return -1
	def DeleteEntry(self,name,number):
		index1=h(StringToInt(name),NameList,'del')
		index2=h(IntToInt(number),NumberList,'del')
		NameList[index1]='del'
		NumberList[index2]='del'
	def AddEntry(self,name,number):
		index1=h(StringToInt(name),NameList,'del')
		index2=h(IntToInt(number),NumberList,'del')
		NameList[index1]=[name,number]
		NumberList[index2]=[number,name]
	def UpdateNumber(name,old_number,new_number):
		index1=h(StringToInt(name),NameList)
		index2=h(IntToInt(old_number),NumberList)
		if (NumberList[index2]!=0 and NumberList[index1]!='del') or ( NameList[index1]!=0 and NameList[index1]!='del'):
			if (name!=NumberList[index2][1] or number!=NameList[index1][1]):
				print 'There\'s something wrong with the information.Please check if the number is correct'
			else:
				NameList[index1]=[name,new_number]
				NumberList[index2]=[number,new_name]
				print 'Got updated'
				
		else:
			print 'There\'s something wrong with the information.Please check if the number is correct'
			
			
		
AddEntry('Subhas',52837962890)
AddEntry('Subhgewras',52862890)
AddEntry('gserbhas',528962890)
AddEntry('fawajekl',28379643209)
AddEntry('wjerioqps',52803965890)
AddEntry('dafiuwa',508127549)
print GetNumber('dafiuwa')
UpdateNumber('dafiuwa',508127549,6423176)
print GetNumber('dafiuwa')
DeleteEntry('fawajekl',28379643209)
print GetNumber('Subhas')
print GetNumber('fawajekl')
