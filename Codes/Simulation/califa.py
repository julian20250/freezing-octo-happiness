print "\nImporting libraries..."
import sys
if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *
import tkFileDialog
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import astropy.io.fits as pyfits
import matplotlib.cm as cm
import matplotlib.colorbar as cbar
print "Done."

def choose():
    "This Function selects the file to be analyzed"
    root = Tk()
    root.update()
    m = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose File')
    root.quit()
    return m

#Steps of spectra
step=4

#Opening File and Pointing
print "\nOpening FITS file..."
#s = pyfits.open("IC1683.V500.rscube.fits.gz")
s= pyfits.open(choose().name)
print "About the File:"
print "==================="
s.info()
print "==================="
data= s[0].data
headers = s[0].header
print "Done."

#Getting Headers of The file
print "\nGetting Headers of the FITS file..."
header_list=[]
header_result=[]
for x, y in headers.iteritems():
    header_list.append(x)
    header_result.append(y)

#Finding the format of the data
count=0
for x in header_list:
    if "CUNIT3" in x:
        x_label_spectra=header_result[count]
    if "CRVAL3" in x:
        lambda_begin=header_result[count]
    if "CDELT3" in x:
        lambda_step=header_result[count]
    if "CRPIX3" in x:
        lambda_pix=header_result[count]
    if "CRVAL2" in x:
        dec_value=header_result[count]
    if "CRPIX2" in x:
        dec_ref=header_result[count]
    if "CD2_2" in x:
        dec_step=header_result[count]
    if "V500 PPAK P3 RA" in x:
        ra_value=header_result[count]
    if "CD1_1" in x :
        ra_step=header_result[count]
    count+=1
#print header_list[count]
#print headers["V500 PPAK P2 RA"]
declination=[]
RA=[]
count=dec_value-dec_step*dec_ref

for x in xrange(1, len(data[0][0])):
    declination.append(count)
    count+=dec_step

count=ra_value-ra_step*dec_ref
for x in xrange(1, len(data[0])):
    RA.append(count)
    count+=ra_step

declination= [str(int(x))+"deg"+str(int((x-int(x))*60.))+"'"+str(int(((x-int(x))*60.-int((x-int(x))*60.))*60.))+"''" for x in declination]

RA=[str(int(x*24/360.))+"h"+str(int((x*24/360.-int(x*24/360.))*60))+"m"+"%1.2f"%(((x*24/360.-int(x*24/360.))*60-int((x*24/360.-int(x*24/360.))*60))*60)+"s" for x in RA]
print "Done."

#print x_label_spectra, lambda_begin, lambda_step, lambda_pix
#Adquire the wavelength interval
print "\nSetting wavelength..."
wavelength= []
for x in xrange(int(lambda_begin), int(lambda_begin+lambda_step*len(data)), int(lambda_step)):
    wavelength.append(x)
wavelength = [wavelength[x] for x in xrange(1,len(data),step)]
print "Done."

def showspectra(event):
    "This function draws the spectra for each pixel and actualizes the frame"
    try:
        ax2.clear()
        f.canvas.draw()
        x,y=int(event.xdata), int(event.ydata)
        ax2.set_xlabel(x_label_spectra)
        ax2.set_ylabel("Flux")
        ax2.plot(wavelength, [data[cout][x][y] for cout in xrange(1,len(data),step)])
        print "Drew spectra of pixel (%i, %i)"%(x,y)
        f.canvas.draw()
    except:
        pass

#Setting Pixels
print "\nSetting Pixels"
magnitude_black=[]
for x in xrange(1,len(data[0])):
    for y in xrange(1,len(data[0][0])):
        magnitude_black.append(sum([data[cout][x][y] for cout in xrange(1,len(data),step)]))
max_color=max(magnitude_black)
min_color=min(magnitude_black)
magnitude_black=[(x-min_color)/(max_color-min_color) for x in magnitude_black]
#New Part
percent=0
magnitude_black=[(1-percent)*x+percent for x in magnitude_black]

#Another new Part
my_cmap= cm.get_cmap("spectral") #Here to Change Colorbar
color_data= my_cmap(np.array(magnitude_black))
print "Done."

#Graphic the environment
print "\nSetting environment..."
f, (ax1, ax2) = plt.subplots(1,2, figsize=(15,10)) #If you have problems in plotting of the data,
#remove the figsize arg
count=0

for x in xrange(1,len(data[0])):
    for y in xrange(1,len(data[0][0])):
        ax1.add_patch(patches.Rectangle((x-.5,y-.5),1,1,fill=True, edgecolor="black", color=color_data[count]))
        count+=1
ax1.set_xlim(0,len(data[0]))
ax1.set_ylim(0,len(data[0][0]))
ax1.set_yticks(xrange(1,len(data[0][0]), 6))
ax1.set_yticklabels([declination[x] for x in xrange(0,len(declination),6)])

normal = plt.Normalize(min(magnitude_black), max(magnitude_black))
cax, _ = cbar.make_axes(ax1)
cb2 = cbar.ColorbarBase(cax, cmap=my_cmap,norm=normal)

ax1.set_xticks(xrange(1, len(data[0]), 4))
ax1.set_xticklabels([RA[x] for x in xrange(0,len(RA),4)], rotation=90)

ax1.set_ylabel("Declination")
ax1.set_xlabel("RA")
plt.suptitle(headers["OBJECT"])

ax1.tick_params(labelsize=8)
ax1.format_coord = lambda x,y : "Pixel: (%0g, %0g)"%(x, y)
ax2.format_coord = lambda x,y : "Wavelength=%0g, Flux=%0g"%(x, y)
cid = f.canvas.mpl_connect('button_press_event', showspectra)
print "Done."

#Showing the environment
print "\nShowing environment..."
plt.show()
print "\n\nFinishing process.\n"

#http://matplotlib.org/users/event_handling.html
#http://pythonhosted.org/pyfits/
