#!/usr/bin/python3

L = []
def reduceNum(num,L):
	k = 2
	while k<num:
		if num%k == 0:
			L.append(k)
			num = num/k
			reduceNum(num)
		else:
			k = k+1
	return L
print(reduceNum(90,L))

