'''
This code was finished on October 6, 2015
Is under GNU General Public License, see http://www.gnu.org/licenses/gpl-3.0.en.html
By Julian Jimenez.
'''
from Tkinter import *
import mechanize #Probably you don't have this, you can install it here: http://wwwsearch.sourceforge.net/mechanize/download.html
from astropy.io import ascii
import numpy as np
import tkFileDialog
import matplotlib.pyplot as plt
import cookielib
import sys

flag=[] #Made to pass data inside functions
def get_data(rai):
    '''
    This function runs if you don't have a txt with the data. It opens a graphic interface similar to
    Hipparcos Database, to introduce the parameters to search. After that, it takes the response from
    the database and saves it as table.txt
    '''
    rai.destroy()#Closing the first window of the execution
    ##Doing the interface to introduce parameters
    main=Tk()
    main.wm_title("Hipparcos")
    Label(text="Select Catalogue to search:").grid(row=0,column=0)
    v= IntVar()
    a={}
    b={}
    c={}
    d={}
    Radiobutton(main, text="Hipparcos Main Catalogue", variable=v, value=0).grid(row=0, column=1)
    Radiobutton(main, text="Tycho Main Catalogue", variable=v, value=1).grid(row=0, column=2)
    Radiobutton(main, text="Tycho-2 Catalogue", variable=v, value=2).grid(row=0, column=3)
    Label(text="Select from some or all of the following fields").grid(row=1,column=0, columnspan=4)
    index1 = ["Field", "Minimun Value", "Maximun Value", "Notes"]
    index2 = ["ra (degrees)", "dec (degrees)", "parallax (mas)", "V magnitude",
              "B-V"]
    index3= ["All catalogues"]*2+["Hipparcos and Tycho Catalogues only",
                                  "Johnson V for Hipparcos and Tycho Catalogues,V_T magnitude for Tycho-2 Catalogue",
                                  "Hipparcos and Tycho Catalogues only"]
    for x in xrange(4):
        Label(text=index1[x]).grid(row=2,column=x)
    for x in xrange(5):
        b[str(x)]=IntVar()
        a[str(x)] = Checkbutton(main, text=index2[x], variable=b[str(x)])
        a[str(x)].grid(row=3+x, column=0)
        Label(text=index3[x]).grid(row=3+x, column=3)
    for x in xrange(5):
        for y in xrange(2):
            d[str(x)+str(y)]=StringVar()
            c[str(x)+str(y)]= Entry(main, textvariable=d[str(x)+str(y)])
            c[str(x)+str(y)].grid(row=3+x, column=y+1)
            d[str(x)+str(y)].set("0.0")
    Button(main,text="Submit", command=main.destroy).grid(row=8, column=0, columnspan=2)
    Button(main,text="Cancel", command=sys.exit).grid(row=8, column=2, columnspan=2)
    main.mainloop()

    ### Gesting Web page
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    #These are generic addheaders, does not matter if they're not the specifications of your computer
    catalogues= ["Hipparcos Main Catalogue","Tycho Main Catalogue","Tycho-2 Catalogue"]
    br.open('http://www.rssd.esa.int/hipparcos_scripts/hipMultiSearch1.pl') #Opening the webpage
    br.select_form(nr=0)
    br.form['Catalogues'] = [catalogues[v.get()]] #Obtaining all fields that can be modified
    ##Here we write all the input we got from the graphic interface in the web page
    if b["0"].get()==1:
        br.form['ra (degrees)']=["on"]
        br.form['ramin']=d["00"].get() 
        br.form['ramax']=d["01"].get()
    if b["1"].get()==1:
        br.form['dec (degrees)']=["on"]
        br.form['decmin']=d["10"].get()
        br.form['decmax']=d["11"].get()

    if b["2"].get()==1:
        br.form['parallax (mas)']=["on"]
        br.form['parmin']=d["20"].get()
        br.form['parmax']=d["21"].get()

    if b["3"].get()==1:
        br.form['V magnitude']=["on"]
        br.form['Vmin']=d["30"].get()
        br.form['Vmax']=d["31"].get()


    if b["4"].get()==1:
        br.form['B-V']=["on"]
        br.form['BVmin']=d["40"].get()
        br.form['BVmax']=d["41"].get()

    br.submit() #Sending the request
    pon=br.response().read()#Reading the response
    print pon[pon.index('color="#ff0000">')+16:pon.index("request.")+8]#Printing the number of values that satisfied the request
    ##Here we obtain the table from the response and we write it in a file called table.txt
    with open("table.txt", "w") as f:
        f.write(pon[pon.index("your request.\n</font></b>")+25:pon.index("</body>\n</html>")])
        f.close()
    flag.append("table.txt") #Now the name of the file to be checked is table

