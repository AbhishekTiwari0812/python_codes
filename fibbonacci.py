
def Fibbonacci(n):
 if n<=0:
  return 1
 elif n==1:
  return 1
 t=Fibbonacci(n-1)+Fibbonacci(n-2)
 print t
Fibbonacci(5)