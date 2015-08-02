class fraction():
	""" 
	Function designed to make operations between fractions,
	expressing the result as a fraction. The fraction must
	be inserted as (a/b).
	"""	
	def __init__(self, frac):
		part = frac.split("/")
		self.num = part[0]
		self.den = part[1]
		self.frac = frac

	def list_duplicates_of(self, seq, item):
    		#http://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list
		start_at = -1
    		locs = []
		while True:
        		try:
            			loc = seq.index(item,start_at+1)
        		except ValueError:
            			break
        		else:
            			locs.append(loc)
            			start_at = loc
    		return locs
	
	def productory(self, h):
		e=1
		for x in h:
			e*=x
		return e
	
	def simplifier(self, n):
		n = n.split("/")
		n[0], n[1]=int(n[0]), int(n[1])
		dfer=1
		if n[0]<0:
			n[0]=-1*n[0]
			dfer= 0
		r1, r2 = xrange(2, n[0]+1), xrange(2, n[1]+1)
		h1, h2= [], []
		for x in r1:
			if n[0]%x==0:
				h1.append(x)
		for x in r2:
			if n[1]%x==0:
				h2.append(x)
		g = [x for x in h1 if x in h2]
	        u1, u2 =n[0], n[1]
	        debv=0
	        while len(g)!=0:
			debv=5
			u1, u2= u1/g[0], u2/g[0]
			r1, r2 = xrange(2, u1+1), xrange(2, u2+1)
			h1, h2= [], []
			for x in r1:
				if u1%x==0:
					h1.append(x)
			for x in r2:
				if u2%x==0:
					h2.append(x)
			g = [x for x in h1 if x in h2]
		if dfer==0:
			u1=-1*u1
		if debv==5:
			if u2==1:
				print "\nYour fraction is %i/%i"%(u1,u2)+" = %i\n"%u1
			else:
				print "\nYour fraction is %i/%i\n"%(u1,u2)
		else:
			print "\nYour fraction is %i/%i\n"%(u1,u2)
	      
	def summ(self, f=[]):
		nums=[self.num]
		dens=[self.den]
		for x in f:
			a =x.split("/")
			nums.append(a[0])
			dens.append(a[1])	 
		count = 0
		nums, dens = [int(x) for x in nums], [int(x) for x in dens]

		if dens.count(dens[0])!=len(dens):
			for x in dens:
				a = self.list_duplicates_of(dens, x)
				if len(a)>1:
					b = [nums[y] for y in a]
					d = sum(b)
					c = 0
					for y in a:
						dens.pop(y-c)
						nums.pop(y-c)
						c+=1
					nums.append(d)
					dens.append(x)
		for x in xrange(len(dens)):
			for y in xrange(len(dens)):
				if x!=y:
					nums[y] = nums[y]*dens[x]
		nums = sum(nums)
		dens = self.productory(dens)
		self.simplifier("%i/%i"%(nums, dens))
	
	def product(self, f=[]):
		nums=[self.num]
		dens=[self.den]		
		for x in f:
			a =x.split("/")
			nums.append(a[0])
			dens.append(a[1])
		nums, dens = [int(x) for x in nums], [int(x) for x in dens]
		nums = self.productory(nums)
		dens = self.productory(dens)		
		self.simplifier("%i/%i"%(nums, dens))
	
	def potentiation(self, i):
		if i<0:
			nums=(self.den)**i
			dens=(self.num)**i
		else:
			nums=int(self.num)**i
			dens=int(self.den)**i
		self.simplifier("%i/%i"%(nums, dens))
		  
print ("\nOptions:\n-Summatory of fractions --> sum.\n-Productory of fractions --> prod.\n-Elevation of fractions (no decimal power) --> pot.\n"
	"-Just simplify --> sim.\n")

while True:
	w = raw_input("Insert the begining fraction in the form (a/b) > ")
	t = fraction(w)
	op = raw_input("Insert the option > ")

	if op == "sum":				
		r = raw_input("Insert fractions separated by commas, in the same way as the begining one > ")
		r = r.split(",")
		t.summ(r)
	elif op == "prod":
		r = raw_input("Insert fractions separated by commas, in the same way as the begining one > ")
		r = r.split(",")
		t.product(r)
	elif op == "pot":
		j = input("Insert power > ")
		t.potentiation(j)
	elif op == "sim":
		t.simplifier(w)
	else:
		print "No option named %s."%op
