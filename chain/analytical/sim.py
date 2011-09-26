#!/usr/bin/python

from scipy.optimize import fmin_tnc
import matplotlib.pyplot as plot

from chain11 import chain

K_A		= 1/5.e-6
K_B		= 1/50.e-6
K_C		= 1/50.e-6

M_tot	= 1.E-6
L_start = 1.E-9
L_end	= 10.E-6

N_end	= 10
Points	= 20

# No more args

x = []
y = []

L_step = (L_end - L_start) / Points
L_tot = L_start
while (L_tot < L_end):

	guess = [max(0,M_tot-L_tot),max(0,L_tot-M_tot)]
	limits = [(0,None),(0,None)]

	ret = fmin_tnc(chain,guess,args=(M_tot,L_tot,K_A,K_B,N_end), approx_grad=True,bounds=limits,disp=0,rescale=0)
	full = chain(ret[0],M_tot,L_tot,K_A,K_B,N_end,True)
		
	if (ret[2] != 1):
		print ret
#	x.append(L_tot)
#	y.append( (M_tot - ret[0][0])/M_tot )
	
	x.append(L_tot/M_tot)
	
	
#	print str(L_tot/M_tot)+"\t",
	temp = []
	for z in full:
		temp.append(z['Mb']/(M_tot - ret[0][0]))	
#		print str(z['Mb'])+"\t",
#	print "\t"
	y.append(temp)
	
	L_tot += L_step

plot.plot(x,y)
plot.ticklabel_format(style='scientific',axis='x',scilimits=(-3,3))
plot.show()


# 			EINVAL       = -2 # Invalid parameters (n<1)
#           INFEASIBLE   = -1 # Infeasible (low > up)
#           LOCALMINIMUM =  0 # Local minima reach (|pg| ~= 0)
#           CONVERGED    =  1 # Converged (|f_n-f_(n-1)| ~= 0)
#           MAXFUN       =  2 # Max. number of function evaluations reach
#           LSFAIL       =  3 # Linear search failed
#           CONSTANT     =  4 # All lower bounds are equal to the upper bounds
#           NOPROGRESS   =  5 # Unable to progress
#           USERABORT    =  6 # User requested end of minimization