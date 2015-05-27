import sys
if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *
import tkFont
import matplotlib.pyplot as plt
import numpy as np

def error(st):
  bel = Tk()
  bel.wm_title("Error!")
  Label(bel, text=st, font=helv14).grid()
  bel.mainloop()
  
def entry(c):
  return c.get()


def each(of, us, ans, do):
  f = plt.figure()
  for x, y, z in zip(of, us, ans):
    plt.scatter(x, y)
    plt.text(x, y, str(z))
  xmax, xmin = max(of)+1, min(of)-1
  ymax, ymin = max(us)+1, min(us)-1
  m={}
  b={}
  count=1
  for x, y, z in zip(of[:-1], us[:-1], xrange(1, len(of))):
    for k, l in zip(of[z:], us[z:]):
      try:
	q = (1.*l-y)/(k-x)
	q = -1./q
      except ZeroDivisionError:
	q = 0
      r = ((y+l)/2.)-q*((x+k)/2.)
      if l-y == 0:
	m[str(z)+str(count)]=None
	b[str(z)+str(count)]=(x+k)/2.
      else:
	m[str(z)+str(count)]=float(q)
	b[str(z)+str(count)]=float(r) #Here
      count+=1    
  for x in m:
    if m[x]==None:
      plt.plot(np.full(50, b[x]), np.linspace(ymin, ymax))
    else:
      plt.plot(np.linspace(xmin, xmax) , [m[x]*y+b[x] for y in np.linspace(xmin, xmax)])
  plt.show()
  
def that(of, us, ans):
  f = plt.figure()  
  for x, y, z in zip(of, us, ans):
    plt.scatter(x, y)
    plt.text(x, y, str(z))
  plt.show()
  
def ash(on, peg):
  if len(on) != peg*3:
    error("You forgot to type one data.")
    raise EnvironmentError("You forgot to type one data.")
  
  mov = []
  for x in xrange(1, peg+1):
    for y in xrange(1, 4):
      mov.append(entry(on[str(x)+str(y)]))
  try:
    mov = [float(x) for x in mov]
  except ValueError:
    error("This only reads integers and floats, not strings. Start again.")
    raise ValueError("This only reads integers and floats, not strings. Start again.")      
  
  where=mov[::3] #X
  am=mov[1::3] #Y
  I=mov[2::3] #Potential
  
  if int(h.get())==1:
    for x in I:
      if x<0:
	error("If you select gravity there is no negative potential")
	raise EnvironmentError("If you select gravity there is no negative potential")  
    that(where, am, I)
  
  if int(h.get())==2:
    nit = Tk()
    nit.wm_title("Probe Charge")
    Label(nit, text="Select the Nature of the Charge", font=helv20).grid()
    bel = IntVar()
    bel.set(1)
    Radiobutton(nit, text="Positive", variable=bel, value=1, font=helv14).grid()
    Radiobutton(nit, text="Negative", variable=bel, value=-1, font=helv14).grid()
    Button(nit, text="Next >", command=lambda: each(where, am, I, bel), font=helv14).grid(sticky=E)
    nit.mainloop()
    

def eye(my, dam):
  bas = Tk()
  if int(h.get()) == 1:
    ing= "Gravity Potential"
  elif int(h.get()) == 2:
    ing= "Electromagnetic Potential"
    
  bas.wm_title("Particles")
  an = entry(my)   
  dam.destroy()
  try:
    an = int(an)
  except ValueError:
    error("No integer inserted.")
    raise ValueError("No integer inserted.")
    bas.destroy()
  if an <2:
    error("(%i) This value must be bigger or equal than 2"%an)
    raise EnvironmentError("(%i) This value must be bigger or equal than 1"%an)
    bas.destroy()
    
  Label(bas, text="Particle", font=helv20).grid(row=0, column=0)
  Label(bas, text="X", font=helv20).grid(row=0, column=1)
  Label(bas, text="Y", font=helv20).grid(row=0, column=2)
  Label(bas, text=ing, font=helv20).grid(row=0, column=3)
  d={}
  for x in xrange(1, an+1):
    Label(bas, text="Particle %i"%x, font=helv14).grid(row=x)
    d[str(x)+"1"]=Entry(bas, justify=CENTER)
    d[str(x)+"1"].grid(row=x, column=1)
    d[str(x)+"2"]=Entry(bas, justify=CENTER)
    d[str(x)+"2"].grid(row=x, column=2)
    d[str(x)+"3"]=Entry(bas, justify=CENTER)
    d[str(x)+"3"].grid(row=x, column=3)
  Button(bas, text="Cancel", command = bas.destroy, font=helv14).grid(row=x+1, column=0, sticky=W)
  Button(bas, text="Next >", command = lambda: ash(d, an), font=helv14).grid(row=x+1, column=3, sticky=E)
   
def nothing():
  pass

def girl():
  ab = Tk()
  ab.protocol("WM_DETELE_WINDOW", nothing)
  ab.wm_title("Became")
  Label(ab, text="Write the number of particles >", font=helv14).grid(row=0, sticky=W)
  eco = Entry(ab,  justify=CENTER)
  eco.grid(row=0, column=1)
  Button(ab, text="Cancel", command = ab.destroy, font=helv14).grid(sticky=W)
  Button(ab, text="Next >", command = lambda: eye(eco, ab), font=helv14).grid(row=1, column=1, sticky=E)
  ab.mainloop()
    
p = Tk()
helv14 = tkFont.Font(family='Helvetica',
    size=14, weight='bold')
helv20 = tkFont.Font(family='Helvetica',
    size=20, weight='bold')

j, k = p.winfo_screenwidth(), p.winfo_screenheight()
p.geometry("%dx%d+0+0" % (j, k))
p.wm_title("Lines of Force")
p.protocol("WM_DETELE_WINDOW", lambda: sys.exit())
menu = Menu(p)
p.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu, font=helv20)
filemenu.add_command(label="Start", command=lambda: girl(), font=helv14)
filemenu.add_command(label="Close", command=lambda: sys.exit(), font=helv14)
Label(p, text="Select Mode:", font=helv20).grid()
h = IntVar()
h.set(1)
Radiobutton(p, text="Gravity", variable=h, value=1, font=helv14).grid()
Radiobutton(p, text="Electromagnetism", variable=h, value=2, font=helv14).grid()
p.mainloop()
