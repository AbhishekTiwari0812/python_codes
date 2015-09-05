#String Operations
name='Banana'
t=name[1]  #t=='a'
t=name[-2]       #t='n' the second last element
Pre='JQLMSW'
Suf='ack'
for letter in Pre:
 print letter+Suf        #Jack Qack Lack Mack Sack Wack
#String Slice
Act='FuckYouMan!'
Slicer1=Act[:4]
Slicer2=Act[4:7]  #you can also define the step up like [0:6:2] will produce [0],[2],[4]
Slicer3=Act[7:]
print Slicer1,Slicer2,Slicer3
#Strings are immutable but you can make a copy and change it and assign the new to the old
greeting='Hello World'
new_greeting='j'+greeting[1:]     #If you try greeting[0]='j' it will produce an error
greeting=new_greeting
print greeting
print greeting.upper()
print greeting.find('lo')                     #you can also give argument for starting point and the ending point of search

for letter in 'Abhishek Anish Tiwari':
 if letter in 'Rajeshwari Shreya Tiwari':
  print letter

print 'c'.islower()