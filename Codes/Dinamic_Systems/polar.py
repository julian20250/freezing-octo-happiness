"""
Demo of a line plot on a polar axis.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_point(num, data, line):
  line.set_data(data[0][num], data[1][num])
  return line,

def clear_line(line):
  line.set_data([], [])
  return line,
  
G = 6.6738e-11
M = 1.9e30
mass = [3.302e23, 4.869e24, 5.9736e24]
velocity = [47.8*1000, 35.0214*1000, 29.78*1000]
mean_r = [57894376*1000, 108208930*1000, 149597870.691*1000]

L = [x*y*z for x,y,z in zip(mass, velocity, mean_r)]
K = [G*x*M for x in mass]

E = [(x*y**2)/2.-1.*z/r for x,y,z,w,r in zip(mass, velocity, K, L, mean_r)]

angle = [np.linspace(0, 2*3.141592, 240), np.linspace(0, 2*3.141592, 620), np.linspace(0, 2*3.141592, 1000)]
eccentricity = [(2*E[x]*L[x]**2/(mass[x]*K[x]**2)+1)**.5 for x in xrange(3)]
r_eccentricity = [0.20563069,0.00677323,0.01671123]
print "Theoretical eccentricity = ", eccentricity
print "Real eccentricity", r_eccentricity
a = [0.387098, 0.723327, 1]
a = [x*1.5e11 for x in a]
r_pos = [(a[x]*(1-r_eccentricity[x]**2))/(1+r_eccentricity[x]*np.cos(angle[x])) for x in xrange(3)]
pos = []

for x in xrange(3):
  pos.append((L[x]**2/(K[x]*mass[x])/(np.cos(angle[x])*eccentricity[x]+1))) # R in polar coordinates
data = []
for x in xrange(3):
  data.append(np.vstack((angle[x], pos[x])))
ani = {}
fig = plt.figure()
ax = fig.add_subplot(111, polar=True, axisbg="black")
ax.grid(True, color="w") #Comment this to unshow grid

ax.set_rmax(2e11)
strings = ["Mercury", "Venus", "Earth"]
for x in xrange(3):
  line, = ax.plot([],[], "o", linewidth=10)
  ax.plot(angle[x], pos[x], label=strings[x])
  ax.plot(angle[x], r_pos[x], label="Real "+strings[x])
  ani[str(x)+str(x)] = animation.FuncAnimation(fig, update_point, frames=len(angle[x]), fargs=(data[x], line), init_func=lambda:clear_line(line),
					interval=1, blit=False)

legend = plt.legend(frameon = 1, bbox_to_anchor=(1.1, 1.05), prop={'size':10})
for text in legend.get_texts():
    text.set_color("white")
frame = legend.get_frame()
frame.set_facecolor('black')
frame.set_edgecolor('black')
ax.xaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='y', colors='white')
plt.show()

