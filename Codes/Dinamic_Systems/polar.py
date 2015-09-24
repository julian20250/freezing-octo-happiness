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
mass = [3.302e23, 4.869e24, 5.9736e24, 6.4185e23, 1.899e27, 5.688e26, 8.68e24,1.024e26]
velocity = [47.8*1000, 35.0214*1000, 29.78*1000, 24.077*1000,13.0697*1000, 9672.4, 6.81*1000, 5.4778*1000]
mean_r = [57894376*1000, 108208930*1000, 149597870.691*1000,227939100*1000, 778412026*1000, 1.426e12, 2.8709722e12,
	  4503443661*1000]
pro=input("One/Two Body Problem? > ")

if pro!=1 and pro!=2:
  print "Invalid Data."
  raise SystemExit
if pro==2:
  mass = [1.*M*x/(M+x) for x in mass]
number = input("How Many Planets? > ")
if number>8 or number<1:
  print "Invalid Data."
  raise SystemExit

L = [x*y*z for x,y,z in zip(mass, velocity, mean_r)]

K = [G*x*M for x in mass]
E = [(x*y**2)/2.-1.*z/r for x,y,z,w,r in zip(mass, velocity, K, L, mean_r)]
angle = [np.linspace(0, 2*3.141592, 240), np.linspace(0, 2*3.141592, 620), np.linspace(0, 2*3.141592, 1000), np.linspace(0, 2*3.141592, 1881),
	 np.linspace(0, 2*3.141592, 11860), np.linspace(0, 2*3.141592, 29460), np.linspace(0, 2*3.141592, 84010), np.linspace(0, 2*3.141592, 164790)]
eccentricity = [(2*E[x]*L[x]**2/(mass[x]*K[x]**2)+1)**.5 for x in xrange(number)]
r_eccentricity = [0.20563069,0.00677323,0.01671123,0.093315, 0.04839266, 0.05415060, 0.044405,
		  0.00858587]
print "Theoretical eccentricity = ", eccentricity
print "Real eccentricity", r_eccentricity
a = [0.387098, 0.723327, 1, 1.523662, 5.204267, 9.5820172, 19.229, 30.103]
a = [x*1.5e11 for x in a]
r_pos = [(a[x]*(1-r_eccentricity[x]**2))/(1+r_eccentricity[x]*np.cos(angle[x])) for x in xrange(number)]
pos = []

for x in xrange(number):
  pos.append((L[x]**2/(K[x]*mass[x])/(np.cos(angle[x])*eccentricity[x]+1))) # R in polar coordinates
data = []
for x in xrange(number):
  data.append(np.vstack((angle[x], pos[x])))
ani = {}
fig = plt.figure()
ax = fig.add_subplot(111, polar=True, axisbg="black")
ax.grid(True, color="w") #Comment this to unshow grid
strings = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
c = [0 for x in xrange(number*2)]
for x in xrange(number):
  line, = ax.plot([],[], "ro", linewidth=10)
  c[x] = ax.plot(angle[x], pos[x], label=strings[x])
  c[x+1] = ax.plot(angle[x], r_pos[x], label="Real "+strings[x])
  ani[str(x)+str(x)] = animation.FuncAnimation(fig, update_point, frames=len(angle[x]), fargs=(data[x], line), init_func=lambda:clear_line(line),
					interval=0.1, blit=False)

legend=plt.legend(frameon = 1, bbox_to_anchor=(1.3, 1.05), prop={'size':10})


for text in legend.get_texts():
    text.set_color("white")
frame = legend.get_frame()
frame.set_facecolor('black')
frame.set_edgecolor('black')
ax.xaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='y', colors='white')
#plt.savefig("polar.png", facecolor="black")
plt.show()


