#!/usr/bin/python3

import numpy as np
p_x  = np.array([[3,3],[4,3],[1,1]])
y = np.array([1,1,-1])

w = np.array([1,0])
b = 0
delat = 1

for i in range(100):
	choice = -1
	for j in range(len(p_x)):
		if y[i] != np.sign(np.dot(w,p_x[0])+b):
			choice = j
			break
	if choice == -1:
		break
	w = w + delat*y[choice]*p_x[choice]
	b = b +delat*y[choice]

print(w)
'''
line_x = [0,10]
line_y = [0,0]

for i in range(len(line_x)):
	line_y[i] = (-w[0]*line_x[i]-b)/w[1]

plt,plot(line_x,line_y)
'''