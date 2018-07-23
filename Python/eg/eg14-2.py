#!/usr/bin/python3

def reduceNum(n):
	print("{} = ".format(n))
	if not isinstance(n,int) or n <= 0:
		print("please input a correct number")
		exit(0)
	elif n == 1:
		print("{}".format(n))
	while n!= 1:
		for idx in range(2,n+1):
			if n%index == 0:
				n/=index
				if n==1:
					print(idx)
				else:
					print("{} *".format(idx))
				break
reduceNum(90)
reduceNum(100)
