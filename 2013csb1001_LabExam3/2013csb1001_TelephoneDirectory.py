def StringToInt(string):
	counter=0
	MyInt=0
	for i in range(len(string)):	
		if counter>10:	
			counter=0
		MyInt+=ord(string[i])*(10**counter)
		counter+=1
	return MyInt
class TelephoneDirectory:
	def __init__(self):
		self.TableSize=324567
		self.NameList=[[]]*self.TableSize
		#self.NumberList=[[]]*TableSize
	def h(self,key):	
		return key%(self.TableSize)
	def AddEntry(self,name,number):
		newEntry=[name,number]
		k=self.h(StringToInt(name))
		A=self.NameList[k][:]
		for i in A:
			if i[1]==number:
				print 'This number is already in the list'
				return i
		for i in A:
			if i[0]==name:
				print 'This Contact is already in the list'
				return i
		A.append(newEntry)
		self.NameList[k]=A
	def GetNumber(self,name):
		k=self.h(StringToInt(name))
		for i in self.NameList[k]:	
			if i[0]==name:	
				return i
		return 'No Contact with this Name!'
		
	def UpdateNumber(self,name,old_number,new_number):
		k=self.h(StringToInt(name))
		A=self.NameList[k]
		for i in range(len(A)):	
			if A[i][0]==name:
				if A[i][1]!=old_number:
					return 'Wrong information,Check again!'
				A[i][1]=new_number
				return 'Number changed to ',int(new_number),' from ',int(old_number)
	def DeleteEntry(self,name,number):
		k=self.h(StringToInt(name))
		A=self.NameList[k]
		for i in range(len(A)):
			if A[i][0]==name:
				if A[i][1]!=number:
					return 'Wrong info.Check Again!'
				del A[i]
				break
#A=TelephoneDirectory()
#import random
#for i in range(100000):
#	A.AddEntry(str(int(random.random()*100)),str(int(random.random()*100)))
#for i in range(100000):
	#print A.GetNumber(str(int(random.random()*100)))
	#print A.DeleteEntry(str(int(random.random()*100)),str(int(random.random()*100)))