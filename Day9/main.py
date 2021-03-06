#%%
import numpy as np
import matplotlib.pyplot as plt;

def numerical_diff(f,x) :
	h = 1e-4;
	return (f(x+h) - f(x-h)) / (2*h);

def gradient_descent(f,init_x,lr = 0.01, step_num = 100) :
	x = init_x;

	for i in range(step_num) :
		grad = numerical_diff(f,x);
		x -= lr*grad
	
	return x;

