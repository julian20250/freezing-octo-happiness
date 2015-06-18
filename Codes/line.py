#References for animation: http://matplotlib.org/1.4.2/examples/animation/basic_example.html 
#http://matplotlib.org/api/animation_api.html
#http://sam-dolan.staff.shef.ac.uk/mas212/lectures/l5.pdf
#https://jakevdp.github.io/blog/2013/02/16/animating-the-lorentz-system-in-3d/
# -*- coding: utf-8 -*-

import sys
if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def remover(lan, drum, dor, kain, wist, M):
  for x in xrange(1, 3):
    M[str(x)].grid_forget()
  for x in xrange(lan, drum):
    wist[str(x)].grid_forget()
    for y in xrange(1, 4):
      kain[str(x)+str(y)].grid_forget()

def error(st):
  bel = Tk()
  bel.wm_title("Error!")
  Label(bel, text=st).grid()
  bel.mainloop()
  
def entry(c):
  return c.get()

def update_line(num, data, line, aul): #Num = xrange(Frames)
    if aul == 1:
      line.set_data(data[0][num], data[1][num])
    elif aul == 0:
      line.set_data(data[...,:num])
    return line,
  
def init(line):
  line.set_data([], [])
  return line
  
def fermata(mistic):
  fig = plt.figure(facecolor="black")
  if mistic[2]<0:
    hud="blue"
  elif mistic[2]>0:
    hud="green"
  else:
    hud="white"
  if entry(mile) ==1:
    ax= fig.add_subplot("111", axisbg="black") #Change Color
    ax.scatter(mistic[0], mistic[1], s=abs(mistic[2]*100), color=hud)
    ax.text(mistic[0], mistic[1], str(mistic[2]), color="white")

  if entry(mile)== 2:  
    plt.axis("off")
    plt.scatter(mistic[0], mistic[1], s=abs(mistic[2]*100), color=hud)
    plt.text(mistic[0], mistic[1], str(mistic[2]), color="white")
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
  #x, y, potential
  you, are, there = mistic[0], mistic[1], mistic[2] #Abandon the dependence

  for x in xrange(3):
    mistic.pop(0)    
  xi=mistic[::5]
  yi=mistic[1::5]
  pot=mistic[2::5]
  vel=mistic[3::5]
  forc=mistic[4::5]
  im={}
  here={}
  for x,y,z,a,b,m in zip(xi, yi, pot, vel, forc, xrange(1, len(xi)+1)):
    im[str(m)]=[]
    here[str(m)]=[]
    im[str(m)].append(x)
    here[str(m)].append(y)      
    xcors= x-you
    ycors= y-are
    d = ((xcors)**2+(ycors)**2)**.5
    if d < sys.float_info.epsilon*1e4:
      d = sys.float_info.epsilon*1e4
    if entry(h)==1:
      f= -1.*z*there/(d**2)
    elif entry(h) ==2:
      f= 1.*z*there/(d**2)
    if entry(thou)==0:
      fx = b[0]+ 1.*f*xcors/d
      fy = b[1] + 1.*f*ycors/d
    elif entry(thou)==1:
      if d>critic:
	fx = b[0]+ 1.*xcors*f/d
	fy = b[1] + 1.*ycors*f/d
      else:
	fx= np.random.randint(-200,200) 
	fy=np.random.randint(-200,200)
    if entry(giv)==1:
      norm = ((fx**2+fy**2)**.5)*10 #Last item (10) makes it smaller to more steps
      if norm==0:
	norm=1
      im[str(m)].append(x+1.*fx/norm)
      here[str(m)].append(y+1.*fy/norm)
      soda=1000
    elif entry(giv)==2:
      try:
	acx = fx/abs(z)
	acy= fy/abs(z)
      except ZeroDivisionError:
	acx=0
	acy=0
      soda=1000
      time = np.linspace(.01, 1, soda)	
      im[str(m)].append(x+a[0]*.01+(1.*acx*.01**2)/2)
      here[str(m)].append(y+a[1]*.01+(1.*acy*.01**2)/2)
    count=0
    while count<soda:
      x=im[str(m)][-1]
      y=here[str(m)][-1]
      xcors= x-you
      ycors= y-are
      d = ((xcors)**2+(ycors)**2)**.5
      if d < sys.float_info.epsilon*1e4:
	d = sys.float_info.epsilon*1e4
      if entry(h)==1:
	f= -1.*z*there/(d**2)
      elif entry(h) ==2:
	f= 1.*z*there/(d**2)
      if entry(thou)==0:
	fx = b[0]+ 1.*xcors*f/d
	fy = b[1] + 1.*ycors*f/d
      elif entry(thou)==1:
	if d>critic:
	  fx = b[0]+ 1.*xcors*f/d
	  fy = b[1] + 1.*ycors*f/d
	else:
	  fx= np.random.randint(-200,200) 
	  fy=np.random.randint(-200,200)
      if entry(giv)==1:
	norm = ((fx**2+fy**2)**.5)*10 #Last item (10) makes it smaller to more steps
	if norm==0:
	  norm=1
	im[str(m)].append(x+1.*fx/norm)
	here[str(m)].append(y+1.*fy/norm)
      elif entry(giv)==2:
	try:
	  acx = fx/abs(z)
	  acy= fy/abs(z)
	except ZeroDivisionError or Runtime:
	  acx=0
	  acy=0
	im[str(m)].append(x+a[0]*time[count]+(1.*acx*time[count]**2)/2)
	here[str(m)].append(y+a[1]*time[count]+(1.*acy*time[count]**2)/2)
      count+=1
  
  if entry(mile)==1:
    count=0
    for x in xrange(1, len(xi)+1):
      if pot[x-1]<0:
	hud="blue"
      elif pot[x-1]>0:
	hud="green"
      else:
	hud="white"
      ax.plot(im[str(x)], here[str(x)], color=hud)
      count+=1
  

  elif entry(mile)==2:
    puss = {}
    count=0
    for x in xrange(1, len(xi)+1):
      puss[str(count)]=np.vstack((np.array(im[str(x)]), np.array(here[str(x)])))
      count+=1
    line_ani={}
    for x in xrange(count):
      if pot[x]<0:
	hud="b"
      elif pot[x]>0:
	hud="g"
      else:
	hud="w"      
      if entry(rest) == 1:
	l2,= plt.plot([],[], hud+"-")
	line_ani[str(x)+str(x)]= animation.FuncAnimation(fig, update_line, frames=soda+2, fargs=(puss[str(x)], l2, 0),
						interval=10, blit=False) #Interval = how it takes
      l, = plt.plot([], [], hud+"o")
      line_ani[str(x)]= animation.FuncAnimation(fig, update_line, frames=soda+2, fargs=(puss[str(x)], l, 1), init_func= lambda: init(l),
						interval=10, blit=False) #Interval = how it takes
  plt.show()    
  p.mainloop()
  
