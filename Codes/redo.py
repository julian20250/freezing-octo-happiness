from time import clock
tea= clock()
def prime(n):
  tic= clock()
  l = [x for x in xrange(2, n+1)]
  for x in l:
    r = [z for z in xrange(2, x+1)]
    r = [x%z for z in r]
    r = r.count(0)
    if r == 1:
      pass
      # Got primes
  toc= clock()
  return toc-tic
import matplotlib.pyplot as plt
import numpy as np
k=10000 #Until which number
f = plt.figure()
d = [x for x in xrange(10, k+1, 10)]
h =[]
count=1
for x in d:
    fa = prime(x)
    h.append(fa)
    print x, "[%i/%i]"%(count, len(d)), fa
    count+=1
plt.scatter(d, h, label="Data")
plt.plot(d, h)
plt.title("Processing time")
plt.xlabel("Primes until x")
plt.ylabel("Time to finish")
plt.xlim(0,)

t= np.lib.polyval(np.lib.polyfit(d, h, 10), d)

plt.plot(d, t, label="Fit")
plt.legend(fontsize=10)
print "Total time spent: ", clock()-tea
plt.show()

#References
# http://www.pythoncentral.io/measure-time-in-python-time-time-vs-time-clock/
