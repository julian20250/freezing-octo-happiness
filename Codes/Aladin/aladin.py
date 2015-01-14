# It will take some time to run the script the first time...
import numpy as np
import os
import matplotlib.pyplot as plt
import webbrowser
import sys
if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *
from mpl_toolkits.mplot3d import Axes3D
try:
  import odf.opendocument
except (ImportError):
  print("Sorry, but I couldn't import the libraries. Maybe you don't have installed odfpy's library, to get it go to this link https://pypi.python.org/packages/source/o/odfpy/odfpy-0.9.6.tar.gz"
    " \n\n If you have it already installed, you have to execute this script with the same permissions which it was installed.")
  sys.exit()
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg  
from odf.table import *
from odf.text import P
location = os.getcwd()
#How to use the next class here http://www.marco83.com/work/173/read-an-ods-file-with-python-and-odfpy/
#Marco Conti 2011
class ODSReader:
 
        # loads the file
        def __init__(self, file):
                self.doc = odf.opendocument.load(file)
                self.SHEETS = {}
                for sheet in self.doc.spreadsheet.getElementsByType(Table):
                        self.readSheet(sheet)
       
 
        # reads a sheet in the sheet dictionary, storing each sheet as an array (rows) of arrays (columns)
        def readSheet(self, sheet):
                name = sheet.getAttribute("name")
                rows = sheet.getElementsByType(TableRow)
                arrRows = []
               
                # for each row
                for row in rows:
                        row_comment = ""
                        arrCells = []
                        cells = row.getElementsByType(TableCell)
                       
                        # for each cell
                        for cell in cells:
                                # repeated value?
                                repeat = cell.getAttribute("numbercolumnsrepeated")
                                if(not repeat):
                                        repeat = 1
                                       
                                ps = cell.getElementsByType(P)
                                textContent = ""
                                                               
                                # for each text/text:span node
                                for p in ps:
                                        for n in p.childNodes:
                                                if (n.nodeType == 1 and n.tagName == "text:span"):
                                                        for c in n.childNodes:
                                                                if (c.nodeType == 3):
                                                                        textContent = textContent + unicode(c.data)
                                                       
                                                if (n.nodeType == 3):
                                                        textContent = textContent + unicode(n.data)
                                       
                                if(textContent):
                                        if(textContent[0] != "#"): # ignore comments cells
                                                for rr in range(int(repeat)): # repeated?
                                                        arrCells.append(textContent)
                                        else:
                                                row_comment = row_comment + textContent + " ";
                                else:
                                        for rr in range(int(repeat)):
                                                arrCells.append("")
 
                        # if row contained something
                        if(len(arrCells)):
                                arrRows.append(arrCells)
                               
                        #else:
                        #       print "Empty or commented row (", row_comment, ")"
               
                self.SHEETS[name] = arrRows
               
        # returns a sheet as an array (rows) of arrays (columns)
        def getSheet(self, name):
                return self.SHEETS[name]
# End of CopyRight

var = ODSReader("M13.ods")
table = var.getSheet("Hoja1")
head = table.pop(0)
original = {}
for x in head:
    original[x]=[]

for x in table:
  count = 0
  for y in x:
    original[head[count]].append(y)
    count +=1

# Making the data readable
readable = dict(original)
for x in xrange(4, 15):
  for y in readable[head[x]]:
    if type(y) == unicode:
      ind = readable[head[x]].index(y)
      readable[head[x]].remove(y)
      readable[head[x]].insert(ind, float(y))      

for x in xrange(2, 4):
  for y in readable[head[x]]:
      road = y.split(" ")
      road = [float(i) for i in road]
      cross = road[0]+road[1]/60+road[2]/3600
      ind = readable[head[x]].index(y)
      readable[head[x]].remove(y)
      readable[head[x]].insert(ind, cross)
plt.rc("text", usetex=True)

