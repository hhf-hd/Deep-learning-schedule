#！/usr/bin/python3
import math
from collections import Iterable
#name = input("please input your name")
#print("hello ",name)
#print("1024*768= ",1024*768)
'''
classmate = ["hhf","yxh","hyf"]
print (classmate)
classmate.append("sys")
classmate.insert(1,"zzx")
classmate.pop(2)
print (classmate)
year = input("your age : ")
birth = int(year)
if birth>2000:
    print("ok")
else:
    print("no")
sum = [1,2,3,4,5,6]
a= 0
for x in sum:
    a = a+x
print(a)
d = {"hhf": 1,"sy":2}
print(d)
d["hhf"] = 4;
d["yxh"] = 9;
print(d)
def my_abs(x):
    if x>0:
        return x;
    else:
        return -x;
print (my_abs(-2))
def quadratic(a,b,c):
    res = b*b - 4*a*c
    if res>0:
        x = math.sqrt(res)
        x1 = (x-b)/2*a
        x2 = -(b+x)/2*a
        return x1,x2
    else:
        if res==0:
    	    x3 = -b/2*a
    	    return x3
        else:
            return 0
print (quadratic(5,8,3))
print (quadratic(2,4,2))
print (quadratic(3,4,9))

def add_end(L=[]):
    L.append("end")
    return L
print(add_end())
print(add_end())

def add_end2(L=None):
    if L is None:
        L = []
    L.append("start")
    return L

print(add_end2())
print(add_end2())

def cal(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i*i
    return sum
print(cal([1,2,5,7]))
para  = [1,4,7]
print(cal(para))

def get(name,gender,**para):
    print("name: ",name,"gender: ",gender,"other: ",para)
name = "hhf"
gender = "F"
get(name,gender,city = "beijing")

def recursion(n):
    if n == 1:
        return 1
    return n*recursion(n-1)
print(recursion(5))

para2 = [1,4,6,7,2,4]
res = []
def slice(para,n):
    for i in range(n):
        res.append(para[i])
    return res
print(slice(para2,3))

L = [x*x for x in range(4)]
G = (x*x for x in range(4))
print(L)
print(G)
print(next(G))
'''
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return "Done"
fib(8)