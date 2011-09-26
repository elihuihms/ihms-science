from math import sqrt,log10
import matplotlib.pyplot as plot

def chain(vals,M_tot,L_tot,K_A,K_B,N_end,eval=False):
	M_free = vals[0]
	L_free = vals[1]
	
	full = []
	M_sum = 0
	L_sum = 0
	for n in range(1,N_end+1):
		
		M_step = 0
		L_step = 0
		for m in range(n-1,(4*n)+2):
			
			if (m == 0):
				P = 0
			elif (m < n+2):
				P = (M_free**n) * (L_free**m) * K_A**(n+m-1)
			else:
				P = (M_free**n) * (L_free**m) * K_A**(2*n) * K_B**(m-n-1)
			
			M_step += n * P
			L_step += m * P
				
		M_sum += M_step
		L_sum += L_step
	
		if (eval):
			full.append({'n':n,'Mb':M_sum,'Lb:':L_sum})
	
	M_diff = sqrt((M_tot - M_free - M_sum)**2)/M_tot
	L_diff = sqrt((L_tot - L_free - L_sum)**2)/L_tot

	if (eval == False):
		return M_diff+L_diff
	else:
		return full
	
def mkPlot(Mf_low,Mf_high,Lf_low,Lf_high,args):
	x = []
	y = []
	z = []
	
#	Mf_low = 1.e-30
#	Mf_high = 1.e-1
	
#	Lf_low = 1.e-7
#	Lf_high = 1.e-2

	for i in range(int(log10(Mf_low))*10,int(log10(Mf_high))*10):
		M = 10.**(i/10.)
		
		x = []
		temp = []
		for j in range(int(log10(Lf_low))*10,int(log10(Lf_high))*10):
			L = 10.**(j/10.)
	
			x.append(log10(L))
			temp.append(log10( chain(args[0],args[1],args[2],args[3],args[4],args[5],args[6]) ))
			
		y.append(log10(M))
		z.append(temp)
		
	plot.title("M_tot:"+str(args[1])+", L_tot:"+str(args[2]))
	plot.contourf(x,y,z,50)
	plot.xlabel("[L]")
	plot.ylabel("[M]")
	plot.show()