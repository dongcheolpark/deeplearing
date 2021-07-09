#%%
import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f,x) :
	h = 1e-4;
	return (f(x+h) - f(x-h)) / (2*h);

def function_1(x) :
	return 0.01*x**2 + 0.1*x;

def function_2(x) :
	return numerical_diff(function_1,10)*(x-10) + function_1(10);

x = np.arange(0.0,20.0,0.1);
y = function_1(x);

y2 = function_2(x);

plt.xlabel("x");
plt.ylabel("f(x)");
plt.plot(x,y);
plt.plot(x,y2);
plt.show();