def each(of, us, ans, do, last): #where, am, I
  fig = plt.figure(facecolor="black")
  xmax, xmin = max(of)+1, min(of)-1
  ymax, ymin = max(us)+1, min(us)-1
  if entry(mile) ==1:
    ax= fig.add_subplot("111", axisbg="black") #Change Color
    for x, y, z in zip(of, us, ans):
      if z<0:
	hud = "blue"
      elif z>0:
	hud= "green"
      else:
	hud="white"
      ax.scatter(x, y, s=abs(z*100), color=hud)
      ax.text(x, y, str(z), color="white")
    ax.axes.get_xaxis().set_visible(False) #Comment this if
    ax.axes.get_yaxis().set_visible(False) #you want to see the axis
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([ymin, ymax])
  if entry(mile) ==2:
    plt.axis("off") #Comment this if you want to see the axis
    for x, y, z in zip(of, us, ans):
      if z<0:
	hud = "blue"
      elif z>0:
	hud = "green"
      else:
	hud = "white"
      plt.scatter(x, y, s= abs(z*100), color=hud)
      plt.text(x, y, str(z), color="white")

  #Those equipotential lines
  #beh =1.*(ymax-ymin)/(xmax-xmin)
  #ind = ymax-beh*xmax
  #mist = np.vstack((np.linspace(xmin, xmax, 20), beh*np.linspace(xmin, xmax, 20)+ind))
  #You are here
  m={}
  b={}
  birth = {}
  calm = {}
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
  count = 1
  for x in m:
    if m[x]==None:      
      birth[str(count)]=np.full(20, b[x])
      calm[str(count)]=np.linspace(ymin, ymax, 20)
      #ax.plot(np.full(50, b[x]), np.linspace(ymin, ymax))
    else:
      birth[str(count)]=np.linspace(xmin, xmax, 20)
      calm[str(count)]=[m[x]*y+b[x] for y in np.linspace(xmin, xmax, 20)]
      #ax.plot(np.linspace(xmin, xmax) , [m[x]*y+b[x] for y in np.linspace(xmin, xmax)])
    count+=1
  les = do
  sorrow = {}
  omin = {}
  for a in xrange(1, len(calm)+1):
      sorrow[str(a)]=[]
      omin[str(a)]=[]
      zem = 0
      for x, y in zip(birth[str(a)], calm[str(a)]):		
	sorrow[str(a)].append([]) 
	sorrow[str(a)][zem].append(x)
	omin[str(a)].append([])
	omin[str(a)][zem].append(y)
	Fx=[]
	Fy=[]
	for q, w, e in zip(of, us, ans):
	  xcords = x-q 
	  ycords = y-w
	  d = ((xcords)**2+(ycords)**2)**.5
	  if d < sys.float_info.epsilon*1e4:
	    d = sys.float_info.epsilon*1e4
	  f = 1.*les*e/(d**2)
	  Fx.append(1.*xcords*f/d)
	  Fy.append(1.*ycords*f/d)
	if entry(thou)==0:
	  xf=sum(Fx)
	  yf=sum(Fy)
	elif entry(thou)==1:
	  if d>critic:
	    xf=sum(Fx)
	    yf=sum(Fy)
	  else:
	    xf=np.random.randint(-200, 200)
	    yf=np.random.randint(-200, 200)
	if entry(giv)==1:
	  norm = ((xf**2+yf**2)**.5)*10 #Last item (10) makes it smaller to more steps
	  sorrow[str(a)][zem].append(x+1.*xf/norm)
	  omin[str(a)][zem].append(y+1.*yf/norm)
	  soda = 100	
	elif entry(giv)==2:
	  sorrow[str(a)][zem].append(x+(xf*.01**2)/2.)
	  omin[str(a)][zem].append(y+(yf*.01**2)/2.)
	  soda = 1000 
	  time = np.linspace(.01, 5, soda) #5 = until which time (seconds)
	count=0
	while count<soda: #How many steps
	  x=sorrow[str(a)][zem][-1]
	  y=omin[str(a)][zem][-1]
	  Fx=[]
	  Fy=[]
	  for q, w, e in zip(of, us, ans):
	    xcords = x-q 
	    ycords = y-w
	    d = ((xcords)**2+(ycords)**2)**.5	
	    if d < sys.float_info.epsilon*1e4:
	      d = sys.float_info.epsilon*1e4
	    f = 1.*les*e/(d**2)
	    Fx.append(1.*xcords*f/d)
	    Fy.append(1.*ycords*f/d)
	  if entry(thou)==0:
	    xf=sum(Fx)
	    yf=sum(Fy)
	  elif entry(thou)==1:
	    if d>critic:
	      xf=sum(Fx)
	      yf=sum(Fy)
	    else:
	      xf=np.random.randint(-200, 200)
	      yf=np.random.randint(-200, 200)
	  if entry(giv)==1:	
	    norm = ((xf**2+yf**2)**.5)*10 #Last item (10) makes it smaller to more steps
	    if norm==0:
	      norm=1
	    sorrow[str(a)][zem].append(x+1.*xf/norm)
	    omin[str(a)][zem].append(y+1.*yf/norm)
	  elif entry(giv)==2:
	    sorrow[str(a)][zem].append(x+(xf*time[count]**2)/2.)
	    omin[str(a)][zem].append(y+(yf*time[count]**2)/2.)
	  count +=1
	zem +=1
  if les == 1:
    hud = "g"
  if les == -1:
    hud= "b"
  if entry(mile) ==1:
    for x in xrange(1, len(calm)+1):
      for y in xrange(len(birth[str(x)])):
	ax.plot(sorrow[str(x)][y], omin[str(x)][y], hud)  


  if entry(mile) ==2:
    puss = {}
    count=0
    for x in xrange(1, len(calm)+1):
      for y in xrange(len(birth[str(x)])):
	puss[str(count)]=np.vstack((np.array(sorrow[str(x)][y]), np.array(omin[str(x)][y])))
	count+=1
    line_ani={}
    for x in xrange(count):
      if entry(rest) == 1:
	l2,= plt.plot([],[], hud+"-")
	line_ani[str(x)+str(x)]= animation.FuncAnimation(fig, update_line, frames=soda+2, fargs=(puss[str(x)], l2, 0),
						interval=10, blit=False) #Interval = how it takes
      l, = plt.plot([], [], hud+"o")
      line_ani[str(x)]= animation.FuncAnimation(fig, update_line, frames=soda+2, fargs=(puss[str(x)], l, 1), init_func= lambda: init(l),
						interval=10, blit=False) #Interval = how it takes

  plt.show()
  p.mainloop()
    
    #If you want to save the animation discomment the next lines, also make sure that you have installed ffmpeg, 
    #which is needed to save the animation. You also should want to make a bigger interval to have a long video.
    #mess = []
    #for x in xrange(count):
      #mess.append(line_ani[str(x)])
    #mess[0].save("a.mp4", extra_anim=mess[1:])
    
