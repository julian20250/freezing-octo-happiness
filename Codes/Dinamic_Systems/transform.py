import numpy as np
import sys
from scipy import constants as ctes

print ("\n\nThis program transforms spacial coordinates to orbit parameters "
	"and viceversa. Select your option:\n\n1. Spacial to orbit.\n2. Orbit"
	" to spatial.\n")
try:
  a=input("Option > ")
except NameError:
  print "Not valid arg"
  sys.exit()
if a!=1 and a!=2:
  print "Not valid arg"
  sys.exit()
print "\n"
if a==1:
  #masa
  #m=input("Mass (m) > ")
  m=5.97e24
  mu=ctes.gravitational_constant*m	
  # vectores posicion y velocidad con sus normas
  r,v=[-6045,-3490,2500],[-3.457,6.618,2.533]
  #r.append(input("Position (x) > "))  
  #r.append(input("Position (y) > "))
  #r.append(input("Position (z) > "))
  #v.append(input("Velocity (v_x) > "))
  #v.append(input("Velocity (v_y) > "))
  #v.append(input("Velocity (v_z) > "))
  
  r=np.array(r)*1000
  v=np.array(v)*1000
  nr=np.linalg.norm(r)
  nv=np.linalg.norm(v)
  radial_v= np.dot(r,v)/nr
  print "Position Vector: ", r
  print "Velocity Vector: ", v
  h= np.cross(r,v)
  nh = np.linalg.norm(h)
  i= np.degrees(np.arccos(h[2]/nh)) #Inclination
  N= np.cross(np.array([0,0,1]), h) #Node Line
  nN = np.linalg.norm(N)
  #Ascendent Node 
  if N[1]>=0:
    Omega = np.degrees(np.arccos(N[0]/nN))
  else:
    Omega = 360-np.degrees(np.arccos(N[0]/nN))
  
  e= (1./mu)*((nv**2-(mu/nr))*r-(nr*radial_v)*v) #Eccentricity
  ne = np.linalg.norm(e)
  
  #Perigee Argument
  if e[2]>=0:
    w= np.degrees(np.arccos(np.dot(N/nN,e/ne)))
  else:
    w= 360-np.degrees(np.arccos(np.dot(N/nN,e/ne)))
  
  #True Anomaly
  if radial_v>=0:
    theta=np.degrees(np.arccos(np.dot(e/ne,r/nr)))
  else:
    theta=360-np.degrees(np.arccos(np.dot(e/ne,r/nr)))
  a= nh**2/(mu*(1-ne**2))
  print "\nSemimayor Axis = %f"%a
  print "Eccentricity = %f"%ne
  print "Inclination = %f"%i
  print "Ascendent Node = %f"%Omega
  print "Perigee Argument = %f"%w
  print "True Anomaly = %f"%theta
  
else:
  a=8793290.356282
  e=0.171665
  i= np.radians(153.249229)
  O= np.radians(255.279285)
  p= np.radians(20.136849)
  g= np.radians(28.377096)
  #a= input("Semimayor axis (a) > ")
  #e= input("Eccentricity (e) > ")
  #i = np.radians(input("inclination (i) > "))
  #O = np.radians(input("Ascendent Node Longitude (O) > "))
  #p = np.radians(input("Pergee arg (p) > "))
  #g = np.radians(input("True Anomaly (g) > "))
  #m1 = input("Mass (m1) > ")
  m1=5.97e24
  #m2 = input("Mass (m2) > ")
  r= a*(1-e**2)/(1+e*np.cos(g))
  x= r*(np.cos(p+g)*np.cos(O)-np.sin(p+g)*np.sin(O)*np.cos(i))
  y= r*(np.cos(p+g)*np.sin(O)+np.sin(p+g)*np.cos(O)*np.cos(i))
  z= r*np.sin(p+g)*np.sin(i)
  k=(ctes.gravitational_constant*m1)**.5
  mu=ctes.gravitational_constant*m1
  n=(mu/a**3)**.5
  #Eccentric Anomaly
  h=(a*mu*(1-e**2))**.5
  E =np.arccos((a-r)/(a*e))
  Edot = n/(1-e*np.cos(E))
  #print e*(mu/h)**.5*np.sin(g)
  #print a*e*np.sin(E)*Edot
  #print ((a**2*n*e*np.sin(E)/r)**2+(k*(a*(1-e**2))**.5/r**2)**2)**.5
  #v_x =x*((a**2*n*e*np.sin(E))/(r**2)) + k*(1+0)**.5*((a*(1-e**2)**.5)/r)*(-np.cos(O)*np.sin(p+g)-np.sin(O)*np.cos(i)*np.cos(p+g))
  #v_y= y*((a**2*n*e*np.sin(E))/(r**2)) + k*(1+0)**.5*((a*(1-e**2)**.5)/r)*(-np.sin(O)*np.sin(p+g)+np.cos(O)*np.cos(i)*np.cos(p+g))
  #v_z= z*((a**2*n*e*np.sin(E))/(r**2)) + k*(1+0)**.5*((a*(1-e**2)**.5)/r)*(np.sin(i)*np.cos(p+g))
  #print (v_x**2+v_y**2+v_z**2)**.5
  #v_x=(u/h)*(-np.sin(g))*
  print "\n\nPosition [x,y,z] = [%f,%f,%f]"%(x,y,z)
  #print "Velocity [v_x,v_y,v_z] = [%f,%f,%f]"%(v_x,v_y,v_z)
