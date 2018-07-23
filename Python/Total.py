#!/usr/bin/python3

'''
for j in range(2,1001):
	s = j
	for i in range(1,j):
		if j%i == 0:
			s -= i
	if s == 0:
		print(j)
'''
'''
hei = 100.0
height = []
tol = []
time =10
for i in range(1,time+1):
	if i == 1:
		tol.append(hei)
	else:
		tol.append(2*hei)
	hei /= 2
	height.append(hei)

print("total num is %s" % sum(tol))
print(height[-1])
'''
'''
res = 1
for i in range(9):
	res = (res+1)*2
print(res)
'''
'''
from sys import stdout

for i in range(4):
	for j in range(2-i+1):
		stdout.write(" ")
	for k in range(2*i+1):
		stdout.write("*")
	print("")

for i in range(3):
	for j in range(i+1):
		stdout.write(" ")
	for k in range(4-2*i+1):
		stdout.write("*")
	print(" ")

'''
'''
x1 = 2.0
x2 = 1.0
res = 0
for i in range(20):
	res += x1/x2
	x1, x2 = x1+x2,x1
print(res)
'''
'''
temp = 1
res = 0
for i in range(1,21):
	temp *= i
	res += temp
print(res)
'''
'''
def recursion(n):
	if n == 1:
		return 1
	else:
		return n*recursion(n-1)
print(recursion(5))
'''
'''
def output(chr,l):
	if l == 0:
		return 
	print(chr[l-1])
	output(chr,l-1)

strr = input("char is : ")
l = len(strr)
output(strr,l)
'''
'''
x = int(input("please input a data: "))
a =str(x)
l =len(a)
flag =True

for i in range(int(l/2)):
	if a[i] != a[-i-1]:
		flag =False
		break
if flag:
	print("Yes")
else:
	print("No")
'''
'''
letter = input("input a letter: ")
if letter == "S":
	print("second letter")
	S_l = input("letter")
	if S_l =="a":
		print("Saturday")
	elif S_l == "u":
		print("Sunday")
	else:
		print("data error")
elif letter == "T":
	print("second letter")
	S_l = input("letter")
	if S_l =="h":
		print("Thursday")
	elif S_l == "u":
		print("Tuesday")
	else:
		print("data error")
elif letter == "M":
	print("Monday")
elif letter == "F":
	print("Friday")
elif letter == "W":
	print("Wednesday")
else:
	print("data error")
'''
'''
L = [1,2,3,4]

st = ",".join(str(n) for n in L)
print(st)
'''
'''
for i in range(2,100):
	if i == 2:
		print(i)
	else:
		Flag = 1	
		for j in range(2,i):
			if i%j == 0:
				Flag = 0
		if Flag == 1:
			print(i)
'''
'''

if __name__ == "__main__":
	a = []
	SUM = 0.0
	for i in range(3):
		a.append([])
		for j in range(3):
			a[i].append(float(input("data")))
	for i in range(3):
		SUM += a[i][i]
	print(SUM)
'''
'''
M_a = []
M_b = []
Res = []
for i in range(3):
	M_a.append([])
	for j in range(3):
		M_a[i].append(int(input("data a: ")))
for i in range(3):
	M_b.append([])
	for j in range(3):
		M_b[i].append(int(input("data a: ")))
for i in range(3):
	Res.append([])
	for j in range(3):
		Res[i].append(M_a[i][j]+M_b[i][j])
print(Res)
'''
'''
MAXIMUM = lambda x,y:(x>y)*x+(x<y)*y
MINIMUM = lambda x,y:(x>y)*y+(x<y)*x

print(MAXIMUM(2,5))
print(MINIMUM(3,9))
'''
'''
import random 

print(random.uniform(10,20))
'''
'''
from sys import stdout
a = []

for i in range(10):
	a.append([])
	for j in range(10):
		a[i].append(0)
for i in range(10):
	a[i][0] = 1
	a[i][i] = 1
for i in range(2,10):
	for j in range(1,i):
		a[i][j] = a[i-1][j] + a[i-1][j-1]
for i in range(10):
	for j in range(i+1):
		stdout.write(str(a[i][j]))
		stdout.write(" ")
'''
'''
a = input("data a: ")
b = input("data b: ")
c = input("data c: ")

def swap(x1,x2):
	return x2,x1

if a<b:
	a,b = swap(a,b)
if a<c:
	a,c = swap(a,c)
if b<c:
	b,c = swap(b,c)
print(a,b,c)
'''
'''
a = [4,2,7,12,5,1]
l = len(a)
MIN = a[0]
Min_idx = 0
MAX = a[0]
Max_idx = 0
for i in range(1,l):
	if a[i] < MIN:
		MIN = a[i]
		Min_idx = i
for i in range(1,l):
	if a[i] > MIN:
		MIN = a[i]
		Max_idx = i
a[0],a[Max_idx] = a[Max_idx],a[0]
a[l-1],a[Min_idx] = a[Min_idx],a[l-1]
print(a)
'''

person = {"h":23,"y":22,"z":13}
m = "h"
for key in person.keys():
	if person[m] < person[key]:
		m = key
print("%s %s "%(m,person[m]))


