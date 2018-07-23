#!/usr/bin/python3
# -*- coding:UTF-8 -*-

Tn = 0
Sn = []
Tol = 0
n = int(input("n is : "))
a = int(input("a is : "))
for count in range(n):
    Tn = Tn + a 
    a = a * 10
    Sn.append(Tn)
    print (Tn)
    Tol += Tn
    print (Tol)

