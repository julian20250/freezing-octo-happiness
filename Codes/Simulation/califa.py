print "\nImporting libraries..."
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import astropy.io.fits as pyfits
print "Done."

#Steps of spectra
step=1

#Opening File and Pointing
print "\nOpening FITS file..."
s = pyfits.open("IC1683.V500.rscube.fits.gz")
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
    count+=1
print "Done."

#print x_label_spectra, lambda_begin, lambda_step, lambda_pix
#Adquire the wavelength interval
print "\nSetting wavelength..."
wavelength= []
for x in xrange(int(lambda_begin), int(lambda_begin+lambda_step*len(data)), int(lambda_step)):
    wavelength.append(x)
wavelength = [wavelength[x] for x in xrange(1,1877,step)]
print "Done."

def showspectra(event):
    "This function draws the spectra for each pixel and actualizes the frame"
    try:
        ax2.clear()
        f.canvas.draw()
        x,y=int(event.xdata), int(event.ydata)
        ax2.set_xlabel(x_label_spectra)
        ax2.set_ylabel("Flux")
        ax2.plot(wavelength, [data[cout][x][y] for cout in xrange(1,1877,step)])
        print "Drew spectra of pixel (%i, %i)"%(x,y)
        f.canvas.draw()
    except:
        pass
#Setting Pixels
print "\nSetting Pixels"
magnitude_black=[]
for x in xrange(1,73):
    for y in xrange(1,78):
        magnitude_black.append(sum([data[cout][x][y] for cout in xrange(1,1877,step)]))
max_color=max(magnitude_black)
min_color=min(magnitude_black)
magnitude_black=[(x-min_color)/(max_color-min_color) for x in magnitude_black]
print "Done."

#Graphic the environment
print "\nSetting environment..."
f, (ax1, ax2) = plt.subplots(1,2, figsize=(15,10)) #If you have problems in plotting of the data,
#remove the figsize arg
count=0
for x in xrange(1,73):
	for y in xrange(1,78):
            ax1.add_patch(patches.Rectangle((x-.5,y-.5),1,1, fill=True, color=str(1-magnitude_black[count])))
            count+=1
ax1.set_xlim(0,74)
ax1.set_ylim(0,79)
cid = f.canvas.mpl_connect('button_press_event', showspectra)
print "Done."

#Showing the environment
print "\nShowing environment..."
plt.show()
print "\n\nFinishing process.\n"

#http://matplotlib.org/users/event_handling.html
#http://pythonhosted.org/pyfits/
