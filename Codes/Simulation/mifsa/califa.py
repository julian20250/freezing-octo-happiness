print "\n"
print "Importing Libraries..."
import sys
if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *
import tkFileDialog
import os
import continuum
import numpy as np
import warnings # Annoying message color override
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import astropy.io.fits as pyfits
import matplotlib.cm as cm
import warnings
import matplotlib.colorbar as cbar
print "Importing Libraries... Done."

#warnings.filterwarnings('ignore')

def abs(x):
    if x>=0:
        return x
    else:
        return -1*x

def choose():
    "This Function selects the file to be analyzed"
    root = Tk()
    root.update()
    m = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose File')
    root.destroy()
    return m

def emergent_window():
    root=Tk()
    root.geometry("500x500")
    root.wm_title("Wavelength Interval")
    Label(root,text="Insert the interval").grid(row=0, column=0)
    var = IntVar()
    c= Checkbutton(root, text="Allow Interval", variable=var, onvalue=1, offvalue=0)
    c.grid(row=1, column=0)
    Label(root,text="Interval").grid(row=2,column=0)
    begin= Entry(root)
    end= Entry(root)
    begin.grid(row=2, column=1)
    end.grid(row=2, column=2)
    j=[]
    Button(root, text="Continue", command=lambda: obtain_entry(root,begin,end,j)).grid(row=3,column=2)
    root.mainloop()
    if var.get()==1:
        return j
    else:
        return None

def obtain_entry(root, a, b, j):
    try:
      j.append(float(a.get()))
      j.append(float(b.get()))
    except:
      pass
    root.destroy()
    
def showspectra(event):
    "This function draws the spectra for each pixel and actualizes the frame"
    try:
        ax2.clear()
        f.canvas.draw()
        x,y=int(event.xdata), int(event.ydata)
        ax2.set_xlabel(x_label_spectra)
        ax2.set_ylabel("Flux")
        if token==0:
            ax2.plot(wavelength, [data[cout][x][y] for cout in xrange(0,len(data),step)])
            wav1,dat1=continuum.interpolate(wavelength,[data[cout][x][y] for cout in xrange(0,len(data),step)])
            ax2.plot(wav1,dat1)
        else:
            ax2.plot(wavelength, [data[cout][x][y] for cout in xrange(begin_wl,end_wl,step)])
            wav1,dat1=continuum.interpolate(wavelength,[data[cout][x][y] for cout in xrange(begin_wl,end_wl,step)])
            ax2.plot(wav1,dat1)
        print "Drew spectra of pixel (%i, %i)"%(x,y)
        f.canvas.draw()
    except:
        pass

def end(root):
    root.destroy()
    sys.exit()

