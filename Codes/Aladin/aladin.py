# The code only works for computers in English or Spanish...

import sys
import os
import numpy as np
if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *
import tkFileDialog 
try:
  import odf.opendocument
  from odf.table import *
  from odf.text import P
except (ImportError):
  print "You don't have installed 'odf', to install it please visit the next link \n\n https://pypi.python.org/packages/source/o/odfpy/odfpy-0.9.6.tar.gz \n\n"
  print ("To run the setup.py you must have (obviously) privileges, so, when you had installed the library, execute this code with the same"
	 " permissions with which you installed the library :)")
  sys.exit()
# Copyright 2011 Marco Conti
# Licensed under the Apache License, Version 2.0 (the "License"):

#  	http://www.apache.org/licenses/LICENSE-2.0

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
			#	print "Empty or commented row (", row_comment, ")"
		
		self.SHEETS[name] = arrRows
		
	# returns a sheet as an array (rows) of arrays (columns)
	def getSheet(self, name):
		return self.SHEETS[name]
	     
#Self
class aladin:
  def __init__(self):
    pass
  
  def choose(self):
    root = Tk()
    m = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a .ods file')
    root.destroy()
    return m
  
  def interactive(self):         
    def read():
      def man():
	fun = E1.get()
	return fun
      def extract():
	doc = ODSReader(aladin.choose())
	tipe = doc.getSheet(sheet)
	sound = [] 
	for x in tipe:
	    for y in x:
	      sound.append(y)
	sound = np.array(sound)
	sound = sound.reshape(len(tipe), len(tipe[0]))
	return tipe, sound
      root.destroy()
      if os.getenv('LANG')[0] + os.getenv('LANG')[1] == "es":
	sheet = "Hoja1"
      elif os.getenv('LANG')[0] + os.getenv('LANG')[1] == "en":
	sheet = "Sheet1"
      else:
	sheet = raw_input("Please insert this (Sheet1) but in your computer language")      
      tipe, sound = extract()      
      ar = []
      for x in tipe[0]:
	ar.append(x)
      reet = Tk()
      reet.wm_title("Interactive")
      L1 = Label(reet, text="I got the data...")
      L2 = Label(reet, text="As you might know, there are %i categories of the data that you have"%len(tipe[0]))
      L3 = Label(reet, text ="And they are: \n")
      E1 = Entry(reet)
      E1.delete(0, END)
      E1.insert(0, "Distance (Parsecs)")
      B1= Button(reet, text="Entry", command=man)
      L1.grid()
      L2.grid()
      L3.grid()
      E1.grid(columnspan = 2, sticky=W)
      B1.grid(row=3, sticky=E)
      for x in tipe[0]:
	Label(reet, text = "- "+x).grid()
      reet.mainloop()
    def andother():
      root.destroy()
      sys.exit()
    root =Tk()
    root.protocol('WM_DELETE_WINDOW', andother)
    root.wm_title("Welcome!")
    L1 = Label(root, text="Hello there! \n Here is the program I made to realize an analysis of the Simbad data got by Aladin."
	       " I hope that the program will be interactive.")
    B1 = Button(root, text="Let's do it", command=read)
    B2 = Button(root, text="Exit", command=andother)
    L1.grid(columnspan=2)
    B1.grid(row=2, sticky=E)
    B2.grid(row=2, column=1, sticky=W)
    root.mainloop()

aladin = aladin()
aladin.interactive()