def main():
  cool = list(set(readable[head[1]]))
  markers = [".", ",", "o", "v", "^", "<", ">", "1", "2", "3",
	    "4", "8", "s", "p", "*", "h", "H", "+"]
  colors = []
  for x in xrange(len(cool)): #Generated by RGB mode
    colors.append((np.random.uniform(0, 1), np.random.uniform(0, 1), np.random.uniform(0, 1)))

  #def index():
    #fig = plt.figure()
    #for x in len(readable[head[9]]):
      #try:
	#plt.plot()

  def reloader():
    try:
      os.system("xterm -hold -e sudo python aladin.py")
      sys.exit()
    except:
      tue = Toplevel()
      tue.wm_title("Error")
      Label(tue, text="I can't execute xterm, to more info see te help.").grid()
      tue.mainloop()

    
  def plot2d(): 	#Plot the Location
    ev = Toplevel()
    ev.wm_title("Position Plot (RA, DEC)")
    fig = plt.figure()
    ax = fig.add_subplot(111, axisbg="black")
    ax.get_xaxis().get_major_formatter().set_scientific(False) #Removing Cientific Notation
    ax.get_xaxis().get_major_formatter().set_useOffset(False) #And exponentials
    dawn = list(cool)
    for x in xrange(len(readable[head[2]])):
      if dawn.count(readable[head[1]][x]) == 1:
	plt.scatter(readable[head[2]][x], readable[head[3]][x], c=colors[cool.index(readable[head[1]][x])],
		  marker=markers[cool.index(readable[head[1]][x])], label = readable[head[1]][x])
	dawn.remove(readable[head[1]][x])
      else:
	plt.scatter(readable[head[2]][x], readable[head[3]][x], c=colors[cool.index(readable[head[1]][x])],
		    marker=markers[cool.index(readable[head[1]][x])])
    plt.xlabel(r"$RA$")
    plt.ylabel(r"$\delta$", fontsize=15)
    plt.legend(bbox_to_anchor=(1, .9),
	      bbox_transform=plt.gcf().transFigure)
    ax.format_coord = lambda x,y : "RA=%g, DEC=%g"%(x, y)
    canvas = FigureCanvasTkAgg(fig, master = ev)
    toolbar = NavigationToolbar2TkAgg(canvas, ev)
    canvas.get_tk_widget().pack()
    toolbar.pack()
    ev.mainloop()
  
  def helper():
    """
    Hello!
    As you needed permissions to execute this script, when the webbrowser is open is going to be in those permissions.
    So, if you have opened a window of that webbrowser without the same permissions, you need to close that window.
    Sorry for the problems!
    """
    loc = location+"/HTML/help.html" 
    webbrowser.open(loc)
    

  def andother():
    burn.destroy()
    sys.exit()
    
  burn = Tk()
  burn.protocol('WM_DELETE_WINDOW', andother)
  burn.wm_title("Analysis From Simbad, Aladin.")
  
  #Toolbar
  menu = Menu(burn)
  burn.config(menu=menu)
  filemenu = Menu(menu)
  menu.add_cascade(label="File", menu=filemenu)
  filemenu.add_command(label="Exit", command=andother)
  setupmenu = Menu(menu)
  menu.add_cascade(label="Setup", menu=setupmenu)
  setupmenu.add_command(label="Reload Colors", command=reloader)
  plotmenu = Menu(menu)
  menu.add_cascade(label="Plots", menu=plotmenu)
  plotmenu.add_command(label="Position (RA, DEC)", command=plot2d)
  menu.add_command(label="Help", command=helper)
  
  l0 = Label(burn, text="")#\n
  l1 = Label(burn, text="Hello! I made this program to analyse all the data recieved from Simbad, a library of Aladin"
	     ", the biggest database about astronomy in the world.")
  l2 = Label(burn, text="If this is your first time I recommend to click in 'Help', where you can find a simple guide of"
	     " how to use Aladin.")
  l1.grid(columnspan = 2)
  l2.grid(columnspan = 2)
  l0.grid()
  burn.grid_columnconfigure(1, weight=1)
  burn.grid_columnconfigure(0, weight=1)  

  burn.mainloop()


while True:
  main()
## References
# http://dalelane.co.uk/blog/?p=778
# libreoffice --help
# http://effbot.org/tkinterbook/tkinter-application-windows.htm
# https://docs.python.org/2/library/functions.html#reload