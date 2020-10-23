import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#plt.style.use('fivethirtyeight')
t=1000   #time for evolution
shape, scale = 2., 2.
population1 = np.random.gamma(shape, scale, size=10000)
all_population_history = [population1.copy()]

def rull(number1,number2):
	if abs(np.log10(number1)-np.log10(number2))<1.2:
		mi = min(number1,number2)
		mutation_i = np.random.normal(loc=0, scale=0.1, size=2)
		return np.abs(mi+ mutation_i[0]), np.abs(mi+ mutation_i[1])
	else :
		ma = max(number1,number2)
		mutation_a = np.random.normal(loc=0, scale=0.1, size=2)
		return np.abs(ma+ mutation_a[0]), np.abs(ma+ mutation_a[1])
def pick(population1):
	half_lenth_of_p = int(len(population1)/2)
	for i in range (half_lenth_of_p):
		population1[2*i] , population1[2*i+1] = rull(population1[2*i] , population1[2*i+1])
	return population1
	
for i in range(t):
	population1 = pick(population1)
	all_population_history.append(population1.copy())
	np.random.shuffle(population1)

def animate(i):
	if i<t:
		bins = [i for i in range(100)]
		plt.cla()
		plt.hist(all_population_history[i],bins,histtype='bar')
		#plt.xscale('log')

ani = FuncAnimation(plt.gcf(), animate, interval=500)
plt.show()