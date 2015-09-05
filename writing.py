#writing in a text file
writer=open('PyWriter','w')
reader=open('text.txt','r')
writer.write('Elements')
#print >> (writer,'Elements')
writer.writelines(['he','Ar','Ne','Kr'])
#for gas in ['he','Ar','Ne','Kr']:
#	print >> (writer,gas) automatically adds newline character.
writer.close()
