print "\nImporting libraries..."
import matplotlib.pyplot as plt
import astropy.io.fits as pyfits
print "Done."

#Opening File and Pointing
print "\nOpening FITS file..."
s = pyfits.open("IC1683.V500.rscube.fits.gz")
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
wavelength = [wavelength[x] for x in xrange(1,1877,8)]
print "Done."

def showspectra(event):
    "This function draws the spectra for each pixel and actualizes the frame"
    try:
        ax2.clear()
        f.canvas.draw()
        x,y=int(event.xdata), int(event.ydata)
        ax2.set_xlabel(x_label_spectra)
        ax2.set_ylabel("Flux")
        ax2.plot(wavelength, [data[cout][x][y] for cout in xrange(1,1877,8)])
        print "Drew spectra of pixel (%i, %i)"%(x,y)
        f.canvas.draw()
    except:
        pass

#Graphic the environment
print "\nSetting environment..."
f, (ax1, ax2) = plt.subplots(1,2, figsize=(15,10))
for x in xrange(1,74):
	for y in xrange(1,79):
		ax1.scatter(x,y)
cid = f.canvas.mpl_connect('button_press_event', showspectra)
print "Done."

#Showing the environment
print "\nShowing environment..."
plt.show()
print "\n\nFinishing process.\n"

#http://matplotlib.org/users/event_handling.html
#http://pythonhosted.org/pyfits/
