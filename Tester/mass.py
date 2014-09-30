import os
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
      
      

my_start().who_is_here()