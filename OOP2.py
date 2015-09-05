#fractions
def GCD(a,b):
	Min=min(a,b)
	Max=max(a,b)
	if Max%Min!=0 :
		return GCD(Min,Max%Min)
	return Min
def sameFraction(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())

class Fraction:

    def __init__(self, top, bottom):

        self.num = top        # the numerator is on top
        self.den = bottom     # the denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4)
print myfraction is yourfraction
print sameFraction(myfraction, yourfraction)