import numpy as np
import sympy as sp
import sys
from scipy import constants as ctes
def tan(x):
  return sp.sin(x)/sp.cos(x)

def arctan2(y,x):
  if x>0:
    return np.arctan(y/x)
  elif y>=0 and x<0:
    return np.arctan(y/x)+np.pi
  elif y<0 and x<0:
    return np.arctan(y/x)-np.pi
  elif y<0 and x==0:
    return -np.pi/2.
  elif y>0 and x==0:
    return np.pi/2.
print ("\n\nThis program transforms spacial coordinates to orbit parameters "
	"and viceversa. Select your option	:\n\n1. Spacial to orbit.\n2. Orbit"
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
  #r,v=[-6045,-3490,2500],[-3.457,6.618,2.533]
  r,v=[],[] 
  r.append(input("Position (x) > "))  
  r.append(input("Position (y) > "))
  r.append(input("Position (z) > "))
  v.append(input("Velocity (v_x) > "))
  v.append(input("Velocity (v_y) > "))
  v.append(input("Velocity (v_z) > "))
  
  r=np.array(r)
  v=np.array(v)
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
  print nN	 
  #Ascendent Node 
  if N[1]>=0:
    Omega = np.degrees(np.arccos(N[0]/nN))
  else:
    Omega = 360-np.degrees(np.arccos(N[0]/nN))
  
  e= ((1./mu)*np.cross(v,h))-(r/nr) #Eccentricity
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
  a= 1/((2/nr)-((nv**2)/mu))
  print "\nSemimayor Axis = %f"%a
  print "Eccentricity = %f"%ne
  print "Inclination = %f"%i
  print "Ascendent Node = %f"%Omega
  print "Perigee Argument = %f"%w
  print "True Anomaly = %f"%theta
  
else:
  #a=8793290.356282
  #e=0.171665
  #i= np.radians(153.249229)
  #O= np.radians(255.279285)
  #p= np.radians(20.136849)
  #g= np.radians(28.377096)
  a= input("Semimayor axis (a) > ")
  e= input("Eccentricity (e) > ")
  i = np.radians(input("inclination (i) > "))
  O = np.radians(input("Ascendent Node Longitude (O) > "))
  p = np.radians(input("Pergee arg (p) > "))
  g = np.radians(input("True Anomaly (g) > "))
  #m1 = input("Mass (m1) > ")
  m1=5.97e24
  #m2 = input("Mass (m2) > ")
  r= a*(1-e**2)/(1+e*sp.cos(g))
  x= r*(sp.cos(p+g)*sp.cos(O)-sp.sin(p+g)*sp.sin(O)*sp.cos(i))
  y= r*(sp.cos(p+g)*sp.sin(O)+sp.sin(p+g)*sp.cos(O)*sp.cos(i))
  z= r*sp.sin(p+g)*sp.sin(i)
  k=(ctes.gravitational_constant*m1)**.5
  mu=ctes.gravitational_constant*m1
  n=(mu/a**3)**.5
  #Eccentric Anomaly
  h=(a*mu*(1-e**2))**.5
  E =2*np.arctan2(np.tan(g/2.),((1+e)+(1-e))**.5)
  r_c=a*(1-e*sp.cos(E))
  o_dot=np.array([-sp.sin(E), sp.cos(E)*(1-e**2)**.5, 0])*(mu*a)**.5/r_c
  v_x=o_dot[0]*(sp.cos(p)*sp.cos(O)-sp.sin(p)*sp.cos(i)*sp.sin(O))-o_dot[1]*(sp.sin(p)*sp.cos(O)+sp.cos(p)*sp.cos(i)*sp.sin(O))
  v_y=o_dot[0]*(sp.cos(p)*sp.sin(O)+sp.sin(p)*sp.cos(i)*sp.cos(O))+o_dot[1]*(sp.cos(p)*sp.cos(i)*sp.cos(O)-sp.sin(p)*sp.sin(O))
  v_z=o_dot[0]*(sp.sin(p)*sp.sin(i))+o_dot[1]*sp.cos(p)*sp.sin(i)
  Edot = n/(1-e*sp.cos(E))
  #print e*(mu/h)**.5*sp.sin(g)
  #print a*e*sp.sin(E)*Edot
  #print ((a**2*n*e*sp.sin(E)/r)**2+(k*(a*(1-e**2))**.5/r**2)**2)**.5
  #v_x =x*((a**2*n*e*sp.sin(E))/(r**2)) + k*(1+0)**.5*((a*(1-e**2)**.5)/r)*(-sp.cos(O)*sp.sin(p+g)-sp.sin(O)*sp.cos(i)*sp.cos(p+g))
  #v_y= y*((a**2*n*e*sp.sin(E))/(r**2)) + k*(1+0)**.5*((a*(1-e**2)**.5)/r)*(-sp.sin(O)*sp.sin(p+g)+sp.cos(O)*sp.cos(i)*sp.cos(p+g))
  #v_z= z*((a**2*n*e*sp.sin(E))/(r**2)) + k*(1+0)**.5*((a*(1-e**2)**.5)/r)*(sp.sin(i)*sp.cos(p+g))
  #print (v_x**2+v_y**2+v_z**2)**.5
  #v_x=(u/h)*(-sp.sin(g))*
  print "\n\nPosition [x,y,z] = [%f,%f,%f]"%(x,y,z)
  print "Velocity [v_x,v_y,v_z] = [%f,%f,%f]"%(v_x,v_y,v_z)

