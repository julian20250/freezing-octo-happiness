import matplotlib.pyplot as plt
import numpy as np
import matplotlib.collections as collections
#Energy vs Angular moment of a circular orbit
m=float(input("Insert constant m (mass) > "))
K= float(input("Insert constant K (GM) > "))
E=[]
for x in range(-1000,0):
    E.append(x)
for x in range(1,1001):
    E.append(x)
L_up=[(abs((m*K**2)/(2*x)))**.5 for x in E[:1000]]
L_do=[-x for x in L_up]
L_pa =[(abs((m*K**2)/(x)))**.5 for x in E[1000:2000]]
L_po =[-x for x in L_pa]
fig, ax = plt.subplots()
ax.plot(E[:1000],L_up,"b")
ax.plot(E[:1000],L_do,"b", label="Circular Orbits")
ax.plot(np.zeros(2),[max(L_up), min(L_do)], "r", label="Parabolic Orbits")
ax.plot([E[0],E[-1]], np.zeros(2), "g", label="Linear Orbits")
collection = collections.BrokenBarHCollection.span_where(
       E[1000:2000], ymin=0, ymax=max(L_up), where=np.array(np.zeros(1000))>-1, facecolor='red', alpha=0.15)
ax.add_collection(collection)
collection = collections.BrokenBarHCollection.span_where(
       E[1000:2000], ymin=min(L_do), ymax=0, where=np.array(np.zeros(1000))>-1, facecolor='red', alpha=0.15)
ax.add_collection(collection)
ax.text(E[1500],L_up[len(L_up)-10], "Hiperbolic Orbits")
ax.text(E[1500],L_do[len(L_do)-10], "Hiperbolic Orbits")
ax.fill_between(E[:1000],0,L_up,color="m", alpha=0.3)
ax.fill_between(E[:1000],0,L_do,color="m", alpha=0.3)
ax.text(E[500],max(L_up)/20, "Eliptical Orbits")
ax.text(E[500],min(L_do)/20, "Eliptical Orbits")
ax.set_xlabel("Energy")
ax.set_ylabel("Angular Momentum")
ax.legend()
plt.show()
print("Done")

#Energy vs Angular Moment for any orbit

