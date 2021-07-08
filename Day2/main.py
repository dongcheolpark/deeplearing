#%%
import numpy as np
import matplotlib.pylab as plt

def set_function(x) : 
	y = x>0;
	return y.astype(np.int64);

def sigmoid(x) : 
	return 1/(1 + np.exp(-x));

def relu(x) :
	return np.maximum(0,x);

x = np.arange(-5.0,5.0,0.1);
y1 = sigmoid(x);
y2 = set_function(x);
y3 = relu(x);

plt.plot(x,y1); # 계단함수
plt.plot(x,y2,linestyle = "--"); # 시그모이드함수 (1/1+e^-1);
plt.plot(x,y3,linestyle = "--"); # ReLU (Rectfied Linear Unit) 함수 
plt.ylim(-0.1,1.1);
plt.show();
# %%
