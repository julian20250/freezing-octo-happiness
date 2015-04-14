import numpy as np
from string import ascii_lowercase as abc
from string import ascii_uppercase as ABC
import sys 
if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *

def choose(k):
  root = Tk()
  will = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a .txt file')
  root.destroy()
  f = open(will, "r")
  gos = f.read()
  if k == 1:
    gos = gos.replace("\n", " ")
  else:
    pass
  
def assign(sca, er):
  if sca%len(er) == 0:
    t = [sca/len(er) for x in xrange(len(er))]

  else:
    t= [sca/len(er) for x in xrange(len(er)-1)]+[sca%len(er)]

  u = []
  count = 0

  if sca%len(er) == 0:
    for x in xrange(len(er)):
      u.append(n[count:count+t[x]])
      count = count+t[x]

  else:
    for x in xrange(len(er)):
      u.append(n[count:count+t[x]])
      count = count+t[x]
    
  u = [int(x) for x in u]
  count=0
  while count == 0:
    count = 1
    for x in u:
      for y in u[u.index(x)+1:]:
	if x == y: 
	  count = 0
	  gt = u.index(x)
	  if (x+1)/(10**int(t[0])) != 0:
	    u.insert(gt, int("1"*t[0]))
	  else:
	    u.insert(gt, x+1)
	  u.remove(x)
  u = [str(x) for x in u]
  
  return u

e = list(abc)+list(ABC)+[" ", "!", "?", ".", ";", "'", "-", ","]+[str(x) for x in xrange(10)]+[None] #Characters
# None is appended because the last item is the residue.

print ("This program encrypts a given text with a seed that can be random or given. Also, it can decrypt a given text with a given seed"
  ". Then, there are two options:\n\n1. Encrypt.\n2. Decrypt.\n")
m = input("Insert the number of the option > ")

if m ==1:
  b = input("Insert the length of the seed (int)> ") #Number of bytes (minimun == len(e))

  if type(b) != int:
    raise ValueError("This input must be an integer.")
  if len(e) > int("9"*(b/len(e))):
    raise EnvironmentError("Insufficient length of seed to do the minimal combinations, insert more.")


  q = raw_input("Enable automatic seed? (y/n) > ")

  if q == "y" or q == "Y":
    n = ""
    for x in xrange(b):
	    n = n + str(np.random.randint(1,10))

  elif q == "n" or q == "N":
    n = raw_input("Insert your seed > ")
    if b<len(n):
      raise EnvironmentError("You said that the lenght is %i, but you put a thing with length %i."%())
    try:
	    l = [int(x) for x in n]
    except ValueError:
	    raise ValueError("This input only accepts numbers.")
    for x in n:
      if x == "0":
	raise TypeError("No zeros please.")
    l = None
    for x in xrange(b-len(n)):
	    n = n + str(np.random.randint(1, 10))

  else:
    raise EnvironmentError("Invalid option.")

  u = assign(b, e)

  L = raw_input("Do you have a txt with the text? (y/n) > ")
  if L == "y" or L == "Y":
    Q = choose(1)    
  elif L == "n" or L == "N":
    Q = raw_input("Insert your text > ")
  else:
    raise EnvironmentError("%s is not a valid option.")
  P = ""
  for x in Q:
    try:
      P = P+u[e.index(x)]
    except ValueError:
      raise ValueError("%s is not in the list e, add it first."%x)

  print "\n- Your seed is %s. \n"%n
  #print "- Your changing list is %s \n"%u[:-1] #Discomment this to show the changing list 
  print "- Your text is: %s. \n"%Q
  print "- The result is : \n%s"%P
  wast = raw_input("\nDo you want the result in a txt? (y/n) > ")
  if wast == "y" or wast == "Y":
    forg = ""
    tim = [e[np.random.randint(26)] for x in xrange(7)]
    for x in tim:
      forg = forg+x
    f = open(forg, "w")
    f.write(P)
    print "Done!, the file was called %s"%forg
  print "Bye!"
elif m == 2:
  n = raw_input("Type your seed > ")
  try:    
    l = [int(x) for x in n]
    n = int(n)
  except:
    raise EnvironmentError("This input only accepts integer.")
  n = str(n)
  b = len(n)
  nosen = b/len(e)
  
  if len(e) > int("9"*(b/len(e))):
    raise EnvironmentError("The given seed can't be because of the minimal combinations.")
  
  u = assign(b, e)
  
  L = raw_input("\nDo you have a txt with the code? (y/n) > ")
  
  if L == "y" or L == "Y":
    Q = choose(0)    
  elif L == "n" or L == "N":
    Q = raw_input("Insert your code > ")
  else:
    raise EnvironmentError("%s is not a valid option."%L)
  
  gun = [Q[x:x+nosen] for x in xrange(0, len(Q), nosen)]
  byo = []
  for x in gun:
    onl = 0
    for y in u:      
      if x == y:
	  byo.append(e[u.index(y)])
	  onl = 1
    if onl == 0:
      raise EnvironmentError("Your code is wrong because there is no matches.")
    
  Q = "".join(gun)
  P = "".join(byo)
  print "\n- Your seed is %s. \n"%n
  #print "- Your changing list is %s \n"%u[:-1] #Discomment this to show the changing list 
  print "- Your code is: %s. \n"%Q
  print "- The result is : \n%s"%P
  wast = raw_input("\nDo you want the result in a txt? (y/n) > ")
  if wast == "y" or wast == "Y":
    forg = ""
    tim = [e[np.random.randint(26)] for x in xrange(7)]
    for x in tim:
      forg = forg+x
    f = open(forg, "w")
    f.write(P)
    print "Done!, the file was called %s"%forg	
  print "Bye!"
else:
    raise EnvironmentError(str(m)+" is not a valid input.")
