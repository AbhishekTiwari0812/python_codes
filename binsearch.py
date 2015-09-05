def binarysearch(A,left,right):
	global placeholder
	global element
	if left<=right:
		mid=(left+right)/2
		if element==A[mid]:
			placeholder=mid
		elif element>A[mid]:
			binarysearch(A,mid+1,right)
		else:
			binarysearch(A,left,mid-1)
A=range(100)
element=0
placeholder=-1
binarysearch(A,0,99)
print placeholder