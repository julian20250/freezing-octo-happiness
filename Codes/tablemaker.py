def tablemaker(dat, col, raw, per):
  """ Function doc.
  
  This function makes a table in LaTeX.
  dat : list
	Data.
  col : int
      Number of columns.
  raw : list
      List of strings in the first row.
  per : int
      Number of rows per table.
  """

  if col != len(raw):
    raise EnvironmentError("You can't have a different number of columns and strings")
  if len(dat)%col != 0:
    raise EnvironmentError("The number of data must be divisible by the number of columns")
  f= open("table.txt", "w")
  d=[]
  table = (len(dat)/col)/per 
  if (len(dat)/col)%per != 0:
    table += 1
  for x in xrange(col):
    d.append("c")
  d="|".join(d)
  fle = []
  count = 0
  dar = len(dat)/col
  deli = int(dar)
  for x in xrange(col):    
    fle.append(dat[count:deli])
    count += dar
    deli += dar
  count = 0 
  fil=0
  onl = int(per)
  for x in xrange(table):
      if count!=0:
	f.write("\\quad")
      f.write("\\begin{tabular}{|%s|}"%d)
      f.write("\n\\hline\n")
      f.write("%s "%raw[0])
      for y in raw[1:]:
	f.write("& %s "%y)
      f.write("\\\\ \\hline\n")
      for y in xrange(fil, onl):
	f.write("$$%f$$ "%fle[0][y])
	for z in xrange(col-1):
	  f.write("& $$%f$$"%fle[z+1][y])
	f.write("\\\\ \\hline")
      f.write("\\end{tabular}")
      count +=1
      fil += per
      onl += per
      if onl>len(dat):
	onl = len(dat)
  f.close()
