def DoTwice(f):
	f()
	f()
def f():
 print 2*'I print twice'
def main():
 DoTwice(f)         #Function as an argument
if __name__=="__main__":
 main()