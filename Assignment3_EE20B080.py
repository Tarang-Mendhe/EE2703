""" ASSIGNMENT 3
Tarang Narendra Mendhe 
EE20B080

"""
from pylab import *
import scipy.special as sp
from scipy.linalg import lstsq
import numpy as np

#Q1 "fitting.dat" has been generated
#Q2
a=loadtxt("fitting.dat")

#Q3 and Q4
def function(t,A,B):
    return A*sp.jv(2,t) + B*t
N=len(a)
F=[] 
t=[] #time array
for i in range(0,len(a)) :
    x = a[i,1:]
    F.append(x)
    t.append(a[i,0])
t= np.array(t)
F= np.array(F)
f=function(t,1.05,-0.105)# actual function
sigma=logspace(-1,-3,9)
F= np.array(F)
plot(t,F)
plot(t,f)
xlabel(r'$t$',size=20)
ylabel(r'$f(t)+noise$',size=20)
title(r'Q4.Data to be fitted',size =22)
grid(True)
legend(["$\u03C3_1$=%.4f"%sigma[0],"$\u03C3_2$=%.4f"%sigma[1],"$\u03C3_3$=%.4f"%sigma[2],"$\u03C3_4$=%.4f"%sigma[3],"$\u03C3_5$=%.4f"%sigma[4],"$\u03C3_6$=%.4f"%sigma[5],"$\u03C3_7$=%.4f"%sigma[6],"$\u03C3_8$=%.4f"%sigma[7],"$\u03C3_9$=%.4f"%sigma[8],"$\u03C3_4$=True Value"],loc= 'upper right')
show()

#Q5
errorbar(t[::5],F[:,0][::5],std(F[:,0]),fmt="ro")
xlabel(r"$t$",size=20)
title(r"Q5:Data points for $\sigma$ = 0.1 along with exact function",size =22)
plot(t,f,label = r"True value")
legend()
show()

#Q6
M=c_[sp.jv(2,t),t]  

#Q7
A = linspace(0,2,20)
B = linspace(-0.2,0,20)
epsilon = np.zeros((len(A),len(B)))
fk = f
for i in range(len(A)):
    for j in range((len(B))):
        epsilon[i,j] = np.mean(np.square(fk - function(t,A[i],B[j])))

#Q8        
cp = contour(A,B,epsilon,20)
plot(1.05,-0.105,"ro")
annotate(r"$Exact\ location$",xy=(1.05,-0.105))
clabel(cp,inline=True)
xlabel(r"$A$",size=20)
ylabel(r"$B$",size=20)
title(r"Q8:Countour plot for $\epsilon_{ij}$",size =22)
show() 

#Q9 and Q10
A_err=[]
B_err=[]
p,resid,rank,sig=lstsq(M,F[:,2])   
for i in range(9) :
    p,resid,rank,sig=lstsq(M,F[:,i])     
    A_err.append(abs(1.05-p[0]))
    B_err.append(abs(-0.105-p[1]))
plot(sigma,A_err,"ro",linestyle="--", linewidth = 1,label=r"$Aerr$")
legend()
plot(sigma,B_err,"go",linestyle="--",linewidth = 1,label=r"Berr")
legend()
grid(True)
xlabel(r"Noise standard deviation",size=20)
ylabel(r"$MS Error$",size=20)
title("$Q10:Variation\ of\  error\  with\  noise$",size =22)
show()

#Q11
loglog(sigma,A_err,"ro")
errorbar(sigma,A_err,np.std(A_err),fmt="ro",label=r"$Aerr$")
legend()
loglog(sigma,B_err,"go")
errorbar(sigma,B_err,np.std(B_err),fmt="go",label=r"$Berr$")
legend()
grid(True)
ylabel(r"$MS Error$",size=20)
title(r"$Q11:Variation\ of\ error\ with\ noise$",size =22)
xlabel(r"$\sigma_{n}$",size=20)
show()

        


