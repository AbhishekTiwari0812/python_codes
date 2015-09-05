#List Operations
t1=['Anish',2,143,'Shreya']
t2=['Abhishek','Rajeshwari',19,20]
t1[1:3]=['These are integers','So I changed it']
print t1
t1=t1+t2                 #this t1 has nothing to do with original t1
print t1
t1.extend(t2)
print t1
t1.sort()
print t1
t3=[1,24,2,4]
print sum(t3)		#prints the sum of all
print t3.pop(1)		#pops out the index value given
print t3
t1.remove('Abhishek')      #removes the element (once only not all)
print t1 
del t1[2:5]
print t1
str1='I love you Shreya,meri-Jaan'
t4=str1.split()            #splits string w.r.t. spaces
print t4
str2=' '.join(t4)
print str2

