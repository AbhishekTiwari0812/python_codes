class point:
	'''class POINT to represent and manipulate co-ordinates''' 
	def __init__(self,abscissa,ordinate):	
		'''Crates a new point at origin'''
		self.x=abscissa
		self.y=ordinate
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def distanceFromOrigin(self):
		return (self.x**2+self.y**2)**(0.5)
	def __str__(self):								#returns only string,can use to to return components of object instance
		return  "x=" + str(self.x) + ", y=" + str(self.y)
	def halfway(self,target):	
		return point((self.x+target.x)/2,(self.y+target.y)/2)			#returns an object of instance point,mid point of self and target
		
		
		
		
def distance (P,Q):		#takes point type objects as arguments 
	diff1=P.getX()-Q.getX()
	diff2=P.getY()-Q.getY()
	return ((diff1**2)+(diff2**2))**0.5
	

P=point(8,4)		#P is a point type object
Q=point(12,6)		#and so is Q
mid=P.halfway(Q)
print P
print P.distanceFromOrigin()
print Q.distanceFromOrigin()
print 'mid is at:',mid
print distance(P,Q)