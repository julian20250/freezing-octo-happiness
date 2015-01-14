# Experiments With Polar Coordinates
# Test Side
#fig = plt.figure()
#ax = plt.axes(projection="3d")
#x = np.linspace(-1, 1, 100)
#y = (1-x**2)**.5
#z = np.zeros(100)

##Axis
#ax.plot(np.linspace(0, 1, 100), z, z, "-g")
#ax.plot(z, np.linspace(0, 1, 100), z, "-g")
#ax.plot(z, z, np.linspace(0, 1, 100), "-g", label = "Axis")

##Text of Axis
#ax.text(1, 0, 0, "x")
#ax.text(0, 1, 0, "y")
#ax.text(0, 0, 1, "z")


#ax.plot(x, y, z, "-r")
#ax.plot(x, -y, z, "-r", label = "Ecliptic")
#theta = np.linspace(0, np.pi, 100)
#inclination = 23+5/60. #= 23 grades, 5 minutes = Earth's inclination 
#s = inclination * np.pi / 180 # Maximun Amplitude between the mayor circles
### ???
#ax.plot(x, np.zeros(100), y, "-g")
#ax.plot(x, y, z, "-b")
#ax.plot(x, -y, -z, "-b", label = "Equator")
#ax.plot(np.zeros(100), x, y)

#ax.plot(np.zeros(2), (0,(1-s**2)**.5), (0, s))

#plt.legend(fontsize=12)
#plt.axis("off")
#plt.show()
# End Of Test Side