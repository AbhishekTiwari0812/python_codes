def merge(Left,Right):
  temp=[]
  while len(Left) > 0 or len(Right) > 0:
    if len(Left) > 0 and len(Right) > 0:
      if Left[0] <= Right[0]:
        temp.append(Left[0])
		del Left[0]
      else:
        temp.append(Right[0])
		del Right[0]
    elif len(Left) > 0:
      temp.append(Left[0])
	  del Left[0]
    elif len(Right) > 0:
      temp.append(Right[0])
	  del Right[0]
  return temp
def mergeSort(a):
  if len(a) <= 1: return a
  m = len(a) / 2
  LeftOfA = a[0:m]           #Creates a sub-string of consisting of 0th to m-1th element and assigns to LeftOfA
  RightOfA = a[m:]              #Creates a sub-string of a consisting of mth to last element and assigns to RightOfA
  LeftOfA = mergeSort(LeftOfA)  #Recursive call
  RightOfA = mergeSort(RightOfA)
  return merge(LeftOfA,RightOfA)
A=input('Enter the unsorted list')
print mergeSort(A)
