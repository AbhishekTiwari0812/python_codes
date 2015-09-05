#threading in classes
import threading 
class My_Thread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)	# this line allows the class to have an attributes of threading.Thread
										#so now we can make use of all the attributes of sub class Thread for this class
		