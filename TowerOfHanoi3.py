def Hanoi3(nDisks,source,intermed,dest):
    if nDisks>0:
        Hanoi3(nDisks - 1, source, dest, intermed)
        print source," --> ",dest
        Hanoi3(nDisks - 1, intermed, source, dest)
n=input('number of disks??\n')
Hanoi3(n, 'A', 'B', 'C')