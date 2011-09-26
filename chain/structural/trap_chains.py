from random import random,seed
from dump import dumpObj
#seed(1)

class simWorld:
	total_trap	= 0
	total_at	= 0
	
	dG_bind		= 0
	dG_interact	= 0
	dG_chain	= 0
	
	clusters=[]
	
	def __init__(self):
		myCluster = Cluster()
		myTRAP_1 = TRAP()
		myTRAP_2 = TRAP()
		myAT = antiTRAP()
		
		myCluster.addTRAP(myTRAP_1)
		myCluster.addAT(myAT)
		myCluster.addTRAP(myTRAP_2)
		
		dumpObj(myTRAP_1,maxlen=200)
		dumpObj(myTRAP_2,maxlen=200)
		dumpObj(myAT,maxlen=200)
	
class Cluster:
	TRAP = []
	AT = []

	def __init__(self): pass
	
	def addTRAP(self,newTRAP):
		if (len(self.TRAP) < 1):
			self.TRAP.append(newTRAP)
		else:
			# make a list of available AT binding sites
			sites = []
			for i in range(len(self.AT)):
				for j in range(len(self.AT[i].boundTo)):
					if (self.AT[i].boundTo[j] == None):
						sites.append([i,j])
			
			# are all sites occupied?
			if (len(sites) < 1):
				return false
			
			# pick a random AT site from the list we compiled
			site = sites[int(len(sites)*random())]

			# which site of newTRAP is bound to the AT site?
			TRAP_site = int(len(newTRAP.boundTo)*random())
			
			# tell the TRAP what AT it is bound to
			newTRAP.boundTo[TRAP_site] = self.AT[site[0]]
			
			# tell the AT what TRAP it is bound to
			self.AT[site[0]].boundTo[site[1]] = newTRAP
			
			# finally, save a reference to the new TRAP to our local list
			self.TRAP.append(newTRAP)
	
	def addAT(self,newAT):
		if (len(self.TRAP) < 1):
			return false
		
		# make a list of available TRAP binding sites
		sites = []
		for i in range(len(self.TRAP)):
			for j in range(len(self.TRAP[i].boundTo)):
				if (self.TRAP[i].boundTo[j] == None):
					sites.append([i,j])
		
		# are all sites occupied?
		if (len(sites) < 1):
			return false
		
		# pick a random TRAP site from the list we compiled
		site = sites[int(len(sites)*random())]
		
		# which newAT site is bound to the TRAP site?
		AT_site = int(len(newAT.boundTo)*random())
		
		# tell the AT what TRAP it is bound to
		newAT.boundTo[AT_site] = self.TRAP[site[0]]
		
		# tell the TRAP what AT it is bound to
#		self.TRAP[site[0]].boundTo[site[1]] = newAT
		
		# save a reference to the new AT in our local list
		self.AT.append(newAT)
			
	def interactions(self):
		counter = 0
		for i in range(len(self.TRAP)):
			counter += self.TRAP[i].interactions
		return counter
	
	def bound(self):
		counter1 = 0
		counter2 = 0
		
		for i in range(len(self.TRAP)):
			counter1 += self.TRAP[i].bound
		
		for i in range(len(AT)):
			counter2 += self.AT[i].bound
		
		if (counter1 != counter2):
			print "Mismatch when counting occupied binding sites!"
		
		return counter1
	
class TRAP:
	boundTo = [None, None, None, None, None]

	def __init__(self): pass
	
	def interactions(self):
		counter = 0
		for i in range(len(self.boundTo)):
			if (self.boundTo[i] != None):
				if (i == len(self.boundTo)):
					if (self.boundTo[0] != 1):
						counter += 1
				else:
					if (self.boundTo[i+1] == 1):
						counter += 1
		return counter
		
	def bound(self):
		counter = 0
		for i in range(len(self.boundTo)):
			if (self.boundTo[i] != None):
				counter+= 1
		return counter
		
class antiTRAP:
	boundTo = [None, None, None]
	
	def __init__(self): pass
	
	def bound(self):
		counter = 0
		for i in range(len(self.boundTo)):
			if (self.boundTo[i] != None):
				counter += 1
		return counter