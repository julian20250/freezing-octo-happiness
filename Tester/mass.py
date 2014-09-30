import os
import string
import numpy as np

def cleaner(list_name):
  list_name = [x.split(" ") for x in list_name]
  list_name = sum(list_name, [])
  while True:
    try:
      list_name.remove('')
    except (ValueError):
      break
  while True:
    try:
      list_name.remove("\n")
    except:
      break
  return list_name
class my_start:
  """
  Enjoy this piece of code made to know by Nmap who is connected to the net.
  """    
  
  def who_is_here(self):
      ip_mena = os.popen("ip route").readlines()
      ip_mena = cleaner(ip_mena)
      my_use = ip_mena.index("static")+1
      being = os.popen("sudo nmap -sP "+ip_mena[my_use]).readlines()
      being = cleaner(being)
      count = 0
      while True:
	try:
	  if count == 0:
	    print "[*]Your Host is " + being[being.index("for")+1]
	    being.remove("for")
	    count += 1
	    
	    
	  if count == 1:
	    to = os.popen("hostname -I").readlines()
	    to = "".join(to)	    
	    print "[*]Your Ip Address is " + to
	    being.remove(to)
	    count +=1
	  print being[being.index("for")+1]
	  being.remove("for")
	except:
	  break

  def justrandom(self):
    b = list(string.ascii_lowercase)
    r = []
    m = []
    for x in xrange(9):
      m.append(np.random.randint(0, 26))
    for x in m:
      r.append(b[x])  
    return "".join(r)

my_start().who_is_here()
print my_start().justrandom()
