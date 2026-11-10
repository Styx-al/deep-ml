import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if(not len(a[0])==len(b)):
        return -1
    c=[]
    for i in range(len(a)):
        tmp=[]
        for j in range(len(b[0])):
            tmp.append(0)
            for k in range(len(b)):
                tmp[j]+=a[i][k]*b[k][j]
        c.append(tmp)
    return c