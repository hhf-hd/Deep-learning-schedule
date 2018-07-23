#!/usr/bin/python3

def GetRes():
    a = []
    for i in range(2):
        a.append([])
        for j in range(2):
        	a[i].append(float(input("input")))
    for i in range(2):
        for j in range(2):
            print(a[i][j],end=" ")
GetRes()
