#!/usr/bin/python3
import math
for i in range(101,201):
	x = int(math.sqrt(i))+1
	tag = 1 #is prime number
	for j in range(2,x+1):
		if i%j == 0:
			tag=0
	if tag == 1:
		print(i)
