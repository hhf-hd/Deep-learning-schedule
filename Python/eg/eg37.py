#！/usr/bin/python3

def Func():
    N =10
    L = []
    print("please input 10 numbers")
    for i in range(N):
        x = int(input())
        L.append(x)
    for i in range(N):
        k = i
        minum = L[i]
        for j in range(i+1,N):
            if L[j] < minum:
                k = j
                minum = L[j]
        temp = L[i]
        L[i] = L[k]
        L[j] = temp
    print(L)

Func()

