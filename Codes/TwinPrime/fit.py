import numpy as np
import matplotlib.pyplot as plt

a=np.loadtxt("data.txt", dtype="int")
b=[]
c=[]
for x in xrange(0,len(a)):
  b.append(a[x][0]) 
  c.append(x+1)

print np.lib.polyfit(b, c, 20)