supported_parameters=["-no_interval"]
warnings.simplefilter(action = "ignore", category= FutureWarning)
warnings.simplefilter(action = "ignore", category= UserWarning)
while True:
    print "\nChecking Parameters..."
    if len(sys.argv)>1:
        for x in sys.argv[1:]:
            flagger=0
            for y in supported_parameters:
                if x==y:
                    flagger=1
            if flagger==0:
                os.system("cat usage.txt")
                sys.exit()
    print "Checking Parameters... Done."

    #Steps of spectra
    step=2

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

    #Getting Headers of The file
    header_list=[]
    header_result=[]
    for x, y in headers.iteritems():
        header_list.append(x)
        header_result.append(y)
    print "Opening FITS file... Done."
    #Finding the format of the data
    print "\nGetting Headers of the FITS file..."
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
    print "Getting Headers of the FITS file... Done."

    #print x_label_spectra, lambda_begin, lambda_step, lambda_pix
    #Adquire the wavelength interval
    print "\nSetting Wavelength..."
    wavelength= []
    for x in xrange(int(lambda_begin), int(lambda_begin+lambda_step*len(data)), int(lambda_step)):
        wavelength.append(x)
    #Emergent Window
    ran=None
    if len(sys.argv)==1:
        ran=emergent_window()
    else:
        just_a_flag=0
        for x in sys.argv[1:]:
            if x=="-no_interval":
                just_a_flag=1
        if just_a_flag==0:
            ran=emergent_window()
    token=0
    if ran != None:
        compare_begin=[abs(x-ran[0]) for x in wavelength]
        compare_end=[abs(x-ran[1]) for x in wavelength]
        begin_wl=compare_begin.index(min(compare_begin))
        end_wl=compare_end.index(min(compare_end))
        wavelength=[wavelength[x] for x in xrange(begin_wl,end_wl,step)]
        ka=len(data[0])
        token=1
        ke=len(data[0][0])
        ob=data
        for x in xrange(len(data[0])):
            for y in xrange(len(data[0][0])):
                for z in xrange(0,len(data),step):
                    if begin_wl<=z<=end_wl:
                        pass
                    else:
                        data[z][x][y]=0
    else:
        wavelength = [wavelength[x] for x in xrange(0,len(data),step)]
        pass

    print "Setting Wavelength... Done."


    #Setting Pixels
    print "\nSetting Pixels..."
    magnitude_black=[]
    for x in xrange(len(data[0])):
        for y in xrange(len(data[0][0])):
            magnitude_black.append(sum([data[cout][x][y] for cout in xrange(0,len(data),step)]))
    max_color=max(magnitude_black)
    min_color=min(magnitude_black)
    magnitude_black=[(x-min_color)/(max_color-min_color) for x in magnitude_black]
    #New Part
    percent=0
    magnitude_black=[(1-percent)*x+percent for x in magnitude_black]
    #Another new Part
    my_cmap= cm.get_cmap("spectral") #Here to Change Colorbar
    color_data= my_cmap(np.array(magnitude_black))
    print "Setting Pixels... Done."
    #Graphic the environment
    print "\nSetting Environment..."
    f, (ax1, ax2) = plt.subplots(1,2, figsize=(15,10)) #If you have problems in plotting of the data,
    #remove the figsize arg
    count=0

    for x in xrange(len(data[0])):
        for y in xrange(len(data[0][0])):
            ax1.add_patch(patches.Rectangle((y-.5,x-.5),1,1,fill=True, edgecolor="black", color=color_data[count]))
            count+=1
    ax1.set_xlim(0,len(data[0][0])-1)
    ax1.set_ylim(0,len(data[0])-10)
    ax1.set_yticks(xrange(0,len(data[0][0])-10, 6))
    ax1.set_yticklabels([declination[x] for x in xrange(0,len(declination),6)])
    normal = plt.Normalize(min(magnitude_black), max(magnitude_black))
    cax, _ = cbar.make_axes(ax1)
    cb2 = cbar.ColorbarBase(cax, cmap=my_cmap,norm=normal)

    ax1.set_xticks(xrange(0, len(data[0])-1, 4))
    ax1.set_xticklabels([RA[x] for x in xrange(0,len(RA),4)], rotation=90)
    ax1.set_ylabel("Declination")
    ax1.set_xlabel("RA")
    plt.suptitle(headers["OBJECT"])

    ax1.tick_params(labelsize=8)
    ax1.format_coord = lambda x,y : "Pixel: (%0g, %0g)"%(x, y)
    ax2.format_coord = lambda x,y : "Wavelength=%0g, Flux=%0g"%(x, y)
    cid = f.canvas.mpl_connect('button_press_event', showspectra)
    print "Setting Environment... Done."

    #Showing the environment
    print "\nShowing Environment..."
    plt.show()
    root=Tk()
    root.geometry("500x500")
    Button(root,text="End",command=lambda: end(root)).grid()
    Button(root,text="Continue", command=root.destroy).grid()
    root.mainloop()
    print "Finishing Process."
    print "\n\n"

#http://matplotlib.org/users/event_handling.html
#http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.polyfit.html
#http://pythonhosted.org/pyfits/