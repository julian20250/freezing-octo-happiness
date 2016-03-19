import sys

f= open("data.txt", "w")
a=[2]
p=2
count=2
count2=0
while True:
  count+=1
  flag=0
  for x in a:
    if count%x==0:
      flag=1
      
  if flag==0:
    a.append(count)
    if a[-1]==a[-2]+2:
      f.write("%i %i\n"%(a[-1], a[-2]))
      count2+=1
      print "\rFound %i pairs"%count2,
      sys.stdout.flush()
  
