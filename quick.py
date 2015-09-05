import random
def mergesort(B):
    result = []
    if len(B) < 2:
        return B
    mid = int(len(B)/2)
    y = mergesort(B[:mid])
    z = mergesort(B[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result							#sample input
def Search(element,B):
	for i in range(len(B)):
		if element ==B[i]:
			print i,element

B=random.sample(range(10000),1000)                    #sample input
print B

B=mergesort(B)
print B