def ash(on, peg, daa, plz, nit, seer):
  if len(on) != (peg-plz)*3:
    error("You forgot to type one data.")
    raise EnvironmentError("You forgot to type one data.")
  
  mov = []
  for x in xrange(plz, peg):
    for y in xrange(1, 4):
      if daa==1:
	mov.append(entry(on[str(x)+str(y)]))
      elif daa==2:
	mov.append(on[str(x)+str(y)])
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
    each(where, am, I, -1, seer+3)
  
  if int(h.get())==2:
    Label(nit, text="Select the Nature of the Charge").grid(row=seer)
    Button(nit, text="Positive", command=lambda: each(where, am, I, 1, seer+3)).grid(row=seer+1, column=1)
    Button(nit, text="Negative", command=lambda: each(where, am, I, -1, seer+3)).grid(row=seer+1, column=2)
    

def eye(my, ore, bas, day):
  an = entry(my)  
  try:
      an = int(an)
  except ValueError:
    error("No integer inserted.")
    raise ValueError("No integer inserted.")

  if int(h.get()) == 1:
    ing= "Gravity Potential"
  elif int(h.get()) == 2:
    ing= "Electromagnetic Potential" 
  if an <2 and entry(free)==0:
    error("(%i) This value must be bigger or equal than 2"%an)
    raise EnvironmentError("(%i) This value must be bigger or equal than 2"%an)
  if entry(free) == 0:	
    if ore == 1:
      Label(bas, text="Particle").grid(row=day, column=0)
      Label(bas, text="X").grid(row=day, column=1)
      Label(bas, text="Y").grid(row=day, column=2)
      Label(bas, text=ing).grid(row=day, column=3)
      d={}
      labels={}
      count=1
      for x in xrange(day+1, day+an+1):
	labels[str(x)]=Label(bas, text="Particle %i"%count)
	labels[str(x)].grid(row=x)
	d[str(x)+"1"]=Entry(bas, justify=CENTER)
	d[str(x)+"1"].grid(row=x, column=1)
	d[str(x)+"2"]=Entry(bas, justify=CENTER)
	d[str(x)+"2"].grid(row=x, column=2)
	d[str(x)+"3"]=Entry(bas, justify=CENTER)
	d[str(x)+"3"].grid(row=x, column=3)
	count+=1
      B={}
      B["2"]=Button(bas, text="Next >", command = lambda: ash(d, day+an+1, ore, day+1, bas, x+2))
      B["2"].grid(row=x+1, column=3, sticky=E)
      B["1"]=Button(bas, text="Clear", command = lambda: remover(day+1, day+an+1, bas, d, labels, B))
      B["1"].grid(row=x+1, column=0, sticky=W)

    elif ore==2:
      d={}
      for x in xrange(day+1, day+an+1):
	d[str(x)+"1"]=np.random.randint(-11,11) #xmin and xmax
	d[str(x)+"2"]=np.random.randint(-11,11) #ymin and ymax
	if int(h.get())==1:
	  d[str(x)+"3"]=np.random.randint(11) #max gravity potential
	elif int(h.get())==2:
	  d[str(x)+"3"]=np.random.randint(-11,11) #min and max electromagnetic potential
      ash(d, day+an+1, ore, day+1, bas, day+1)

  elif entry(free) == 1:
    if an<1:
      error("(%i) This value must be bigger or equal than 1"%an)
      raise EnvironmentError("(%i) This value must be bigger or equal than 1"%an)
    
    l={}
    Label(bas, text="Let me know some things about the main particle").grid(row=day, column=0, columnspan=3)
    Label(bas, text="X").grid(row=day+1, column=0)
    Label(bas, text="Y").grid(row=day+1, column=1)
    Label(bas, text=ing).grid(row=day+1, column=2) #You are Here
    l["00"] = Entry(bas, justify=CENTER)
    l["01"] = Entry(bas, justify=CENTER)
    l["02"] = Entry(bas, justify=CENTER)
    l["00"].grid(row=day+2, column=0)
    l["01"].grid(row=day+2, column=1)
    l["02"].grid(row=day+2, column=2)
    if ore ==1:
      Label(bas, text="Now tell me about the probe particles").grid(row=day+3, column=0, columnspan=3)
      Label(bas, text="Xi").grid(row=day+4, column=0)
      Label(bas, text="Yi").grid(row=day+4, column=1)
      Label(bas, text=ing).grid(row=day+4, column=2)
      Label(bas, text="Velocity (Vx, Vy)").grid(row= day+4, column=3)
      Label(bas, text="External force (Fx, Fy)").grid(row=day+4, column=4)
      count=1
      for x in xrange(day+5, day+an+5):
	l[str(count)+"0"]= Entry(bas, justify=CENTER)
	l[str(count)+"0"].grid(row=x, column=0)
	l[str(count)+"1"]= Entry(bas, justify=CENTER)
	l[str(count)+"1"].grid(row=x, column=1)
	l[str(count)+"2"]= Entry(bas, justify=CENTER)
	l[str(count)+"2"].grid(row=x, column=2)
	l[str(count)+"3"]= Entry(bas, justify=CENTER)
	l[str(count)+"3"].grid(row=x, column=3)
	l[str(count)+"4"]= Entry(bas, justify=CENTER)
	l[str(count)+"4"].grid(row=x, column=4)
	count+=1
      Button(bas, text="Next >", command= lambda: eve(l, an)).grid(row=x+1, column=4, sticky=E)
    
    elif ore == 2:
      count=1
      for x in xrange(day+5, day+an+5):
	l[str(count)+"0"] = np.random.randint(-11, 11)
	l[str(count)+"1"] = np.random.randint(-11, 11)	
	if int(h.get())==1:
	  l[str(count)+"2"]=np.random.randint(11) #max gravity potential
	elif int(h.get())==2:
	  l[str(count)+"2"]=np.random.randint(-11,11) #min and max electromagnetic potential
	l[str(count)+"3"]=[np.random.randint(-11,11), np.random.randint(-11,11)]
	l[str(count)+"4"]=[np.random.randint(-11,11), np.random.randint(-11,11)]
	count+=1
      Button(bas, text="Next", command= lambda: eve(l, an)).grid(row=day+3, column=3, sticky=E)

