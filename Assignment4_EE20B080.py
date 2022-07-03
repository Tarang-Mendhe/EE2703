#importing necessory modules
from pylab import *
from scipy import integrate

#defining required functions
def u1(x,k):
    return exp(x) * cos(k*x)
def v1(x,k):
    return exp(x) * sin(k*x)
def v2(x,k):
    return cos(cos(x))* sin(k*x)
def u2(x,k):
    return cos(cos(x)) * cos(k*x)
#function 1 : e^x
def f1(x):
    return exp(x)
#function 2 : cos(cos(x))
def f2(x):
    return (cos(cos(x)))

#Plotting the two functions
figure(figsize=(15, 6))
s=linspace(-2*pi,4*pi,400)
subplot(1,2,1)
grid(True)
semilogy(s,f1(s))   # e^x is plotted in semilogy
ylabel(r"log($e^x$)",size=16)
xlabel(r"x",size=16)
title(r"plot of $e^x$ (semilogy)",size =18)
subplot(1,2,2)
plot(s,f2(s))
xlabel(r"x",size=16)
ylabel(r"cos(cos(x))",size=16)
title(r"plot of $cos(cos(x))$",size =18)
grid(True)

# generating coefficients 
a0_f1=(integrate.quad(f1,0,2*pi)[0])/(2*pi)
a0_f2=(integrate.quad(f2,0,2*pi)[0])/(2*pi)

f1_coeff = [a0_f1]
f2_coeff = [a0_f2]
for k in range(1,26):
    f1_coeff.append(np.abs((integrate.quad(u1,0,2*pi,args=k)[0])/pi))
    f1_coeff.append(np.abs((integrate.quad(v1,0,2*pi,args=k)[0])/pi))
    f2_coeff.append(np.abs((integrate.quad(u2,0,2*pi,args=k)[0])/pi))
    f2_coeff.append(np.abs((integrate.quad(v2,0,2*pi,args=k)[0])/pi))

#plotting semilogy and loglog graphs for coefficients of both the functions
n = arange(0,51)
figure(figsize=(15, 6))
subplot(1,2,1)
semilogy(n, np.abs(f1_coeff), 'ro')
xlabel("n",size="16")
ylabel("Coefficients in log scale",size="16")
title("$e^x$ in semilog",size="18")
grid(True)
subplot(1,2,2)
loglog(n, np.abs(f1_coeff), 'ro')
xlabel("n in log scale",size="16")
ylabel("Coefficients in log scale",size="16")
title("$e^x$ in loglog",size="18")
grid(True)
show()

figure(figsize=(15, 6))
subplot(1,2,1)
semilogy(n, np.abs(f2_coeff), 'ro')
xlabel("n",size="16")
ylabel("Coefficients in log scale",size="16")
title("$cos(cos(x)$ in semilog",size="18")
grid(True)
subplot(1,2,2)
loglog(n, np.abs(f2_coeff), 'ro')
xlabel("n in log scale",size="16")
ylabel("Coefficients in log scale",size="16")
title("$cos(cos(x)$ in loglog",size="18")
grid(True)
show()

#finding coefficients using least square method
x=linspace(0,2*pi,401)
x=x[:-1] # drop last term to have a proper periodic integral
b1=f1(x) # f has been written to take a vector
b2=f2(x)
A=zeros((400,51)) # allocate space for A
A[:,0]=1 # col 1 is all ones
for k in range(1,26):
    A[:,2*k-1]=cos(k*x) # cos(kx) column
    A[:,2*k]=sin(k*x) # sin(kx) column
#endfor
c1=lstsq(A,b1,rcond=-1)[0] # the ’[0]’ is to pull out the best fit vector. lstsq returns a list.
c2=lstsq(A,b2,rcond=-1)[0]


# In[15]:


#graphs for comparision of least square vs direct integration 
figure(figsize=(15, 6))
subplot(1,2,1)
semilogy(n, np.abs(f1_coeff), 'ro',label="True Value")
semilogy(n, np.abs(c1), 'go',label="Least Square Value")
xlabel("n",size="16")
ylabel("Coefficients in log scale",size="16")
title("$e^x$ in semilog",size="18")
grid(True)
legend()
subplot(1,2,2)
loglog(n, np.abs(f1_coeff), 'ro',label="True Value")
loglog(n, np.abs(c1), 'go',label="Least Square Value")
xlabel("n in log scale",size="16")
ylabel("Coefficients in log scale",size="16")
title("$e^x$ in loglog",size="18")
grid(True)
legend()
show()

figure(figsize=(15, 6))
subplot(1,2,1)
semilogy(n, np.abs(f2_coeff), 'ro',label="True Value")
semilogy(n, np.abs(c2), 'go',label="Least Square Value")
xlabel("n",size="16")
ylabel("Coefficients in log scale",size="16")
title("cos(cos(x)) in semilog",size="18")
grid(True)
legend()
subplot(1,2,2)
loglog(n, np.abs(f2_coeff), 'ro',label="True Value")
loglog(n, np.abs(c2), 'go',label="Least Square Value")
xlabel("n in log scale",size="16")
ylabel("Coefficients in log scale",size="16")
title("cos(cos(x)) in loglog",size="18")
grid(True)
legend()
show()

#finding deviations in the two methods
dev1 = abs(abs(np.array(f1_coeff)) - abs(c1))
dev2 = abs(abs(np.array(f2_coeff)) - abs(c2))
max_dev1 = np.max(dev1)
max_dev2 = np.max(dev2)
print(f"maximum deviations for e^x and cos(cos(x)) are {max_dev1} and {max_dev2} respectively")

#plotting exact function vs estimated function (A.c)
figure(figsize=(15, 6))
y=x[::4]      # interval spaces of 4 are taken for clarity of graph
subplot(1,2,1)
semilogy(y,f1(y),label="exact function")
semilogy(y,A.dot(c1)[::4],"go",label="estimated function")
ylabel(r"log($e^x$)",size=16)
xlabel(r"x",size=16)
title(r"plot of $e^x$ (semilogy)",size =18)
grid(True)
legend()
subplot(1,2,2)
plot(y,f2(y),label="exact function")
plot(y,A.dot(c2)[::4],"go",label="estimated function")
xlabel(r"x",size=16)
ylabel(r"cos(cos(x))",size=16)
title(r"plot of $cos(cos(x))$",size =18)
grid(True)
legend()

