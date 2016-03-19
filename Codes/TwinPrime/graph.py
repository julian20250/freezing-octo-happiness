from numpy import loadtxt as ldtxt
import matplotlib.pyplot as plt
import sys

a=ldtxt("data.txt", dtype="int")
count=1
for x in xrange(0,len(a)):
  plt.scatter(a[x][0], x+1, s=0.01)
  print "\rPlotted %i pairs"%count,
  count+=1
frame1 = plt.gca()
#frame1.axes.get_yaxis().set_visible(False)
plt.show()  

