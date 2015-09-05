import threading
import time 


class AsyncWriter(threading.Thread):
	def __init__(self,text,out):
		threading.Thread.__init__(self)			#to make it a thread
		self.text=text
		self.out=out
		
	def run(self):			#when background.start is called,this starts executing.
		f=open('self.out','a')
		f.write(self.txt+"\n")
		f.close()
		time.sleep(2)
		print 'Finished background file write to',self.out
		
		
def main():	
	message=raw_input("Enter the string to store")
	background=AsyncWriter(message,'out.txt')
	background.start()
	print "The prgram continues to run while background runs"
	print 100+400
	background.join()
	print "Waited until thread was complete"
	
if __name__=='__main__':
	main()