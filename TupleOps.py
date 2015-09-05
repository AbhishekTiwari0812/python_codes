#Tuples
#tuples are immutable
t='a','b','c','d',143,69,'anything'   #you can use parentheses too
print t
if isinstance(t,tuple):
 print 'yay'
#can't modify but replacement is possible
t=('Changed',)+t[1:]
print t
#swaping made Easy Brought to you by Tuple & Co. O:-)
a=(10,20,30,'a')          #can be anything
b=(5,'Sup Nigga')
a,b=b,a			#left side is tuple and right side is value of tuples
print a
print b
#variable length arguments in tuple
def printAll(*args):
 for i in args:
  print i
printAll('I','am','mad')
printAll('Tuples','are','so' ,'awesome')
t=11,3
print divmod(*t)       #returns quotient and remainder
#Zipping->you can zip two types in one list..
p=[1,2,3]
t=('anish','abhishek','Shreya')
t1=zip(t,p)			#creates a list of tuples
print t1,t1[0][0],t[1][:]
#you can give ranks by enumerate('str')
for index,element in enumerate('Anish'):
 print index,element
#we can change dictionary into tuples simply by dictObj.items()
