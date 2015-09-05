#reading from a file.
reader=open('text.txt','r')
#data=reader.read(10)
#data =reader.readline()
contents=reader.readlines()
count =0
total=0
#while data!='':        for read() and readline()
#	print (len(data),data)
	#data=reader.read(20)
	#data =reader.readline()
for data in contents:
	count+=1
	total+=len(data)
	print (data)
	print (len(data))
print ("Average:",float(total)/float(count))

