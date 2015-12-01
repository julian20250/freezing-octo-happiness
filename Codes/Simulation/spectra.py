#coding: utf-8
from astropy.io import fits
from Tkinter import *
import tkFileDialog
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import uuid
import warnings
import numpy as np
from astropy.modeling import models, fitting
warnings.simplefilter('ignore', np.RankWarning)
#------------------------------------------------------------
print ("\n\nHola. Este programa analiza tanto archivos fits como txt con datos de espectros. "
  "Se abrirá una ventana emergente donde podéis escoger el archivo a analizar y el tipo del mismo. "
  "Una vez seleccionado, se graficará el espectro y se mostrará el flujo total, calculado a "
  "partir de una aproximación por integración por rectángulos.\n\n Para analizar una línea de emisión o absorción, "
  "hay que hacerle zoom en la gráfica, cerrar esta gráfica y el programa hará el resto. Es mejor seleccionar un buen "
  "perfil, porque no es muy bueno con líneas combinadas. Si son varias líneas, analizará la que tenga más intensidad.\n\n"
  "Puede pasar que la campana no quede sobre el continuo, mas es la campana que corresponde a la línea analizada.\n\n")
flagg=0
def get_file():
	root=Tk()
	m= tkFileDialog.askopenfile(parent=root, mode="rb", title="Choose a FITS file", filetypes=[('fits files', '.fits.gz'), ('text files', '.txt')])
	root.destroy()
	return m
def find_nearest(array,value):
  #Taken of :http://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
    idx = (np.abs(array-value)).argmin()
    return array[idx]
name = get_file()
try:
  t = fits.open(name)
  try:
      oa = t[0].header["AUTHOR"]
      if oa=="CALIFA Collaboration":
	  print "\n\n===================================================================="
	  print "Filename: %s\nObject Name: %s"%(t[0].header["FILENAME"], t[0].header["OBJECT"])
	  print "Califa ID: %s\nAuthor: %s"%(t[0].header["CALIFAID"], t[0].header["AUTHOR"])
	  print "===================================================================="
  except:
      pass

  print "\n\n"
  print "===================================================================="
  print "FITS info:"
  t.info()
  print "====================================================================\n\n"

  #Show keys of header
  print "===================================================================="
  chec = " "

  #print "These are the headers:"
  #for x in t[0].header:
  #    print x,
  #while chec!="":
  #    chec= raw_input("\nType to get info header, else, left blank > ")
  #    if chec!="":
  #        print "Info: %s"%t[0].header[chec]
  tbdata = t[0].data
  try:
	  start= t[0].header["W0"]
	  step= t[0].header["WPC"]
  except:
	  pass
  wl = []
  cout=float(start)
  if len(tbdata)==2:
	  tbdata=tbdata[0]
  else:
	  pass
  for x in xrange(len(tbdata)):
	  wl.append(cout)
	  cout+=step
  wl= np.array(wl)

except:
  flagg=1
  wl, tbdata=np.loadtxt(name.name, dtype="float", skiprows=3, usecols=(0,1), unpack=True)
tot_flux=0
for x in xrange(len(wl)-1):
    delta=wl[x+1]*wl[x]
    tot_flux+=delta*min([tbdata[x+1], tbdata[x]])
poly =np.polyfit(wl, tbdata, 2)
poly= np.poly1d(poly)
poly= poly(wl)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(wl,tbdata, label="Espectro")
ax.plot(wl, poly, label="Ajuste")
plt.legend()
if flagg==1:
  ax.set_xlabel("Eje Espectral (km/s)")
else:
  ax.set_xlabel("Longitud de Onda (A)")
if tbdata[0]<1:
	ax.set_ylabel("Flujo (Jy)")
	print "Flujo Total = %f Jy"%tot_flux
else:
	ax.set_ylabel("Fotones por segundo (counts/s)")
	print "Flujo Total = %f counts/s"%tot_flux
#namae=str(uuid.uuid4())
plt.show()

h,j=ax.get_xlim()
count1=-1
count2=-1
ter=0
while ter==0:
  if wl[count1+1]>h:
    ter=1
  count1+=1
ter=0
while ter==0:
  if wl[count2+1]>j:
    ter=1
  count2+=1
  
sti = wl[count1:count2]
ck= tbdata[count1:count2]
men = sti[list(ck).index(max(ck))]
poly =np.polyfit(sti, ck, 10)
poly= np.poly1d(poly)
poly= poly(np.linspace(count1, count2, 1000))
found=np.linspace(count1, count2, 1000)
to= (min(ck)+max(ck))/2.
near = find_nearest(poly, to)
poly=list(poly)
ub1=found[poly.index(near)]
poly.remove(near)
poly=np.array(poly)
near=find_nearest(poly, to)
poly=list(poly)
ub2=found[poly.index(near)]
FWMH=abs(ub2-ub1)
o=FWMH/2.355
print "FWMH= %f"%FWMH
g_init = models.Gaussian1D(amplitude=max(ck), mean=men, stddev=o)
fit_g = fitting.LevMarLSQFitter()
g = fit_g(g_init, sti, ck)
scale=max(ck)/(max(ck)+min(ck))
ret=(g(np.array(sti))+min(ck))*scale
plt.plot(sti, ret,"r-", label="Gaussiana")
#plt.plot([ub1,ub2], [near, near])
plt.scatter(sti,ck)
plt.legend()
plt.show()
#plt.savefig(namae, transparent=False)
#print "Image called %s generated.\nBye."%namae
try:
  t.close()
except:
  pass
print "\n\n"

#---------------------------------------------------------------
#References:
#http://docs.astropy.org/en/stable/io/fits/
#Error LaTeX: https://github.com/matplotlib/matplotlib/issues/5076
#http://www.stsci.edu/documents/dhb/web/c03_stsdas.fm3.html
