#!/usr/bin/python3

pro = int(input("profit: "))
res = 0
para = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
for idx in range(0,6):
    if pro>para[idx]:
        res += (pro-para[idx])*rat[idx]
        print((pro-para[idx])*rat[idx])
        i = para[idx]
    print(res)