#References for animation: http://matplotlib.org/1.4.2/examples/animation/basic_example.html 
#http://matplotlib.org/api/animation_api.html
#http://sam-dolan.staff.shef.ac.uk/mas212/lectures/l5.pdf
#https://jakevdp.github.io/blog/2013/02/16/animating-the-lorentz-system-in-3d/
import sys
if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *
import tkFont
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.lines import Line2D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

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
    ax.set_xlim([xmin, xmax]) #Change this to 
    ax.set_ylim([ymin, ymax]) #set limits
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
    plt.xlim(xmin, xmax) #Change this to 
    plt.ylim(ymin, ymax) #set limits
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
	xf=sum(Fx)
	yf=sum(Fy)
	norm = ((xf**2+yf**2)**.5)*10 #Last item (10) makes it smaller to more steps
	sorrow[str(a)][zem].append(x+1.*xf/norm)
	omin[str(a)][zem].append(y+1.*yf/norm)
	count=0
	while count<100: #How many steps
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
	  xf=sum(Fx)
	  yf=sum(Fy)
	  norm = ((xf**2+yf**2)**.5)*10 #Last item (10) makes it smaller to more steps
	  sorrow[str(a)][zem].append(x+1.*xf/norm)
	  omin[str(a)][zem].append(y+1.*yf/norm)
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
	line_ani[str(x)+str(x)]= animation.FuncAnimation(fig, update_line, frames=102, fargs=(puss[str(x)], l2, 0),
						interval=10, blit=False) #Interval = how it takes
      l, = plt.plot([], [], hud+"o")
      line_ani[str(x)]= animation.FuncAnimation(fig, update_line, frames=102, fargs=(puss[str(x)], l, 1), init_func= lambda: init(l),
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
  if ore == 1:
    if int(h.get()) == 1:
      ing= "Gravity Potential"
    elif int(h.get()) == 2:
      ing= "Electromagnetic Potential" 
    if an <2:
      error("(%i) This value must be bigger or equal than 2"%an)
      raise EnvironmentError("(%i) This value must be bigger or equal than 1"%an)
      
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
def nothing():
  pass

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
	      " as you want. Also, the images are incorporated in the main window.\n\n", "normal")
  text.insert(INSERT, "Dinamic", "big")
  text.insert(INSERT, "\nThis option is similar to 'Static', but in this is displayed the particles moving"
	      " through the lines of force. This modality takes more proccessing that 'Static' because"
	      " it must be reloading each certain time. For this reason is recommendable to close the last animation"
	      " before opening a new one.\nClose an animation is possible without closing all the program because"
	      " the animation is opened in a normal widget from matplotlib. If the animation was opened in the main window"
	      " , this window can restrict the frames of the animation, putting a limit to it. That is why the animation is"
	      " not in the same window as 'Static' mode.\n\n", "normal")
  text.insert(INSERT, "Restart", "big")
  text.insert(INSERT, "\nThis program is structured with Tkinter, so is like a matrix. When you use manual mode (where you"
	      " can put the coordinates and potential) the program puts the entry widgets, but if you alternate this"
	      " option with 'Random' you will see that are some lines that are not hidden. Then, pushing 'Restart' button"
	      " will make that the program run again.\nThis is also useful when the window is full of properties after"
	      " doing some options. The close button has the same purpose.\n\n", "normal")
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
  Label(p, text="Options:").grid(row=0, column=3)
  rest= IntVar()
  check = Checkbutton(p, text="Enable trayectories (only dinamic mode)", variable=rest, onvalue=1, offvalue=0)
  check.grid(row=1, column=3)
  Button(p, text="Start", command = lambda: girl(p)).grid(sticky=E, column=2)  
  art = 9
  p.config(menu=menu)
  p.mainloop()	