def eve(ost, al):
  tain=[]
  for x in xrange(3):
    tain.append(float(entry(ost["0"+str(x)])))
  if entry(moz)==1:
    for x in xrange(1, al+1):
      for y in xrange(5):
	if y!=3 and y!=4:
	  try:
	    tain.append(float(entry(ost[str(x)+str(y)]))) #You Are Here
	  except NameError:
	    error("You forgot to type one data")
	    raise NameError("You forgot to type one data")
	  except ValueError:
	    error("One of the data is invalid")
	    raise ValueError("One of the data is invalid")
	else:
	  yur = entry(ost[str(x)+str(y)]).split(",")
	  yur= [float(m) for m in yur]
	  tain.append(yur)
  elif entry(moz)==2:
    for x in xrange(1, al+1):
      for y in xrange(5):
	tain.append(ost[str(x)+str(y)])
  fermata(tain)
      
def girl(ab):
  Label(ab, text="Write the number of particles >").grid(row=art, column=1, sticky=W)
  eco = Entry(ab,  justify=CENTER)
  eco.grid(row=art, column=2)
  Button(ab, text="Next >", command = lambda: eye(eco, entry(moz), ab, art+3)).grid(row=art+1, column=2, sticky=E)

def Help():
  yer = Tk()
  yer.wm_title("Help")
  text = Text(yer, width=80, heigh=30, wrap=WORD)
  scroll= Scrollbar(yer, command= text.yview)
  text.tag_configure("big",font= ("Verdana", 14, "bold"))
  text.tag_configure("normal", justify="left", font= ("Verdana", 12))
  text.insert(INSERT, "You can scroll down with the mouse wheel.\n", "normal")
  text.insert(INSERT, "Static", "big")
  text.insert(INSERT, "\nThis is the basic option of the program, in this way the lines of force are"
	      " represented in a static image. Since the program makes the calculations first, you can make as many images"
	      " as you want.\n\n", "normal")
  text.insert(INSERT, "Dinamic", "big")
  text.insert(INSERT, "\nThis option is similar to 'Static', but in this is displayed the particles moving"
	      " through the lines of force. This modality takes more proccessing that 'Static' because"
	      " it must be reloading each certain time. For this reason is recommendable to close the last animation"
	      " before opening a new one.\n\n", "normal")
  text.insert(INSERT, "Restart", "big")
  text.insert(INSERT, "\nThis program is structured with Tkinter, so is like a matrix. When you use manual mode (where you"
	      " can put the coordinates and potential) the program puts the entry widgets, but if you alternate this"
	      " option with 'Random' you will see that are some lines that are not hidden. Then, pushing 'Restart' button"
	      " will make that the program run again.\nThis is also useful when the window is full of properties after"
	      " doing some options. The close button has the same purpose.\n\n", "normal")
  text.insert(INSERT, "Trayectories", "big")
  text.insert(INSERT, "\nThis option is valid only to 'Dinamic' mode. Enable this to show the trayectories that"
	      " describe the particle moving through the lines of force. This consumes twice times the proccesing"
	      " that would take this option disabled because is like doing two animations separated. Also, is more"
	      " charge for the matplotlib window.\n\n", "normal")
  text.insert(INSERT, "Mechanic", "big")
  text.insert(INSERT, "\nThis mode is more demmanding than the lines of force because it requires a lot of steps to avoid"
	      " loosing presition. In this mode the force equals acceleration, so, via cinematic equations, the position of"
	      " the probe particle is calculed as x = xi + (at^2)/2\n\n", "normal")
  text.insert(INSERT, "Probe Particle", "big")
  text.insert(INSERT, "\nIn this mode you can specify the position and the potential of a main particle. This particle"
	      " does not moves. Also, depending if you select 'Manual' or 'Random' mode you can put probe particles with the"
	      " characteristics you want. If you select 'Random' the characteristics are filled by random, but if you"
	      " select 'Manual' you can fill them.\nAs velocity and force are vectors, to insert the value you must"
	      " insert the entry like this: '2,3' in velocity will give to the particle a velocity of 2 units per frame "
	      " along the x axis and 3 along the y axis.\n\n", "normal")
  text.insert(INSERT, "Funny", "big")
  text.insert(INSERT, "\nActivating this option will allow that in a predefined distance around a particle the force induced"
	      " by it will be random in magnitude and direction. You can change this distance going to the last lines code of this "
	      " program, where is alocated a variable called 'critic', change it to the value that you want. Just for fun!\n\n", "normal")
  text.pack(side=LEFT)
  scroll.pack(side=RIGHT, fill=Y)
  yer.mainloop()
  
