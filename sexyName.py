#multithreading
from threading import *
class MyThread(Thread):
	def __init__(self,ID):
		Thread.__init__(self)
		self.x="anish"
		self.ID=ID
	def run(self):
		global counter
		global lock
		for i in range(10):
			counter+=1
			lock.acquire()
			print "In the thread Number:",self.ID
			lock.release()
def main():
	global lock
	global counter
	lock=Lock()
	counter=0
	Thread1=MyThread(1)
	Thread2=MyThread(2)
	Thread3=MyThread(3)
	Thread4=MyThread(4)
	Thread5=MyThread(5)
	Thread1.start()
	Thread2.start()
	Thread3.start()
	Thread4.start()
	Thread5.start()
	Thread1.join()
	Thread2.join()
	Thread3.join()
	Thread4.join()
	Thread5.join()
	print 'printing counter',counter,'this worked !'
	



	
	
	
	
	
	
	
	
	
	
	
	
	
	
main()