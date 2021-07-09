#%%
import numpy as np
import matplotlib.pyplot as plt;

def function_2(x) :
	return np.sum(x**2);

x = np.array([np.arange(0,20,0.1), np.arange(0,20,0.1)]);

y = function_2(x);
print(y);

plt.plot(x[0],x[1],y);
# %%
