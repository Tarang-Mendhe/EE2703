#EE20B080 
#Tarang Mendhe
#EE2703 Assignment 8
#17/4/2022

#Q1.Working through given example
from pylab import *
x=rand(100)
X=fft(x)
Y=ifft(X)
c_[x,Y]
print (abs(x-Y).max())
print (x)


# In[4]:


x=linspace(0,2*pi,128)
y=sin(x)
Y=fft(y)
figure(figsize=(8,12))
subplot(3,1,1)
plot(abs(Y),lw=2)
grid(True)
subplot(3,1,2)
plot(unwrap(angle(Y)),lw=2)
grid(True)
subplot(3,1,3)
plot(Y)
show()


# In[5]:


from pylab import *
x=linspace(0,2*pi,128)
y=sin(5*x)
Y=fft(y)
figure(figsize=(8,8))
subplot(2,1,1)
plot(abs(Y),lw=2)
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\sin(5t)$",size=16)
grid(True)
subplot(2,1,2)
plot(unwrap(angle(Y)),lw=2)
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$k$",size=16)
grid(True)
savefig("fig9-1.png")
show()


# In[6]:


#correcting errors
x=linspace(0,2*pi,129);x=x[:-1]  #the overlap between 0 and 2Pi is prevented
y=sin(5*x)
Y=fftshift(fft(y))/128.0
w=linspace(-64,63,128)
figure(figsize=(8, 8))
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-10,10])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\sin(5t)$",size=16)
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2,)
ii=where(abs(Y)>1e-3)
plot(w[ii],angle(Y[ii]),'go',lw=2)
xlim([-10,10])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$k$",size=16)
grid(True)
savefig("fig9-2.png")
show()


# In[7]:


#AM modulation
t=linspace(0,2*pi,129);t=t[:-1]
y=(1+0.1*cos(t))*cos(10*t)
Y=fftshift(fft(y))/128.0
w=linspace(-64,63,128)
figure(figsize=(8, 8))
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-15,15])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\left(1+0.1\cos\left(t\right)\right)\cos\left(10t\right)$")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2)
xlim([-15,15])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig("fig9-3.png")
show()


# In[8]:


#correction for AM
t=linspace(-4*pi,4*pi,513);t=t[:-1]
y=(1+0.1*cos(t))*cos(10*t)
Y=fftshift(fft(y))/512.0
w=linspace(-64,64,513);w=w[:-1]
figure(figsize=(8, 8))
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-15,15])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\left(1+0.1\cos\left(t\right)\right)\cos\left(10t\right)$")
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'ro',lw=2)
xlim([-15,15])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig("fig9-4.png")
show()


# In[25]:


#Q2 Spectrum of sin(t)^3 and cos(t)^3
t=linspace(-4*pi,4*pi,513);t=t[:-1]
y1=sin(t)**3
y2=cos(t)**3
Y1=fftshift(fft(y1))/512.0
Y2=fftshift(fft(y2))/512.0
w=linspace(-64,64,513);w=w[:-1]
figure(figsize=(15, 6))
subplot(2,2,1)
plot(w,abs(Y1),lw=2)
xlim([-15,15])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $sin^3(t)$",size=16)
grid(True)
subplot(2,2,3)
plot(w,angle(Y),'g*',lw=2)
ii=where(abs(Y2)>1e-3)
plot(w[ii],angle(Y2[ii]),'ro')
xlim([-15,15]) 
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
subplot(2,2,2)
plot(w,abs(Y2),lw=2)
xlim([-15,15])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $cos^3(t)$",size=16)
grid(True)
subplot(2,2,4)
plot(w,angle(Y2),'g*')
ii=where(abs(Y2)>1e-3)
plot(w[ii],angle(Y2[ii]),'ro')
xlim([-15,15])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig("fig9-5.png")
show()


# In[26]:


#Q3 Spectrum of cos (20t +5cos(t))
t=linspace(-4*pi,4*pi,513);t=t[:-1]
y=cos(20*t +5*cos(t))
Y=fftshift(fft(y))/512.0
w=linspace(-64,64,513);w=w[:-1]
figure(figsize=(8, 8))
subplot(2,1,1)
plot(w,abs(Y),lw=2)
xlim([-40,40])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\cos\left(20t +5\cos\left(t\right)\right)$",size=16)
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'y*',lw=2)
ii=where(abs(Y)>1e-3)
plot(w[ii],angle(Y[ii]),'ro')
xlim([-40,40])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
savefig("fig9-6.png")
show()


# In[29]:


#Q4 Spectrum of a Gaussian exp(-(t^2)/2)
T = 2*pi
N = 128
iter = 0
tolerance = 1e-15
error = tolerance + 1
# This loop will calculate the DFT and also the error between the calculated and actual 
# Only when the error is less than a tolerance value will the loop be terminated.
while True:
        t = linspace(-T/2,T/2,N+1)[:-1]
        w = N/T * linspace(-pi,pi,N+1)[:-1]
        y = exp(-0.5*t**2)
        iter = iter + 1
        Y = fftshift(fft(y))*T/(2*pi*N)
        Y_actual = (1/sqrt(2*pi))*exp(-0.5*w**2)
        error = mean(abs(abs(Y)-Y_actual))
        if error < tolerance:
            break
        T = T*2
        N = N*2
figure(figsize=(8, 8))
subplot(2,1,1)
plot(w,abs(Y),lw=2)
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $e^{-t^2/2}$",size=16)
xlim([-10,10])
grid(True)
subplot(2,1,2)
plot(w,angle(Y),'y*',lw=2)
ii=where(abs(Y)>1e-3)
plot(w[ii],angle(Y[ii]),'ro')
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
xlim([-10,10])
grid(True)
savefig("fig9-7.png")
show()


# In[ ]:




