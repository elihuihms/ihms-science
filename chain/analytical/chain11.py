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
