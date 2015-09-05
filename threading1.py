#threading 
import threading
def DoAfter():
	global x
	
def Do_this():
	global Dead,x
	print "This is my thread\n"
	while x<300:
		x+=1
	print x
def main():
	global Dead,x
	x=0
	lock=threading.Lock()
	# lock.acquire() lock.release()
	Dead=False
	My_thread=threading.Thread(target=Do_this,name="My_thread",args=())	#makes a thread object,arguments target=The label where you wanna start 
	# name names the thread,uses to give the arguments of the target function
	My_thread.start()							# calls run attribute of Thread object
	print threading.active_count()	#prints the number of threads actively running
	print threading.enumerate()		#gives the list of running threads
	print threading.current_thread()
	print My_thread.is_alive()
	My_thread.join() 	#No other thread starts before finishing My_thread
	#Join waits current thread to terminate,before starting a new thread
	
	raw_input("Hit a key to die")
	Dead=True
	print "wait for a bit"
	for i in range(10):
		print 'thread is dying'
	print My_thread.is_alive()
	print "Thread is dead\n:'(\nAre you happy now?"
	print My_thread.ident		#prints the identification number of the thread
if (__name__=="__main__"):
	main()