#using Dictionary to count letters and repitions
def Histogram(s):  #s is the word
 rec=dict()          #becomes global
 for c in s:
  if c not in rec:
   rec[c]=1
  else:
   rec[c]+=1
            #returns the value if key exists otherwise creates and equalize to default
 return rec
i ='wassup'
print Histogram(i)
