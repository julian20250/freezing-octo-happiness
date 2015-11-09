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
  m=input("Mass (m) > ")
  mu=ctes.gravitational_constant*m	
  # vectores posicion y velocidad con sus normas
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
  print "Position Vector: ", r
  print "Velocity Vector: ", v
  #momento angular
  h=np.cross(r,v)
  nh=np.linalg.norm(h)
  #Energia
  E=((nv**2)/2.0)-(mu/nr)
  #Semieje mayor
  a=-mu/(2.0*E)
  #Tipo de orbita
  if E < 0:
    print ("Closed Orbit")
    if E == a:
      print ("Circular Orbit")
    else:
      print ("Eliptic Orbit")
  #Excentricidad
  e=np.cross(v,h)/mu-r*(1/nr)
  ne=np.linalg.norm(e)
  #Vector unitario z
  k=np.array([0,0,1])
  #Inclinacion
  i=np.degrees(np.arccos(np.dot(np.cross(r,v),k)/nh))
  #vector que apunta en la direccion de la linea del nodo ascendente
  n=np.cross(k,h)
  nn=np.linalg.norm(n)
  #Omega=np.array([np.arccos(n[0]*(1/nn)),np.arcsin(n[1]*(1/nn))])
  #Omegan=np.linalg.norm(Omega)
  #Nodo ascendente
  Omega=np.degrees(np.arccos(n[0]*(1/nn)))
  #Argumento del perigeo
  if np.dot(e,k)>0:
    omega=np.degrees(np.arccos(np.dot(n,e)/(nn*ne)))
  else:
    print ("Cuadrant Correction done for: omega")
    omega=0.0
  #Anomalia verdadera
  if np.dot(r,v)>0:
    teta=np.degrees(np.arccos(np.dot(r,e)/(nr*ne)))
  else: 
    print ("Cuadrant Correction done for: theta")
    teta=0.0
  #Anomalia excentrica
  Ex=np.degrees(2*np.arctan(teta/2)/np.sqrt((1+ne)/(1-ne)))

  print "Semimayor Axis (a): ",a
  print "Eccentricity (ne): ", ne
  print "Inclination (i): ", i
  print "Perigee arg (omega): ",omega
  print "Energy (E): ", E
  print "Ascendent Node Longitude (Omega): ", Omega
  print "True Anomaly (teta): ",teta
  print "Eccentric Anomaly (Ex): ",Ex

else:
  a= input("Semimayor axis (a) > ")
  e= input("Eccentricity (e) > ")
  i = input("inclination (i) > ")
  O = input("Ascendent Node Longitude (O) > ")
  p = input("Pergee arg (p) > ")
  g = input("True Anomaly (g) > ")	
  m1 = input("Mass (m1) > ")
  m2 = input("Mass (m2) > ")
  i=i*np.pi/180.
  O=O*np.pi/180.
  p=p*np.pi/180.
  g=g*np.pi/180.
  r= a*(1-e**2)/(1+e*np.cos(g))
  x= r*(np.cos(p+g)*np.cos(O)-np.sin(p+g)*np.sin(O)*np.cos(i))
  y= r*(np.cos(p+g)*np.sin(O)+np.sin(p+g)*np.cos(O)*np.cos(i))
  z= r*np.sin(p+g)*np.sin(i)
  k=(ctes.gravitational_constant*m1)**.5
  mu=ctes.gravitational_constant*m1
  n=(mu/a**3)**.5
  #Eccentric Anomaly
  E =np.arccos((a-r)/(a*e))
  v_x =x*((a**2*n*e*np.sin(E))/r**2) + k*(1+(m2/m1))**.5*((a*(1-e**2)**.5)/r)*(-np.cos(O)*np.sin(p+g)-np.sin(O)*np.cos(i)*np.cos(p+g))
  v_y= y*((a**2*n*e*np.sin(E))/r**2) + k*(1+(m2/m1))**.5*((a*(1-e**2)**.5)/r)*(-np.sin(O)*np.sin(p+g)+np.cos(O)*np.cos(i)*np.cos(p+g))
  v_z= z*((a**2*n*e*np.sin(E))/r**2) + k*(1+(m2/m1))**.5*((a*(1-e**2)**.5)/r)*(np.sin(i)*np.cos(p+g))
  print "\n\nPosition [x,y,z] = [%f,%f,%f]"%(x,y,z)
  print "Velocity [v_x,v_y,v_z] = [%f,%f,%f]"%(v_x,v_y,v_z)