while True:    
  p = Tk()
  menu = Menu(p)
  menu.add_command(label="Restart", command= lambda: p.destroy())
  menu.add_command(label="Help", command= Help)
  menu.add_command(label="Exit", command = lambda: sys.exit(0))
  p.wm_title("Lines of Force")
  p.protocol("WM_DETELE_WINDOW", lambda: sys.exit(0))
  Label(p, text="Select Mode:").grid(column=1)
  h = IntVar()
  h.set(1)
  Radiobutton(p, text="Gravity", variable=h, value=1).grid(column=1)
  Radiobutton(p, text="Electromagnetism", variable=h, value=2).grid(column=1)
  Label(p, text="").grid(column=1)
  Label(p, text="Select Graphic's Mode:").grid(row=4, column=1)
  mile= IntVar()
  mile.set(1)
  Radiobutton(p, text="Static", variable=mile, value=1).grid(row=5, column=1)
  Radiobutton(p, text="Dinamic", variable=mile, value=2).grid(row=6, column=1)
  moz = IntVar()
  moz.set(1)
  Label(p, text = "Select Particle Generator:").grid(row=0, column=2)
  Radiobutton(p, text="Manual", variable=moz, value=1).grid(row=1, column=2)
  Radiobutton(p, text="Random", variable=moz, value=2).grid(row=2, column=2)
  giv = IntVar()
  giv.set(1)
  Label(p, text= "Select Lines:").grid(row=4, column=2)
  Radiobutton(p, text="Force", variable=giv, value=1).grid(row=5, column=2)
  Radiobutton(p, text="Mechanic", variable=giv, value=2).grid(row=6, column=2)
  Label(p, text="Options:").grid(row=0, column=3)
  rest= IntVar()
  check = Checkbutton(p, text="Enable trayectories (only dinamic mode)", variable=rest, onvalue=1, offvalue=0)
  check.grid(row=1, column=3)
  free = IntVar()
  sol = Checkbutton(p, text="Enable probe particle mode (appreciable with mechanic mode)", variable=free, onvalue=1, offvalue=0)
  sol.grid(row=2, column=3)
  Button(p, text="Start", command = lambda: girl(p)).grid(sticky=E, column=2)  
  thou = IntVar()
  sen = Checkbutton(p, text="Enable funny mode", variable=thou, onvalue=1, offvalue=0)
  sen.grid(row=3, column=3)
  art = 9
  critic=.5
  p.config(menu=menu)
  p.mainloop()	
