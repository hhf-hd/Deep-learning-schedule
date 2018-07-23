#!/usr/bin/python3
L = [1,1]
def fib1(num,L):
	a,b =1,1
	for i in range(2,num):
		a,b = a+b,a
		L.append(a)
	return L
print(fib1(4,L))