def get_file(rai):
    '''
    This function opens a graphic interface to search the file that is going to be analized.
    '''
    rai.destroy()
    root = Tk()
    m = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a .txt file')
    root.destroy()
    flag.append(m) #Now the name of te file to be checked is m
##Here starts the ejecution
ant = Tk()#Simple asking window 
ant.wm_title("Hipparcos Database")
Label(text="Do you have a txt with the data?").grid()
Button(ant, text="yes", command=lambda: get_file(ant)).grid(row=1, column=0)
Button(ant, text="no", command=lambda: get_data(ant)).grid(row=1, column=1)
ant.mainloop()
   
while True:
    ##Here is where you introduce the combination you want
    frame = Tk()
    Label(text="Insert combination:").grid()
    Label(text="Colour Index").grid(row=1, column=0)
    Label(text="Magnitude").grid(row=1, column=1)
    fir=IntVar()
    sec=IntVar()
    fir.set(38)
    sec.set(33)
    frame.wm_title("HR Diagram")
    Radiobutton(frame, text="B-V Index", variable=fir, value=38).grid(row=2, column=0)
    Radiobutton(frame, text="V-I Index", variable=fir, value=41).grid(row=3, column=0)
    Radiobutton(frame, text="B mag", variable=sec, value=33).grid(row=2, column=1)
    Radiobutton(frame, text="V mag", variable=sec, value=35).grid(row=3, column=1)
    Button(frame,text="Submit", command=frame.destroy).grid(row=4, column=0)
    Button(frame, text="END", command=sys.exit).grid(row=4,column=1)
    frame.mainloop()
    data = ascii.read(flag[0]) #Reading the file
    par = data["col12"] #Reading the parallax column
    M=[]
    ind = []
    m= data["col"+str(sec.get())] #Reading B or V mag
    for x,y,z in zip(par,m,data["col"+str(fir.get())]): #Obtaining B-V or V-I index
        try:
            M.append(float(y)+5-5*np.log(1./float(x))) #Obtaining the abs mag
            ind.append(float(z)) 
        except:
            pass
    print "There were %i valid entries"%len(M) #Printing the number of valid entries
    ##Doing the plot
    ax= plt.subplot()
    ax.set_axis_bgcolor('black')
    ax.set_ylim([max(M)+1,min(M)-1])
    if fir.get()==38:
        ax.set_xlabel("B-V Index")
    else:
        ax.set_xlabel("V-I Index")
    if sec.get()==33:
        ax.set_ylabel("Abs Mag (Blue)")
    else:
        ax.set_ylabel("Abs Mag (Visual)")
    ax.set_title("HR Diagram")
    ##About colors
    count=0
    other=0
    jai=0
    another=0
    cout=0
    for x in ind:
        if -.29<=x<=0:
            count+=1
        elif x<=-.29:
            cout+=1
        if x>=.31:
            another+=1
        if 0<=x<=.31:
            jai+=1
        if x<=.31:
            other+=1
    long = len(ind)
    ##Degrading colors 
    col = [np.concatenate((np.array([255]*(long-count-cout)),np.linspace(255,0,cout+count)))/1000., np.concatenate((np.concatenate((np.linspace(0,255,long-other),np.array([255]*jai))),np.linspace(255,0,cout+count)))/1000. ,
           np.concatenate((np.concatenate((np.array([0]*(long-other)),np.linspace(0,255,jai))),np.array([255]*(cout+count))))/1000.]
    timer=0
    fin, now= [],[]
    for x in np.array(ind).argsort()[::-1]:
        fin.append(ind[x])
        now.append(M[x])
    for x,y in zip(fin, now):
        ax.scatter(x, y, s=1, color=[(col[0][timer], col[1][timer], col[2][timer])])
        timer+=1
    plt.show()
#References:
# http://stackoverflow.com/questions/25027339/how-to-get-data-from-inspect-element-of-a-webpage-using-python
# http://stockrt.github.io/p/emulating-a-browser-in-python-with-mechanize/
