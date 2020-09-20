import math
def gt(n):
    tich=1;
    for i in range(1,n+1):
        tich*=i
    return tich

def prob(n,p,r):
     x=gt(n)
     y=gt(r)
     z=gt(r-n)
     xs=(r/(y*z)*1/(2**n))
     return xs


def infoMeasure(n,p,r):
    k = -(math.log2(prob(n, p, r)))
    return k

def sumProb(N,p,r):
    '''
    created by VuMinhHieu
    '''
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, r)
    return sum

def approxEntropy(N,p,r):
    '''
    hello world,python!
    ham tinh trung binh luong tin
    '''
    avg = 0
    for i in range(1, N + 1):
        avg += infoMeasure(i, p, r)
    avg = avg / N
    return avg
